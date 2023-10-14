import json
from bs4 import BeautifulSoup
import requests
from classes.Result import Result

class Leroy:
  def __init__(self):
    self.lista = []
    
  def read(self):
    url = "https://www.leroymerlin.com.br/telhas-de-fibrocimento"
    vetorPaginas=[]
    vetorNomePisos=[]
    vetorPaginas.append(url)
    i=1
    fim = False

    with open("./data/leroyProducts.txt", "w", encoding="utf-8") as produto:
      for y in vetorPaginas:
          busca = requests.get(y)
          soup = BeautifulSoup(busca.content, 'html.parser')

          data = json.loads(soup.find_all("script", {"type":"application/ld+json"})[-1].text)
          
          if(data):
              for x in data:
                  # Se não tiver offers acabou as páginas
                  if(x.get('offers')==None):
                      fim = True
                      break
                  nome = x["name"]
                  link = x["url"]
                  valor = x["offers"][0]["price"]

                  result = Result()
                  result.nome = nome
                  result.preco = float(valor)
                  result.link = link
                  self.lista.append(result)
                  
                  produto.write(nome + "\n")
                  produto.write(link + "\n")
                  produto.write(str(valor) + "\n")

          if(fim):
              break

          i=i+1
          vetorPaginas.append(url + "?page=" + str(i))