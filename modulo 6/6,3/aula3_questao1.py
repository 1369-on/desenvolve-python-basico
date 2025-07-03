
valores = []
while len(valores) < 4:
    num = int(input("Digite um número inteiro (pelo menos 4 valores): "))
    valores.append(num)

print("Lista original:", valores)

print("3 primeiros elementos:", valores[:3])

print("2 últimos elementos:", valores[-2:])

print("Lista invertida:", valores[::-1])

print("Elementos de índice par:", valores[::2])

print("Elementos de índice ímpar:", valores[1::2])
