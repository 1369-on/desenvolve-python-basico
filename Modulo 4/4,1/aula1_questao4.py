
n = int(input("Digite quantos números deseja comparar: "))

maior = 0

while n > 0:
   
    x = int(input("Digite um número: "))
    
    if x > maior:
        maior = x  # Atualiza 'maior' com o novo maior número
    
    n -= 1

print("Maior número:", maior)
