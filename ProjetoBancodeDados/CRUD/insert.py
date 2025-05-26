from database import connect
from datetime import datetime

# Inserir um novo usuário
from database import connect


def mostrar_feedback(tipo, id_inserido, nome_inserido):
    print(f"\n{tipo} inserido com sucesso!")
    print(f"ID do {tipo}: {id_inserido}")
    print(f"Detalhes do {tipo}: {nome_inserido}")

def verificar_id_usuario_existente(id_usuario):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Usuario WHERE id_usuario = ?", (id_usuario,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] > 0  # Retorna True se o ID já existe, False caso contrário

# Inserir um novo usuário com ID especificado
# Função para inserir um novo usuário
def insert_usuario():
    login = input("Digite o login do usuário: ")
    senha = input("Digite a senha do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    data_ingresso = input("Digite a data de ingresso (AAAA-MM-DD): ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Usuario (login, senha, data_ingresso, email)
        VALUES (?, ?, ?, ?)
    """, (login, senha, data_ingresso, email))

    conn.commit()
    conn.close()
    print(f"Usuário {login} inserido com sucesso!")

# Inserir um novo arquivo
def insert_arquivo(nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario):
    conn = connect()  # Conecta ao banco de dados
    cursor = conn.cursor()

    # Inserção do arquivo na tabela
    cursor.execute("""
        INSERT INTO Arquivo (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario))

    conn.commit()
    conn.close()

    print(f"Arquivo '{nome}' inserido com sucesso!")

def insert_arquivo(nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario, id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    
    # Inserção de arquivo no banco de dados
    cursor.execute("""
        INSERT INTO Arquivo (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    # Chama o feedback para mostrar os detalhes e o ID
    mostrar_feedback("Arquivo", id_arquivo, nome)

# Registrar operação no histórico
def registrar_operacao(id_arquivo, id_usuario, operacao):
    conn = connect()
    cursor = conn.cursor()
    data = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H:%M:%S')
    cursor.execute("""
        INSERT INTO Historico (id_arquivo, id_usuario, operacao, data, hora)
        VALUES (?, ?, ?, ?, ?)
    """, (id_arquivo, id_usuario, operacao, data, hora))
    conn.commit()
    cursor.close()
    conn.close()
# Função para inserir um novo compartilhamento
def insert_compartilhamento(id_arquivo, id_dono, id_compartilhado):
    conn = connect()
    cursor = conn.cursor()
    data_compartilhamento = datetime.now().strftime('%Y-%m-%d')  # Data atual
    cursor.execute("""
        INSERT INTO Compartilhamento (id_arquivo, id_dono, id_compartilhado, data_compartilhamento)
        VALUES (?, ?, ?, ?)
    """, (id_arquivo, id_dono, id_compartilhado, data_compartilhamento))
    conn.commit()
    cursor.close()
    conn.close()

# Função para inserir um novo comentário
def insert_comentario(id_arquivo, id_usuario, conteudo):
    conn = connect()
    cursor = conn.cursor()
    data = datetime.now().strftime('%Y-%m-%d')  # Data atual
    hora = datetime.now().strftime('%H:%M:%S')  # Hora atual
    cursor.execute("""
        INSERT INTO Comentario (conteudo, data, hora, id_usuario, id_arquivo)
        VALUES (?, ?, ?, ?, ?)
    """, (conteudo, data, hora, id_usuario, id_arquivo))


# Função para inserir um novo administrador
def insert_administrador(id_usuario):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Administrador (id_usuario)
        VALUES (?)
    """, (id_usuario,))
    conn.commit()
    cursor.close()
    conn.close()

# Função para inserir um novo suporte
def insert_suporte(id_usuario, id_arquivo, descricao):
    conn = connect()
    cursor = conn.cursor()
    data = datetime.now().strftime('%Y-%m-%d')  # Data atual
    hora = datetime.now().strftime('%H:%M:%S')  # Hora atual
    cursor.execute("""
        INSERT INTO Suporte (id_usuario, id_arquivo, data, hora, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (id_usuario, id_arquivo, data, hora, descricao))
    conn.commit()
    cursor.close()
    conn.close()

# Função para verificar se o ID do arquivo já existe
def check_id_arquivo(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Arquivo WHERE id_arquivo = ?", (id_arquivo,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] > 0  # Retorna True se o ID já existir


    conn.commit()
    cursor.close()
    conn.close()

    # Função para inserir um novo histórico de alteração de arquivo
def insert_historico(id_arquivo, id_usuario_alteracao, operacao, conteudo_mudado):
    conn = connect()
    cursor = conn.cursor()
    
    # Pega a data e a hora atuais
    data = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H:%M:%S')

    # Insere o histórico de versão do arquivo
    cursor.execute("""
        INSERT INTO Historico (id_arquivo, id_usuario_alteracao, data, hora, operacao, conteudo_mudado)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (id_arquivo, id_usuario_alteracao, data, hora, operacao, conteudo_mudado))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Histórico registrado com sucesso!")

    # Função para inserir uma nova instituição
# Função para inserir uma nova instituição
def insert_instituicao(nome, causa_social, endereco):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Instituicao (nome, causa_social, endereco)
        VALUES (?, ?, ?)
    """, (nome, causa_social, endereco))
    
    conn.commit()
    conn.close()
    print(f"Instituição '{nome}' inserida com sucesso!")


# Função para inserir um novo plano
def associar_instituicao_plano():
    id_instituicao = int(input("Informe o ID da Instituição: "))
    id_plano = int(input("Informe o ID do Plano: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Instituicao_Plano (id_instituicao, id_plano)
        VALUES (?, ?)
    """, (id_instituicao, id_plano))

    conn.commit()
    conn.close()
    print(f"Instituição de ID {id_instituicao} associada ao Plano de ID {id_plano} com sucesso!")


# Função para associar um usuário a uma instituição
def associate_usuario_instituicao(id_usuario, id_instituicao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Usuario_Instituicao (id_usuario, id_instituicao)
        VALUES (?, ?)
    """, (id_usuario, id_instituicao))
    conn.commit()
    cursor.close()
    conn.close()

# Função para associar uma instituição a um plano
# Função para associar uma instituição a um plano
def associate_instituicao_plano(id_instituicao, id_plano):
    conn = connect()
    cursor = conn.cursor()
    
    # Insere a associação na tabela Instituicao_Plano
    cursor.execute("""
        INSERT INTO Instituicao_Plano (id_instituicao, id_plano)
        VALUES (?, ?)
    """, (id_instituicao, id_plano))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Instituição {id_instituicao} agora está associada ao plano {id_plano}.")

def insert_plano(nome, duracao, espaco_usuario, data_aquisicao):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Plano (nome, duracao, espaco_usuario, data_aquisicao)
        VALUES (?, ?, ?, ?)
    """, (nome, duracao, espaco_usuario, data_aquisicao))

    conn.commit()
    conn.close()
    print(f"Plano '{nome}' inserido com sucesso!")



def insert_admin_and_user():
    # Inserir um usuário comum
    insert_usuario(1, "admin", "admin123", "2025-05-01", "admin@example.com")
    
    # Tornar o usuário com ID 1 um administrador
    insert_administrador(1)

    # Inserir um usuário comum
    insert_usuario(2, "usuario", "senha123", "2025-05-01", "usuario@example.com")
