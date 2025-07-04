

def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ''.join(['*' if letra in vogais else letra for letra in frase])
    return frase_modificada

frase = input("Digite uma frase: ")
print("Frase modificada:", substituir_vogais(frase))
