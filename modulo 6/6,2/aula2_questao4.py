
qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input()) for _ in range(qtd1)]


qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input()) for _ in range(qtd2)]


lista_intercalada = []
for a, b in zip(lista1, lista2):
    lista_intercalada.append(a)
    lista_intercalada.append(b)

lista_intercalada.extend(lista1[len(lista2):])
lista_intercalada.extend(lista2[len(lista1):])


print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
