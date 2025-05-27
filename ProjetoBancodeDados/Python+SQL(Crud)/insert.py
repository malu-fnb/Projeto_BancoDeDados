from database import connect
from datetime import datetime


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
    return resultado[0] > 0  


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


def insert_arquivo(nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Arquivo (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario))

    conn.commit()
    conn.close()


    print(f"Arquivo '{nome}' inserido com sucesso!")



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

def insert_compartilhamento(id_arquivo, id_dono, id_compartilhado):
    conn = connect()
    cursor = conn.cursor()
    data_compartilhamento = datetime.now().strftime('%Y-%m-%d')  
    cursor.execute("""
        INSERT INTO Compartilhamento (id_arquivo, id_dono, id_compartilhado, data_compartilhamento)
        VALUES (?, ?, ?, ?)
    """, (id_arquivo, id_dono, id_compartilhado, data_compartilhamento))
    conn.commit()
    cursor.close()
    conn.close()

def insert_comentario(id_arquivo, id_usuario, conteudo):
    conn = connect()
    cursor = conn.cursor()
    data = datetime.now().strftime('%Y-%m-%d')  
    hora = datetime.now().strftime('%H:%M:%S')  
    cursor.execute("""
        INSERT INTO Comentario (conteudo, data, hora, id_usuario, id_arquivo)
        VALUES (?, ?, ?, ?, ?)
    """, (conteudo, data, hora, id_usuario, id_arquivo))


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

def insert_suporte(id_usuario, id_arquivo, descricao):
    conn = connect()
    cursor = conn.cursor()
    data = datetime.now().strftime('%Y-%m-%d')  
    hora = datetime.now().strftime('%H:%M:%S')  
    cursor.execute("""
        INSERT INTO Suporte (id_usuario, id_arquivo, data, hora, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (id_usuario, id_arquivo, data, hora, descricao))
    conn.commit()
    cursor.close()
    conn.close()

def check_id_arquivo(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Arquivo WHERE id_arquivo = ?", (id_arquivo,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] > 0  


    conn.commit()
    cursor.close()
    conn.close()

def insert_historico(id_arquivo, id_usuario_alteracao, operacao, conteudo_mudado):
    conn = connect()
    cursor = conn.cursor()
    
    data = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H:%M:%S')

    cursor.execute("""
        INSERT INTO Historico (id_arquivo, id_usuario_alteracao, data, hora, operacao, conteudo_mudado)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (id_arquivo, id_usuario_alteracao, data, hora, operacao, conteudo_mudado))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Histórico registrado com sucesso!")


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


def associate_instituicao_plano(id_instituicao, id_plano):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM Instituicao_Plano WHERE id_instituicao = ? AND id_plano = ?
    """, (id_instituicao, id_plano))
    resultado = cursor.fetchone()
    
    if resultado[0] > 0:
        print("Esta associação já existe!")
    else:
        cursor.execute("""
            INSERT INTO Instituicao_Plano (id_instituicao, id_plano)
            VALUES (?, ?)
        """, (id_instituicao, id_plano))
        conn.commit()
        print(f"Instituição de ID {id_instituicao} associada ao Plano de ID {id_plano} com sucesso!")

    conn.close()


def associate_instituicao_plano(id_instituicao, id_plano):
    conn = connect()
    cursor = conn.cursor()
    
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



#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

def insert_admin_and_user():

    insert_usuario(1, "admin", "admin123", "2025-05-01", "admin@example.com")
  
    insert_administrador(1)

   
    insert_usuario(2, "usuario", "senha123", "2025-05-01", "usuario@example.com")

def inserir_instituicao():
    nome = input("Digite o nome da instituição: ")
    causa_social = input("Digite a causa social da instituição: ")
    endereco = input("Digite o endereço da instituição: ")

    conn = connect() 
    cursor = conn.cursor()


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
    
    cursor.execute("""
        INSERT INTO Instituicao (nome, causa_social, endereco)
        VALUES (?, ?, ?)
    """, (nome, causa_social, endereco))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Instituição '{nome}' inserida com sucesso!")

def associar_instituicao_plano():
    id_instituicao = int(input("Informe o ID da Instituição: "))
    id_plano = int(input("Informe o ID do Plano: "))

    conn = connect()  
    cursor = conn.cursor()


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

    cursor.execute("""
        SELECT COUNT(*) FROM Instituicao_Plano
        WHERE id_instituicao = ? AND id_plano = ?
    """, (id_instituicao, id_plano))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        print("Essa associação já existe!")
    else:

        cursor.execute("""
            INSERT INTO Instituicao_Plano (id_instituicao, id_plano)
            VALUES (?, ?)
        """, (id_instituicao, id_plano))
        conn.commit()
        print(f"Instituição de ID {id_instituicao} associada ao Plano de ID {id_plano} com sucesso!")

    cursor.close()
    conn.close()


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
def inserir_instituicoes():
    instituicoes = [
        ("Universidade Federal de Pernambuco", "Educação superior", "Av. Prof. Moraes Rego, s/n - Cidade Universitária, Recife - PE"),
        ("Universidade de Pernambuco", "Educação superior", "Av. Agamenon Magalhães, 5500 - Santo Amaro, Recife - PE"),
        ("Faculdade dos Guararapes", "Educação superior", "Rua Domingos Ferreira, 118 - Pina, Recife - PE"),
        ("Instituto Federal de Pernambuco", "Educação técnica e superior", "Av. Recife, s/n - Iputinga, Recife - PE")
    ]

    conn = connect()
    cursor = conn.cursor()

    for instituicao in instituicoes:
        cursor.execute("""
            INSERT INTO Instituicao (nome, causa_social, endereco)
            VALUES (?, ?, ?)
        """, instituicao)

    conn.commit()
    conn.close()
    print("Instituições inseridas com sucesso!")


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
def inserir_planos():
    planos = [
        ("Plano Básico", 12, 100, "2025-01-01"),  
        ("Plano Intermediário", 24, 250, "2025-01-01"), 
        ("Plano Avançado", 36, 500, "2025-01-01")  
    ]

    conn = connect()
    cursor = conn.cursor()

    for plano in planos:
        cursor.execute("""
            INSERT INTO Plano (nome, duracao, espaco_usuario, data_aquisicao)
            VALUES (?, ?, ?, ?)
        """, plano)

    conn.commit()
    conn.close()
    print("Planos inseridos com sucesso!")

from datetime import datetime

def insert_compartilhamento(id_arquivo, id_dono, id_compartilhado):
    conn = connect()
    cursor = conn.cursor()
    

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

    data_compartilhamento = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute("""
        INSERT INTO Compartilhamento (id_arquivo, id_dono, id_compartilhado, data_compartilhamento)
        VALUES (?, ?, ?, ?)
    """, (id_arquivo, id_dono, id_compartilhado, data_compartilhamento))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"Arquivo {id_arquivo} compartilhado com sucesso para o usuário {id_compartilhado}.")


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

    print(f"Usuário com ID {id_usuario} foi promovido a administrador com sucesso!")



#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
from database import connect
from datetime import datetime

def insert_comentario(id_usuario, id_arquivo, conteudo):
    with connect() as conn:
        cursor = conn.cursor()

        data = datetime.now().strftime('%Y-%m-%d')  
        hora = datetime.now().strftime('%H:%M:%S')  

        cursor.execute("""
            INSERT INTO Comentario (conteudo, data, hora, id_usuario, id_arquivo)
            VALUES (?, ?, ?, ?, ?)
        """, (conteudo, data, hora, id_usuario, id_arquivo))

        conn.commit()

    print(f"Comentário inserido com sucesso para o arquivo {id_arquivo}!")



#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

    def visualizar_comentarios(id_arquivo):
            conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT C.conteudo, C.data, C.hora, U.login 
        FROM Comentario C
        JOIN Usuario U ON C.id_usuario = U.id_usuario
        WHERE C.id_arquivo = ?
    """, (id_arquivo,))
    
    comentarios = cursor.fetchall()
    
    if comentarios:
        print("\nComentários sobre este arquivo:")
        for comentario in comentarios:
            print(f"Comentário: {comentario[0]}")
            print(f"Data: {comentario[1]} | Hora: {comentario[2]}")
            print(f"Feito por: {comentario[3]}")
            print("-" * 30)  
    else:
        print("Nenhum comentário encontrado para este arquivo.")
    
    conn.close()

    




    

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR