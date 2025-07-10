import csv

# Funções auxiliares para gerência de arquivos
def carregar_usuarios(arquivo):
    usuarios = []
    try:
        with open(arquivo, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuarios.append(row)
    except FileNotFoundError:
        pass
    return usuarios

def salvar_usuarios(arquivo, usuarios):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'nome', 'senha', 'nivel_permissao']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)

def carregar_produtos(arquivo):
    produtos = []
    try:
        with open(arquivo, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                produtos.append(row)
    except FileNotFoundError:
        pass
    return produtos

def salvar_produtos(arquivo, produtos):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# CRUD para usuários
def criar_usuario(usuarios, id, nome, senha, nivel_permissao):
    novo_usuario = {'id': id, 'nome': nome, 'senha': senha, 'nivel_permissao': nivel_permissao}
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} criado com sucesso!")
    return usuarios

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Permissão: {usuario['nivel_permissao']}")

def atualizar_usuario(usuarios, id, novo_nome=None, nova_senha=None, novo_nivel_permissao=None):
    for usuario in usuarios:
        if usuario['id'] == id:
            if novo_nome:
                usuario['nome'] = novo_nome
            if nova_senha:
                usuario['senha'] = nova_senha
            if novo_nivel_permissao:
                usuario['nivel_permissao'] = novo_nivel_permissao
            print(f"Usuário {id} atualizado com sucesso!")
            return usuarios
    print(f"Usuário com ID {id} não encontrado.")
    return usuarios

def deletar_usuario(usuarios, id):
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    print(f"Usuário com ID {id} removido.")
    return usuarios

# CRUD para produtos
def criar_produto(produtos, id, nome, preco, quantidade):
    novo_produto = {'id': id, 'nome': nome, 'preco': float(preco), 'quantidade': int(quantidade)}
    produtos.append(novo_produto)
    print(f"Produto {nome} criado com sucesso!")
    return produtos

def listar_produtos(produtos):
    for produto in produtos:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")

def buscar_produto(produtos, id):
    for produto in produtos:
        if produto['id'] == id:
            print(f"Produto encontrado: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")
            return produto
    print(f"Produto com ID {id} não encontrado.")
    return None

def atualizar_produto(produtos, id, novo_nome=None, novo_preco=None, nova_quantidade=None):
    for produto in produtos:
        if produto['id'] == id:
            if novo_nome:
                produto['nome'] = novo_nome
            if novo_preco:
                produto['preco'] = float(novo_preco)
            if nova_quantidade:
                produto['quantidade'] = int(nova_quantidade)
            print(f"Produto {id} atualizado com sucesso!")
            return produtos
    print(f"Produto com ID {id} não encontrado.")
    return produtos

def deletar_produto(produtos, id):
    produtos = [produto for produto in produtos if produto['id'] != id]
    print(f"Produto com ID {id} removido.")
    return produtos

# Funções para ordenação
def ordenar_produtos_por_nome(produtos):
    return sorted(produtos, key=lambda produto: produto['nome'])

def ordenar_produtos_por_preco(produtos):
    return sorted(produtos, key=lambda produto: float(produto['preco']))

# Função de controle de acesso
def login(usuarios, nome, senha):
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print(f"Login bem-sucedido! Bem-vindo(a), {nome}.")
            return usuario['nivel_permissao']
    print("Usuário ou senha incorretos.")
    return None

# Exemplo de uso do sistema
if __name__ == "__main__":
    arquivo_usuarios = 'usuarios.csv'
    arquivo_produtos = 'produtos.csv'
    
    usuarios = carregar_usuarios(arquivo_usuarios)
    produtos = carregar_produtos(arquivo_produtos)
    
    # Simulação de criação e listagem de usuários
    usuarios = criar_usuario(usuarios, '1', 'admin', '123', 'gerente')
    usuarios = criar_usuario(usuarios, '2', 'funcionario1', 'abc', 'funcionario')
    
    listar_usuarios(usuarios)
    
    # Simulação de login
    nivel = login(usuarios, 'admin', '123')
    
    # Salvar os dados no arquivo
    salvar_usuarios(arquivo_usuarios, usuarios)
    salvar_produtos(arquivo_produtos, produtos)


Gerência de arquivos : Funções como `carregar_usuariose `salvar_usuasalvar_usuariosmanipulam arco
CRUD para usuários e produtos : Funções comocriar_usuario, `listar_listar_usuarios, `atuaatualizar_usuario, `deletar_usuario, e
Ordenação de produtos :
Controle de acesso : Fulogine.p.a.
