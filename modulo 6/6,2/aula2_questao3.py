
import random
from collections import Counter


lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]


interseccao = list(set(lista1) & set(lista2))
interseccao.sort()


contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)


print("Lista1:", lista1)
print("Lista2:", lista2)
print("Interseccao:", interseccao)
print("Contagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={contagem_lista1[valor]}, lista2={contagem_lista2[valor]})")
