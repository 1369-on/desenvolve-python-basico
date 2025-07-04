
import re

with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo)

with open("palavras.txt", "w") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

with open("palavras.txt", "r") as arquivo_palavras:
    print(arquivo_palavras.read())
