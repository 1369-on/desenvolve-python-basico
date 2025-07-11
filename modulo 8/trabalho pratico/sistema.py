import csv

ARQ_USUARIOS = 'usuarios.csv'
ARQ_SERVICOS = 'servicos.csv'

def carregar_usuarios():
    usuarios = []
    try:
        with open(ARQ_USUARIOS, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuarios.append(row)
    except FileNotFoundError:
        pass
    return usuarios

def salvar_usuarios(usuarios):
    with open(ARQ_USUARIOS, 'w', newline='', encoding='utf-8') as f:
        campos = ['id', 'nome', 'login', 'senha', 'tipo']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(usuarios)

def login(usuarios):
    login = input("Login: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u['login'] == login and u['senha'] == senha:
            return u
    return None

def menu(usu):
    if usu['tipo'] == 'gerente':
        return gerente_menu
    elif usu['tipo'] == 'funcionario':
        return funcionario_menu
    elif usu['tipo'] == 'cliente':
        return cliente_menu
    else:
        return lambda: print("Tipo de usuário desconhecido")

def listar_usuarios(usuarios):
    for u in usuarios:
        print(f"{u['id']} - {u['nome']} ({u['tipo']})")

def criar_usuario(usuarios):
    id = str(len(usuarios)+1)
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")
    tipo = input("Tipo (gerente/funcionario/cliente): ")
    usuarios.append({'id': id, 'nome': nome, 'login': login, 'senha': senha, 'tipo': tipo})

def atualizar_usuario(usuarios):
    id = input("ID do usuário a editar: ")
    for u in usuarios:
        if u['id'] == id:
            u['nome'] = input("Novo nome: ")
            u['senha'] = input("Nova senha: ")

def deletar_usuario(usuarios):
    id = input("ID do usuário a deletar: ")
    usuarios[:] = [u for u in usuarios if u['id'] != id]

def carregar_servicos():
    servicos = []
    try:
        with open(ARQ_SERVICOS, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                servicos.append(row)
    except FileNotFoundError:
        pass
    return servicos

def salvar_servicos(servicos):
    with open(ARQ_SERVICOS, 'w', newline='', encoding='utf-8') as f:
        campos = ['tipo', 'id', 'nome', 'preco', 'quantidade', 'descricao']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(servicos)

def listar_por_nome(servicos):
    for s in sorted(servicos, key=lambda x: x['nome']):
        print(s)

def listar_por_preco(servicos):
    for s in sorted(servicos, key=lambda x: float(x['preco'])):
        print(s)

def buscar_servico(servicos):
    termo = input("Buscar por nome: ").lower()
    for s in servicos:
        if termo in s['nome'].lower():
            print(s)

def criar_servico(servicos):
    tipo = input("Tipo (produto/servico): ")
    id = str(len(servicos)+1)
    nome = input("Nome: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade (vazio se serviço): ")
    descricao = input("Descrição (vazio se produto): ")
    servicos.append({'tipo': tipo, 'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade, 'descricao': descricao})

def atualizar_servico(servicos):
    id = input("ID do item: ")
    for s in servicos:
        if s['id'] == id:
            s['preco'] = input("Novo preço: ")
            if s['tipo'] == 'produto':
                s['quantidade'] = input("Nova quantidade: ")

def deletar_servico(servicos):
    id = input("ID a deletar: ")
    servicos[:] = [s for s in servicos if s['id'] != id]

def gerente_menu():
    while True:
        print("\n1. Usuários\n2. Produtos/Serviços\n0. Sair")
        op = input("Opção: ")
        if op == '1':
            usuarios = carregar_usuarios()
            print("a. Listar\nb. Criar\nc. Editar\nd. Deletar")
            sub = input("Opção: ")
            if sub == 'a': listar_usuarios(usuarios)
            elif sub == 'b': criar_usuario(usuarios)
            elif sub == 'c': atualizar_usuario(usuarios)
            elif sub == 'd': deletar_usuario(usuarios)
            salvar_usuarios(usuarios)
        elif op == '2':
            servicos = carregar_servicos()
            print("a. Listar por nome\nb. Listar por preço\nc. Buscar\nd. Criar\ne. Editar\nf. Deletar")
            sub = input("Opção: ")
            if sub == 'a': listar_por_nome(servicos)
            elif sub == 'b': listar_por_preco(servicos)
            elif sub == 'c': buscar_servico(servicos)
            elif sub == 'd': criar_servico(servicos)
            elif sub == 'e': atualizar_servico(servicos)
            elif sub == 'f': deletar_servico(servicos)
            salvar_servicos(servicos)
        elif op == '0':
            break

def funcionario_menu():
    while True:
        print("\n1. Produtos/Serviços\n0. Sair")
        op = input("Opção: ")
        servicos = carregar_servicos()
        if op == '1':
            print("a. Listar por nome\nb. Buscar\nc. Editar")
            sub = input("Opção: ")
            if sub == 'a': listar_por_nome(servicos)
            elif sub == 'b': buscar_servico(servicos)
            elif sub == 'c': atualizar_servico(servicos)
            salvar_servicos(servicos)
        elif op == '0':
            break

def cliente_menu():
    while True:
        print("\n1. Ver produtos/serviços\n0. Sair")
        op = input("Opção: ")
        servicos = carregar_servicos()
        if op == '1':
            listar_por_nome(servicos)
        elif op == '0':
            break

# Execução principal
usuarios = carregar_usuarios()
usuario = login(usuarios)
if usuario:
    print(f"Bem-vindo, {usuario['nome']} ({usuario['tipo']})")
    menu(usuario)()
else:
    print("Login ou senha inválidos.")
