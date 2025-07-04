
import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search("[a-z]", senha):
        return False
    if not re.search("[A-Z]", senha):
        return False
    if not re.search("[0-9]", senha):
        return False
    if not re.search("[@#$]", senha):
        return False
    return True


senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
