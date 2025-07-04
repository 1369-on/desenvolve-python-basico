
import random

def embaralhar_palavra(palavra):
    if len(palavra) > 3:
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    return palavra

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)


frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
