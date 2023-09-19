import requests, json
from bs4 import BeautifulSoup

def leroyRead():
  url = "https://www.leroymerlin.com.br/pisos-e-revestimentos-porcelanatos/marca/Eliane?page=1"
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

                produto.write(nome + "\n")
                produto.write(link + "\n")
                produto.write(str(valor) + "\n")

        if(fim):
            break

        i=i+1
        vetorPaginas.append("https://www.leroymerlin.com.br/pisos-e-revestimentos-porcelanatos/marca/Eliane?page="+str(i))
