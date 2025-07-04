from collections import Counter

frase = input("Digite uma frase: ").split()
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = [palavra for palavra in frase if Counter(palavra.lower()) == Counter(palavra_objetivo.lower())]
print(f"Anagramas: {anagramas}")
