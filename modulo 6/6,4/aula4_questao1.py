# a) Todos os números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print(pares)

# b) Os quadrados de todos os valores da lista [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in range(1, 10)]
print(quadrados)

# c) Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print(divisiveis_por_7)

# d) "par" ou "ímpar" dependendo da paridade dos elementos em range(0,30,3)
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print(paridade)
