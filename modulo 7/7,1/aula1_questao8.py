def calcula_digito(cpf, multiplicador_inicial):
    soma = sum(int(cpf[i]) * (multiplicador_inicial - i) for i in range(len(cpf)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

cpf_input = input("Digite o CPF (XXX.XXX.XXX-XX): ").replace('.', '').replace('-', '')
cpf_numeros = cpf_input[:9]

digito1 = calcula_digito(cpf_numeros, 10)
digito2 = calcula_digito(cpf_numeros + str(digito1), 11)

cpf_gerado = cpf_numeros + str(digito1) + str(digito2)
if cpf_input == cpf_gerado:
    print("Válido")
else:
    print("Inválido")
