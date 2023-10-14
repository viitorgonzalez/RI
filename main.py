from classes.Cc import Cc
from classes.Comparativo import Comparativo
from classes.Leroy import Leroy
from classes.Sodimac import Sodimac
import re

cc = Cc()
leroy = Leroy()
sodimac = Sodimac()

listaComparativo = []

def main():
    cc.read()
    leroy.read()
    sodimac.read()
    encontraMaisBarato()
    
def encontraMaisBarato():
    for item in cc.lista:
        nome = padronizaNome(item.nome)
        if nome != None:
            index = buscaListaIndex(nome)
            if index != None:
                if (listaComparativo[index].precoCC == 0 or item.preco < listaComparativo[index].precoCC):
                    listaComparativo[index].precoCC = item.preco
                if (item.preco < listaComparativo[index].menorPreco):
                    listaComparativo[index].menorPreco = item.preco
                    listaComparativo[index].link = item.link
            else:
                comparativo = Comparativo()
                comparativo.nome = nome
                comparativo.precoCC = item.preco
                comparativo.menorPreco = item.preco
                comparativo.link = item.link
                listaComparativo.append(comparativo)
      
    for item in leroy.lista:
        nome = padronizaNome(item.nome)
        if nome != None:
            
            if nome == "Telha de Fibrocimento 4mm 122X 50cm":
                print(item.link)
            index = buscaListaIndex(nome)
            if index != None:
                if (listaComparativo[index].precoLeroy == 0 or item.preco < listaComparativo[index].precoLeroy):
                    listaComparativo[index].precoLeroy = item.preco
                
                if (item.preco < listaComparativo[index].menorPreco):
                    listaComparativo[index].menorPreco = item.preco
                    listaComparativo[index].link = item.link
            else:
                comparativo = Comparativo()
                comparativo.nome = nome
                comparativo.precoLeroy = item.preco
                comparativo.menorPreco = item.preco
                comparativo.link = item.link
                listaComparativo.append(comparativo)
        
    for item in sodimac.lista:
        nome = padronizaNome(item.nome)
        if nome != None:
            index = buscaListaIndex(nome)
            if index != None:
                if (listaComparativo[index].precoSodimac == 0 or item.preco < listaComparativo[index].precoSodimac):
                    listaComparativo[index].precoSodimac = item.preco
                
                if (item.preco < listaComparativo[index].menorPreco):
                    listaComparativo[index].menorPreco = item.preco
                    listaComparativo[index].link = item.link
            else:
                comparativo = Comparativo()
                comparativo.nome = nome
                comparativo.precoSodimac = item.preco
                comparativo.menorPreco = item.preco
                comparativo.link = item.link
                listaComparativo.append(comparativo)

    listaComparativo.sort(key=lambda x: x.nome)
    
    with open("./result/result.txt", "w", encoding="utf-8") as result:

        cabecalho = "nome"+ " "*35 + "CeC    " + "Leroy  " +"Sodimac" + "Menor Preco" + "link"
        print(cabecalho)
        result.write(cabecalho + "\n")
        for item in listaComparativo:
            nome = item.nome
            precoCC = str(item.precoCC)
            precoLeroy = str(item.precoLeroy)
            precoSodimac = str(item.precoSodimac)
            menorPreco = str(item.menorPreco)
            link = item.link
            linha = nome + " "*(40-len(nome))
            linha += precoCC + " "*(8-len(precoCC))
            linha += precoLeroy + " "*(8-len(precoLeroy))
            linha += precoSodimac + " "*(8-len(precoSodimac))
            linha += menorPreco + " "*(12-len(menorPreco))
            linha += link
            print(linha)
            result.write(linha + "\n")
        
def padronizaNome(nome):
    if re.search(r"telha.*fibrocimento.*", nome, re.IGNORECASE):
        tamanho = padronizaTamanho(nome)
        if tamanho != None:
            return "Telha de Fibrocimento" + " " + tamanho

def padronizaTamanho(nome):
    tamanho = None
    if re.search(r"1?22", nome):
        tamanho = "122"
    elif re.search(r"1?53", nome):
        tamanho = "153"
    elif re.search(r"1?83", nome):
        tamanho = "183"
    elif re.search(r"2?13", nome):
        tamanho = "213"
    elif re.search(r"2?44|2?40", nome):
        tamanho = "244"
    elif re.search(r"3?05", nome):
        tamanho = "305"
    elif re.search(r"3?66", nome):
        tamanho = "366"
    else:
        return None
    
    if re.search(r"0,4cm|4mm", nome):
        tamanho = "4mm " + tamanho + "X 50cm"
    elif re.search(r"0,5cm|5mm", nome):
        tamanho = "5mm " + tamanho + "X110cm"
    elif re.search(r"0,6cm|6mm", nome):
        tamanho = "6mm " + tamanho + "X110cm"
    else:
        return None
    return tamanho

def buscaListaIndex(nome):
    for item in listaComparativo:
        if item.nome == nome:
            return listaComparativo.index(item)

if __name__ == "__main__":
    main()