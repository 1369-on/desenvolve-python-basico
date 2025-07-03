
import random


valores = [random.randint(-100, 100) for _ in range(20)]


valores_ordenados = sorted(valores)

indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))


print("Lista ordenada:", valores_ordenados)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
