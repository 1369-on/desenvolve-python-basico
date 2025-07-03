
import random

valores = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", valores)

maior_qtd_negativos = 0
indice_maior_intervalo = 0
for i in range(len(valores) - 4):
    intervalo = valores[i:i+5]
    qtd_negativos = len([x for x in intervalo if x < 0])
    
    if qtd_negativos > maior_qtd_negativos:
        maior_qtd_negativos = qtd_negativos
        indice_maior_intervalo = i

del valores[indice_maior_intervalo:indice_maior_intervalo + 5]

print("Lista editada:", valores)
