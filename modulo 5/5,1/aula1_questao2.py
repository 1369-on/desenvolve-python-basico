
import random
import math

n = int(input("Digite o valor de n: "))
soma = sum(random.randint(0, 100) for _ in range(n))
raiz_quadrada = math.sqrt(soma)

print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada:.2f}")
