import random

def encrypt(nomes):
    n = random.randint(1, 10)
    criptografados = [''.join(chr((ord(c) + n - 33) % 94 + 33) for c in nome) for nome in nomes]
    return criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)
print(f"Chave: {chave}")
print(f"Nomes criptografados: {nomes_cript}")
