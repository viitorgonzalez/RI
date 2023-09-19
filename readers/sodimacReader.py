import requests
from bs4 import BeautifulSoup

def sodimacRead():
  baseUrl = "https://www.sodimac.com.br"
  url = "https://www.sodimac.com.br/sodimac-br/category/cat170729/porcelanato/?currentpage=1&=&f.product.brandName=eliane"
  urlPaginationOne = "https://www.sodimac.com.br/sodimac-br/category/cat170729/porcelanato/?currentpage="
  urlPaginationTwo = "&=&f.product.brandName=eliane"
  vetorPaginas=[]
  vetorNomePisos=[]
  vetorPaginas.append(url)
  i=1

  with open("./data/sodimacProducts.txt", "w", encoding="utf-8") as produto:
    for y in vetorPaginas:
        busca = requests.get(y)
        soup = BeautifulSoup(busca.content, 'html.parser')

        alvo = soup.find_all("div", {"class":"ie11-product-container"})

        if(alvo):
            for x in alvo:
                nome = x.find("h2", {"class":"product-title"}).text
                inteiro = x.find("span", {"class":"jsx-1747766189"}).text
                decimais = x.find("span", {"class":"decimals"}).text
                valor = inteiro + decimais
                link = baseUrl + x.find("a")["href"] 

                produto.write(nome + '\n')
                produto.write(valor + '\n')
                produto.write(link + '\n')

            nextPage = soup.find("span", class_="jsx-4278284191 cs-icon-arrow_right")
            if(nextPage):
                i = i + 1
                nextUrl = urlPaginationOne + str(i) + urlPaginationTwo
                vetorPaginas.append(nextUrl)
