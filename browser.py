
import sys
import os
import requests
import locale
from colorama import Fore, init
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
BLUE = "\u001b[1;34m"
RESET = "\u001b[0;0m"
lista = []
diretorio = ""
init(autoreset=True)

# FUNCAO LIBERAR DIRETORIO


def apagar_arquivo(a):
    b = a.split(".")
    if b[0] == "www":
        del b[0]
    os.remove(f"{diretorio}/{b[0]}")


# PROGRAMA EM SI
if len(sys.argv) > 1:
    diretorio = sys.argv[1]
else:
    diretorio = "./tb_tabs"
if not os.access(diretorio, os.F_OK):
    os.mkdir(diretorio)
while True:
    a = input()
    if a == "exit":
        break
    if a == ".":
        print("Invalid URL")
        continue
    a.strip()
    a = a.casefold()
    if a == "back" and len(lista) > 1:
        a = lista.pop()
        apagar_arquivo(a)
        a = lista.pop()
    elif a == "back" and len(lista) <= 1:
        continue
    if a.find(".") < 0:
        print("Invalid URL")
        continue

    if a.find("https://") >= 0 or a.find("http://") >= 0:
        html = requests.request("GET", a)
        a = a.replace("https://", "")
        a = a.replace("http://", "")
    else:
        html = requests.request("GET", "http://" + a)

    lista.append(a)
    soup = BeautifulSoup(html.text, "html.parser")

    variavel = ""
    # LOCALIZA AS TAGS COM LINKS
    for tag in soup.find_all("a"):
        if len(tag.get_text()) > 0:
            try:
                texto = str(tag.get_text()).encode('latin1').decode('utf-8')
            except:
                texto = tag.get_text()
            # AQUI ESTA O ERRO
            tag.string = "".join([Fore.BLUE, texto, Fore.RESET])
    # FAZ UMA LIMPEZA AINDA DE TAGS QUE NÃO ERAM PRA VIR - PODE DAR ERRO ALGUNS SITES
    for tag in soup.find_all("input"):
        tag.decompose()
    for tag in soup.find_all("form"):
        tag.decompose()

    teste = soup.find_all(
        ["p", "a", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5 ", "h6"]
    )
    for string in teste:
        variavel = variavel + string.get_text() + "\n"
    # variavel = variavel.strip()
    b = a.split(".")
    if b[0] == "www":
        del b[0]

    if not os.access(f"{diretorio}/{b[0]}", os.F_OK) and len(diretorio) > 1:
        with open(f"{diretorio}/{b[0]}", "w") as f:
            f.write(str(variavel))
            print((variavel))
    else:
        with open(f"{diretorio}/{b[0]}", "r") as f:
            variavel = str(f.read())
            print(variavel)

for i in range(len(lista)):
    a = lista.pop()
    apagar_arquivo(a)
