
frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
print("Vogais:", vogais)

consoantes = [letra for letra in frase if letra.lower() not in 'aeiou' and letra.isalpha()]
print("Consoantes:", consoantes)
