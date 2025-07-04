
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print("Primeiras 25 linhas:")
print("".join(linhas[:25]))

num_linhas = len(linhas)
print(f"\nNúmero de linhas: {num_linhas}")

linha_maior = max(linhas, key=len)
print(f"Linha com maior número de caracteres:\n{linha_maior}")

contagem_nonato = sum(1 for linha in linhas if "nonato" in linha.lower())
contagem_iria = sum(1 for linha in linhas if "íria" in linha.lower())
print(f"\nMenções a 'Nonato': {contagem_nonato}")
print(f"Menções a 'Íria': {contagem_iria}")
