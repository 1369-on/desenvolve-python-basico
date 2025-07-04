frase = input("Digite uma frase: ")
vogais = [i for i, letra in enumerate(frase) if letra.lower() in "aeiou"]
print(f"{len(vogais)} vogais")
print(f"Índices {vogais}")
