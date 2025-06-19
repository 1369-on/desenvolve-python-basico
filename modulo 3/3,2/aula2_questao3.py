
idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False) ").lower() == "true"
vitorias = int(input("Quantos jogos já venceu? "))

apto = 16 <= idade <= 18 and jogou_3_jogos and vitorias >= 1

print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
