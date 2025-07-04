numero = input("Digite o número: ")
if len(numero) == 8:
    numero = '9' + numero
if len(numero) == 9 and numero[0] != '9':
    numero = '9' + numero
print(f"Número completo: {numero[:5]}-{numero[5:]}")
