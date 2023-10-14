from bs4 import BeautifulSoup
import requests

from classes.Result import Result

class Cc:
  def __init__(self):
    self.lista = []
        
  def read(self):
    baseUrl = "https://www.cec.com.br"
    url = "https://www.cec.com.br/busca?q=telha"
    
    vetorPaginas = [url] 
    visited = set()  

    with open("./data/ccProducts.txt", "w", encoding="utf-8") as produto:
        while vetorPaginas:
            url = vetorPaginas.pop(0)
            visited.add(url)

            busca = requests.get(url)
            soup = BeautifulSoup(busca.content, "html.parser")

            alvo = soup.find("div", class_="products")
            products = alvo.find_all("div", class_="product d-flex")

            for y in products:
                nameTarget = y.find("span", class_="product-name-text")
                priceTarget = y.find("span", class_="value-full")
                hrefTarget = baseUrl + y.find("a", class_="photo")["href"]

                # Extrai o preço e remove "R$"
                priceText = priceTarget.text.replace("R$", "").replace(",",".").strip()

                result = Result()
                result.nome = nameTarget.text
                result.preco = float(priceText)
                result.link = hrefTarget
                
                self.lista.append(result)

                produto.write(nameTarget.text + '\n')
                produto.write(priceText + '\n')
                produto.write(hrefTarget + '\n')

            # Procura a próxima página
            pagination = soup.find("ul", class_="pagination")
            if pagination:
                Li = pagination.find_all("li", class_="li_bt_pag")
                for z in Li:
                  aElement = z.find("a", class_="bt_pag")
                  iElement = aElement.find("i", class_="fa fa-angle-right")
                  if aElement and iElement:
                      nextUrl = baseUrl + aElement["href"]
                      if nextUrl not in visited:
                          vetorPaginas.append(nextUrl)
