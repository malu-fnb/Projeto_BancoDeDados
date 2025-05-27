from database import connect
from insert import insert_usuario,insert_comentario, insert_compartilhamento, insert_arquivo, insert_administrador, insert_compartilhamento, insert_comentario, insert_suporte, insert_historico, insert_instituicao, insert_plano, associate_instituicao_plano, inserir_instituicao, associar_instituicao_plano, inserir_instituicoes, inserir_planos, insert_administrador
from select import get_usuario, get_arquivo, get_compartilhamentos, get_comentarios, get_historico_arquivo, get_arquivos_usuario, verificar_id_usuario_existente
from update import update_usuario, update_arquivo
from delete import delete_usuario, delete_arquivo
from models import create_tables
from datetime import datetime

def mostrar_menu():
    print("\nMenu:")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")


def login():
    print("\n----- Sistema de Login -----")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")
    tipo_usuario = input("Você é um(a): \n1. Administrador\n2. Usuário\nEscolha (1-2): ")
    print("PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR")


    senha = input("Digite sua senha: ")

    conn = connect()
    cursor = conn.cursor()


    if tipo_usuario == "1" and senha == "admin123":
        print("Bem-vindo, Administrador!")
        conn.close()
        return 'admin', None 


    elif tipo_usuario == "2":
        cursor.execute(""" 
            SELECT id_usuario FROM Usuario WHERE senha = ?
        """, (senha,))
        user = cursor.fetchone()
        if user:
            id_usuario = user[0] 
            print("Bem-vindo, Usuário!")
            conn.close()
            return 'user', id_usuario 
        else:
            print("Senha incorreta.")
            conn.close()
            return None, None 

    else:
        print("Opção inválida!")
        conn.close()
        return None, None  

def main():
    while True:
        usuario_tipo, id_usuario = login() 

        if usuario_tipo == 'admin':
            menu_admin()  
        elif usuario_tipo == 'user' and id_usuario:  
            menu_usuario(id_usuario)  
        else:
            print("Tentando novamente...")





def menu_admin():
    print("\n----- Menu Administrador -----")
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Arquivos")
    print("3. Gerenciar Instituições e Planos")
    print("4. Visualizar Suporte")
    print("5. Adicionar Outro Administrador")
    print("6. Listar Usuários")
    print("7. Listar Administradores")


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
    print("8. Sair")
    
    escolha = input("Escolha uma opção (1-8): ")

    if escolha == "1":
        menu_gerenciar_usuarios() 
    elif escolha == "2":
        menu_arquivo_admin()
    elif escolha == "3":
        menu_instituicao_plano()
    elif escolha == "4":
        menu_suporte_admin()
    elif escolha == "5":
        adicionar_admin()  
    elif escolha == "6":
        listar_usuarios()  
    elif escolha == "7":
        listar_administradores()  
    elif escolha == "8":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida.")
        menu_admin()



#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
def adicionar_admin():
   
    id_usuario = int(input("Informe o ID do usuário que você deseja promover a administrador: "))

    if verificar_id_usuario_existente(id_usuario):
        insert_administrador(id_usuario)  
        print(f"Usuário com ID {id_usuario} agora é um administrador.")
    else:
        print("ID de usuário não encontrado. Tente novamente.")


def menu_gerenciar_usuarios():
    print("\n----- Gerenciamento de Usuários -----")
    print("1. Inserir Novo Usuário")
    print("2. Buscar Usuário")
    print("3. Atualizar Usuário")
    print("4. Remover Usuário")
    print("5. Voltar ao Menu Administrador")
    
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        insert_usuario() 
    elif escolha == "2":
        buscar_usuario()  
    elif escolha == "3":
        atualizar_usuario()  
    elif escolha == "4":
        remover_usuario()  
    elif escolha == "5":
        menu_admin()  
    else:
        print("Opção inválida.")
        menu_gerenciar_usuarios()  


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

def menu_usuario(id_usuario):
    while True:
        print("\n----- Menu Usuário -----")
        print("1. Gerenciar Arquivos")
        print("2. Visualizar Histórico de Operações")
        print("3. Solicitar Suporte")
        print("4. Visualizar Arquivos Compartilhados")
        print("5. Compartilhar Arquivo")
        print("6. Comentar Arquivo")  
        print("7. Inserir Arquivo")  
        print("8. Sair")
        
        escolha = input("Escolha uma opção (1-8): ")

        if escolha == "1":
            menu_arquivo_user(id_usuario)
        elif escolha == "2":
            menu_historico(id_usuario)
        elif escolha == "3":
            menu_suporte_user(id_usuario)
        elif escolha == "4":
            visualizar_compartilhamentos(id_usuario)
        elif escolha == "5":
            compartilhar_arquivo(id_usuario)
        elif escolha == "6":
            comentar_arquivo(id_usuario) 
        elif escolha == "7":
            inserir_arquivo_usuario(id_usuario) 
        elif escolha == "8":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida.")


#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

def inserir_arquivo_usuario(id_usuario):
    print("\n----- Inserir Arquivo -----")
    nome = input("Nome do Arquivo: ")
    tipo = input("Tipo do Arquivo: ")


    print("\nEscolha a permissão de acesso para o arquivo:")
    print("1. Público - O arquivo pode ser acessado por qualquer usuário.")
    print("2. Privado - O arquivo só pode ser acessado pelo dono do arquivo.")
    print("3. Restrito - O arquivo pode ser acessado por um grupo específico de usuários.")

    permissao_opcao = input("Escolha uma opção (1-3): ")
    
    if permissao_opcao == "1":
        permissao_de_acesso = "público"
    elif permissao_opcao == "2":
        permissao_de_acesso = "privado"
    elif permissao_opcao == "3":
        permissao_de_acesso = "restrito"
    else:
        print("Opção inválida. A permissão será definida como 'privado' por padrão.")
        permissao_de_acesso = "privado"

    tamanho = float(input("Tamanho do Arquivo (MB): "))
    URL = input("URL do Arquivo: ")
    data_mode = input("Data de Última Modificação (AAAA-MM-DD): ")
    localizacao = input("Localização do Arquivo: ")



#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
    insert_arquivo(nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario)
    print(f"Arquivo '{nome}' inserido com sucesso!")
    menu_usuario(id_usuario)  


def menu_arquivo_user(id_usuario):
    print("\n----- Menu Arquivos (Usuário) -----")
    print("1. Carregar Arquivo")
    print("2. Atualizar Arquivo")
    print("3. Remover Arquivo")
    print("4. Voltar")
    
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        carregar_arquivo_user(id_usuario)
    elif escolha == "2":
        atualizar_arquivo_user(id_usuario)
    elif escolha == "3":
        remover_arquivo_user(id_usuario)
    elif escolha == "4":
        menu_usuario(id_usuario)
    else:
        print("Opção inválida.")
        menu_arquivo_user(id_usuario)


def menu_arquivo_user(id_usuario):
    print("\n----- Menu Arquivos (Usuário) -----")
    print("1. Ver Arquivos Acessíveis")
    print("2. Atualizar Arquivo")
    print("3. Voltar")
    
    escolha = input("Escolha uma opção (1-3): ")

    if escolha == "1":
        arquivos = get_arquivos_usuario(id_usuario)  
        if arquivos:
            print("\nArquivos Acessíveis:")
            for arquivo in arquivos:
                print(f"ID: {arquivo[0]}, Nome: {arquivo[1]}")  
        else:
            print("Você não tem acesso a nenhum arquivo.")
        
        menu_arquivo_user(id_usuario)  
    elif escolha == "2":
        id_arquivo = int(input("Informe o ID do arquivo que deseja atualizar: "))
        atualizar_arquivo_user(id_arquivo, id_usuario)
    elif escolha == "3":
        menu_usuario(id_usuario) 
    else:
        print("Opção inválida.")
        menu_arquivo_user(id_usuario) 

from select import get_arquivos_usuario, get_historico_arquivo

def menu_historico(id_usuario):
    print("\nHistórico de Operações")

    arquivos = get_arquivos_usuario(id_usuario)

    if arquivos:
        print("Selecione um arquivo para visualizar o histórico:")
        for arquivo in arquivos:
            print(f"ID: {arquivo[0]}, Nome: {arquivo[1]}")

        id_arquivo = int(input("\nInforme o ID do arquivo para visualizar o histórico: "))
        
        historico = get_historico_arquivo(id_arquivo)
        
        if historico:
            for registro in historico:
                print(f"ID Histórico: {registro[0]}")
                print(f"Operação: {registro[3]}")
                print(f"Data: {registro[4]}")
                print(f"Hora: {registro[5]}")
                print(f"Conteúdo Alterado: {registro[6]}")
                print("-" * 30)  
        else:
            print("Nenhum histórico encontrado para este arquivo.")
    else:
        print("Você não tem acesso a nenhum arquivo.")

    menu_usuario(id_usuario) 


def menu_suporte_user(id_usuario):
    print("\n----- Suporte (Usuário) -----")
    print("1. Solicitar Suporte para Arquivo")
    print("2. Voltar")
    
    escolha = input("Escolha uma opção (1-2): ")

    if escolha == "1":
        solicitar_suporte(id_usuario)  
    elif escolha == "2":
        menu_usuario(id_usuario)
    else:
        print("Opção inválida.")


def menu_instituicao_plano():
    print("\n----- Menu Instituições e Planos -----")
    print("1. Inserir Instituição")
    print("2. Associar Instituição a um Plano")
    print("3. Visualizar Instituições e Planos")  
    print("4. Voltar ao Menu Administrador")
    
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        insert_instituicao()  
    elif escolha == "2":
        associar_instituicao_plano()  
    elif escolha == "3":
        visualizar_instituicoes_e_planos()  
    elif escolha == "4":
        menu_admin()  
    else:
        print("Opção inválida.")
        menu_instituicao_plano()


def menu_suporte_admin():
    print("\n----- Suporte (Administrador) -----")
    print("1. Visualizar Suporte")
    print("2. Voltar")
    
    escolha = input("Escolha uma opção (1-2): ")

    if escolha == "1":
        visualizar_suporte()
    elif escolha == "2":
        menu_admin()
    else:
        print("Opção inválida.")

        def menu_historico():
             print("\nHistórico de Operações")
    id_arquivo = int(input("Informe o ID do arquivo para visualizar o histórico: "))
    
 
    historico = get_historico_arquivo(id_arquivo)
    
    if historico:
        for registro in historico:
            print(f"ID Histórico: {registro[0]}")
            print(f"Operação: {registro[2]}")
            print(f"Data: {registro[3]}")
            print(f"Hora: {registro[4]}")
            print(f"Conteúdo Alterado: {registro[5]}")
            print("-" * 30)  
    else:
        print("Nenhum histórico encontrado para este arquivo.")


def insert_arquivo_admin():
    nome = input("Nome do Arquivo: ")
    tipo = input("Tipo do Arquivo: ")

    print("\nEscolha a permissão de acesso para o arquivo:")
    print("1. Público - O arquivo pode ser acessado por qualquer usuário.")
    print("2. Privado - O arquivo só pode ser acessado pelo dono do arquivo.")
    print("3. Restrito - O arquivo pode ser acessado por um grupo específico de usuários.")

    permissao_opcao = input("Escolha uma opção (1-3): ")

    if permissao_opcao == "1":
        permissao_de_acesso = "público"
    elif permissao_opcao == "2":
        permissao_de_acesso = "privado"
    elif permissao_opcao == "3":
        permissao_de_acesso = "restrito"
    else:
        print("Opção inválida. A permissão será definida como 'privado' por padrão.")
        permissao_de_acesso = "privado"

    tamanho = float(input("Tamanho do Arquivo (MB): "))
    URL = input("URL: ")
    data_mode = input("Data de Última Modificação (AAAA-MM-DD): ")
    localizacao = input("Localização: ")
    id_usuario = int(input("ID do Usuário (Dono do Arquivo): "))

    insert_arquivo(nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario)
    print(f"Arquivo '{nome}' inserido com sucesso!")


def buscar_arquivo_admin():
    id_arquivo = int(input("Informe o ID do Arquivo para buscar: "))
    
    arquivo = get_arquivo(id_arquivo, None)  
    
    if arquivo:
        print(f"Arquivo encontrado: {arquivo}")
    else:
        print("Arquivo não encontrado.")

def atualizar_arquivo_admin():
    id_arquivo = int(input("Informe o ID do Arquivo para atualizar: "))
    
    nome = input("Novo Nome do Arquivo: ")
    tipo = input("Novo Tipo do Arquivo: ")
    
    print("\nEscolha a nova permissão de acesso para o arquivo:")
    print("1. Público - O arquivo pode ser acessado por qualquer usuário.")
    print("2. Privado - O arquivo só pode ser acessado pelo dono do arquivo.")
    print("3. Restrito - O arquivo pode ser acessado por um grupo específico de usuários.")
    
    permissao_opcao = input("Escolha uma opção (1-3): ")
    
    if permissao_opcao == "1":
        permissao_de_acesso = "público"
    elif permissao_opcao == "2":
        permissao_de_acesso = "privado"
    elif permissao_opcao == "3":
        permissao_de_acesso = "restrito"
    else:
        print("Opção inválida. A permissão será definida como 'privado' por padrão.")
        permissao_de_acesso = "privado"
    
    tamanho = float(input("Novo Tamanho do Arquivo (MB): "))
    URL = input("Nova URL: ")
    data_mode = input("Nova Data de Última Modificação (AAAA-MM-DD): ")
    localizacao = input("Nova Localização: ")
    
    update_arquivo(id_arquivo, nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao)
    print(f"Arquivo {id_arquivo} atualizado com sucesso!")

def remover_arquivo_admin():
    id_arquivo = int(input("Informe o ID do Arquivo para remover: "))
    
    delete_arquivo(id_arquivo)
    print(f"Arquivo {id_arquivo} removido com sucesso!")

def buscar_arquivo_user(id_usuario):
    id_arquivo = int(input("Informe o ID do Arquivo para buscar: "))
    
    arquivo = get_arquivo(id_arquivo, id_usuario)  
    
    if arquivo:
        print(f"Arquivo encontrado: {arquivo}")
    else:
        print("Você não tem acesso a este arquivo.")

def atualizar_arquivo_user(id_usuario): 
    id_arquivo = int(input("Informe o ID do Arquivo para atualizar: "))
    
    arquivo = get_arquivo(id_arquivo, id_usuario)
    
    if arquivo:
        nome = input("Novo Nome do Arquivo: ")
        tipo = input("Novo Tipo do Arquivo: ")
        
        print("\nEscolha a nova permissão de acesso para o arquivo:")
        print("1. Público - O arquivo pode ser acessado por qualquer usuário.")
        print("2. Privado - O arquivo só pode ser acessado pelo dono do arquivo.")
        print("3. Restrito - O arquivo pode ser acessado por um grupo específico de usuários.")
        
        permissao_opcao = input("Escolha uma opção (1-3): ")
        
        if permissao_opcao == "1":
            permissao_de_acesso = "público"
        elif permissao_opcao == "2":
            permissao_de_acesso = "privado"
        elif permissao_opcao == "3":
            permissao_de_acesso = "restrito"
        else:
            print("Opção inválida. A permissão será definida como 'privado' por padrão.")
            permissao_de_acesso = "privado"
        
        tamanho = float(input("Novo Tamanho do Arquivo (MB): "))
        URL = input("Nova URL: ")
        data_mode = input("Nova Data de Última Modificação (AAAA-MM-DD): ")
        localizacao = input("Nova Localização: ")
        
        update_arquivo(id_arquivo, nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao)
        print(f"Arquivo {id_arquivo} atualizado com sucesso!")
    else:
        print("Você não tem permissão para atualizar este arquivo.")

def solicitar_suporte(id_usuario):
    id_arquivo = int(input("Informe o ID do Arquivo para solicitar suporte: "))
    descricao = input("Descrição do Suporte: ")
    
    insert_suporte(id_usuario, id_arquivo, descricao)
    print(f"Suporte solicitado para o Arquivo {id_arquivo}.")

def atualizar_usuario():
    id_usuario = int(input("Informe o ID do Usuário para atualizar: "))
    
    login = input("Novo Login do Usuário: ")
    senha = input("Nova Senha do Usuário: ")
    email = input("Novo E-mail do Usuário: ")
    data_ingresso = input("Nova Data de Ingresso (AAAA-MM-DD): ")
    
    update_usuario(id_usuario, login, senha, data_ingresso, email)
    print(f"Usuário {id_usuario} atualizado com sucesso!")


def remover_usuario():
    id_usuario = int(input("Informe o ID do Usuário para remover: "))
    
   
    delete_usuario(id_usuario)
    print(f"Usuário {id_usuario} removido com sucesso!")


def visualizar_suporte():
    print("\n----- Visualização de Suporte -----")
    
    conn = connect()  
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Suporte")
    suportes = cursor.fetchall()
    
    if suportes:
        for suporte in suportes:
            print(f"ID Suporte: {suporte[0]}, ID Usuário: {suporte[1]}, ID Arquivo: {suporte[2]}, Descrição: {suporte[5]}")
    else:
        print("Nenhuma solicitação de suporte encontrada.")
    
    conn.close()


def verificar_estrutura_historico():
    conn = connect()  
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(Historico);") 
    colunas = cursor.fetchall()
    
    for coluna in colunas:
        print(coluna)  
    
    conn.close()

verificar_estrutura_historico()

def menu_arquivo_admin():
    print("\n----- Menu Arquivos (Administrador) -----")
    print("1. Inserir Arquivo")
    print("2. Buscar Arquivo")
    print("3. Atualizar Arquivo")
    print("4. Remover Arquivo")
    print("5. Voltar ao Menu Administrador")
    
    escolha = input("Escolha uma opção (1-5): ")
    
    if escolha == "1":
        insert_arquivo_admin()  
    elif escolha == "2":
        buscar_arquivo_admin()  
    elif escolha == "3":
        atualizar_arquivo_admin()  
    elif escolha == "4":
        remover_arquivo_admin()  
    elif escolha == "5":
        menu_admin()  
    else:
        print("Opção inválida. Tente novamente.")
        menu_arquivo_admin() 


def buscar_usuario():
    id_usuario = int(input("Informe o ID do Usuário para buscar: "))
    
    usuario = get_usuario(id_usuario)
    
    if usuario:
        print(f"Usuário encontrado: {usuario}")
    else:
        print("Usuário não encontrado.")
def comentar_arquivo(id_usuario):
    print("\n----- Comentário sobre o Arquivo -----")
    id_arquivo = int(input("Informe o ID do arquivo sobre o qual você deseja comentar: "))
    conteudo = input("Digite o conteúdo do comentário: ")  
    insert_comentario(id_usuario, id_arquivo, conteudo)
    print(f"Comentário sobre o arquivo {id_arquivo} inserido com sucesso!")

def verificar_estrutura_historico():
    conn = connect()  
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(Historico);")  
    colunas = cursor.fetchall()
    
    for coluna in colunas:
        print(coluna)  
    
    conn.close()


verificar_estrutura_historico()

def visualizar_instituicoes_e_planos():
    conn = connect()
    cursor = conn.cursor()
    
    print("\n----- Instituições e Planos -----")
    
    cursor.execute("""
        SELECT I.id_instituicao, I.nome, I.causa_social, I.endereco, P.id_plano, P.nome, P.duracao, P.espaco_usuario
        FROM Instituicao I
        JOIN Instituicao_Plano IP ON I.id_instituicao = IP.id_instituicao
        JOIN Plano P ON IP.id_plano = P.id_plano
    """)
    
    instituicoes_planos = cursor.fetchall()
    
    if instituicoes_planos:
        for instituicao_plano in instituicoes_planos:
            print(f"\nID Instituição: {instituicao_plano[0]}")
            print(f"Nome da Instituição: {instituicao_plano[1]}")
            print(f"Causa Social: {instituicao_plano[2]}")
            print(f"Endereço: {instituicao_plano[3]}")
            print(f"ID Plano: {instituicao_plano[4]}")
            print(f"Nome do Plano: {instituicao_plano[5]}")
            print(f"Duração: {instituicao_plano[6]} meses")
            print(f"Espaço por Usuário: {instituicao_plano[7]} MB")
            print("-" * 50)
    else:
        print("Nenhuma instituição ou plano encontrado.")
    
    conn.close()

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

    visualizar_instituicoes_e_planos()  

    conn.close()
    print("Instituições inseridas com sucesso!")

def carregar_arquivo_user(id_usuario):
    conn = connect()
    cursor = conn.cursor()

    # Exibe os arquivos aos quais o usuário tem acesso
    cursor.execute("SELECT id_arquivo, nome FROM Arquivo WHERE id_usuario = ?", (id_usuario,))
    arquivos = cursor.fetchall()

    if arquivos:
        print("\nArquivos disponíveis:")
        for arquivo in arquivos:
            print(f"ID: {arquivo[0]}, Nome: {arquivo[1]}")
        
        id_arquivo = int(input("Escolha o ID do arquivo para carregar: "))

        # Registra a operação no histórico
        operacao = "Carregar"
        data = datetime.now().strftime('%Y-%m-%d')
        hora = datetime.now().strftime('%H:%M:%S')
        cursor.execute("""
            INSERT INTO Historico (id_arquivo, id_usuario, operacao, data, hora)
            VALUES (?, ?, ?, ?, ?)
        """, (id_arquivo, id_usuario, operacao, data, hora))
        
        # Exibe as informações do arquivo carregado
        cursor.execute("SELECT * FROM Arquivo WHERE id_arquivo = ?", (id_arquivo,))
        arquivo = cursor.fetchone()
        if arquivo:
            print(f"Arquivo carregado: ID: {arquivo[0]}, Nome: {arquivo[1]}, Tipo: {arquivo[2]}")
        else:
            print("Arquivo não encontrado.")
    
    else:
        print("Você não tem arquivos disponíveis.")

    conn.commit()
    conn.close()


def atualizar_arquivo_user(id_arquivo, id_usuario):
    arquivo = get_arquivo(id_arquivo, id_usuario)  
    if arquivo:
        nome = input("Novo Nome do Arquivo: ")
        tipo = input("Novo Tipo do Arquivo: ")

        print("\nEscolha a nova permissão de acesso para o arquivo:")
        print("1. Público - O arquivo pode ser acessado por qualquer usuário.")
        print("2. Privado - O arquivo só pode ser acessado pelo dono do arquivo.")
        print("3. Restrito - O arquivo pode ser acessado por um grupo específico de usuários.")

        permissao_opcao = input("Escolha uma opção (1-3): ")

        if permissao_opcao == "1":
            permissao_de_acesso = "público"
        elif permissao_opcao == "2":
            permissao_de_acesso = "privado"
        elif permissao_opcao == "3":
            permissao_de_acesso = "restrito"
        else:
            print("Opção inválida. A permissão será definida como 'privado' por padrão.")
            permissao_de_acesso = "privado"

        tamanho = float(input("Novo Tamanho do Arquivo (MB): "))
        URL = input("Nova URL: ")
        data_mode = input("Nova Data de Última Modificação (AAAA-MM-DD): ")
        localizacao = input("Nova Localização: ")

        update_arquivo(id_arquivo, nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao)
        print(f"Arquivo {id_arquivo} atualizado com sucesso!")
    else:
        print("Você não tem permissão para atualizar este arquivo.")


def remover_arquivo_user(id_usuario):
    conn = connect()
    cursor = conn.cursor()

  
    cursor.execute("SELECT id_arquivo, nome FROM Arquivo WHERE id_usuario = ?", (id_usuario,))
    arquivos = cursor.fetchall()

    if arquivos:
        print("\nArquivos disponíveis:")
        for arquivo in arquivos:
            print(f"ID: {arquivo[0]}, Nome: {arquivo[1]}")

        id_arquivo = int(input("Escolha o ID do arquivo para remover: "))

     
        operacao = "Remover"
        data = datetime.now().strftime('%Y-%m-%d')
        hora = datetime.now().strftime('%H:%M:%S')
        cursor.execute("""
            INSERT INTO Historico (id_arquivo, id_usuario, operacao, data, hora)
            VALUES (?, ?, ?, ?, ?)
        """, (id_arquivo, id_usuario, operacao, data, hora))
        
 
        cursor.execute("DELETE FROM Arquivo WHERE id_arquivo = ? AND id_usuario = ?", (id_arquivo, id_usuario))
        print(f"Arquivo {id_arquivo} removido com sucesso!")
    else:
        print("Você não tem arquivos disponíveis.")

    conn.commit()
    conn.close()

def remover_arquivo_user(id_usuario):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id_arquivo, nome FROM Arquivo WHERE id_usuario = ?", (id_usuario,))
    arquivos = cursor.fetchall()

    if arquivos:
        print("\nArquivos disponíveis:")
        for arquivo in arquivos:
            print(f"ID: {arquivo[0]}, Nome: {arquivo[1]}")

        id_arquivo = int(input("Escolha o ID do arquivo para remover: "))

     
        operacao = "Remover"
        data = datetime.now().strftime('%Y-%m-%d')
        hora = datetime.now().strftime('%H:%M:%S')
        cursor.execute("""
            INSERT INTO Historico (id_arquivo, id_usuario, operacao, data, hora)
            VALUES (?, ?, ?, ?, ?)
        """, (id_arquivo, id_usuario, operacao, data, hora))
     
        cursor.execute("DELETE FROM Arquivo WHERE id_arquivo = ? AND id_usuario = ?", (id_arquivo, id_usuario))
        print(f"Arquivo {id_arquivo} removido com sucesso!")
    else:
        print("Você não tem arquivos disponíveis.")

    conn.commit()
    conn.close()

def buscar_arquivo_e_comentarios(id_usuario):
    print("\n----- Buscar Arquivo e Mostrar Comentários -----")
    id_arquivo = int(input("Informe o ID do arquivo para buscar: "))

  
    arquivo = get_arquivo(id_arquivo, id_usuario) 
    if arquivo:
        print(f"\nArquivo encontrado: {arquivo[0]}")
        print(f"Nome: {arquivo[1]}, Tipo: {arquivo[2]}, Permissão: {arquivo[3]}")

        
        comentarios = get_comentarios(id_arquivo)  
        if comentarios:
            print("\nComentários sobre este arquivo:")
            for comentario in comentarios:
                print(f"ID Comentário: {comentario[0]}, Conteúdo: {comentario[1]}, Data: {comentario[2]}, Hora: {comentario[3]}")
        else:
            print("Este arquivo não possui comentários.")
    else:
        print("Arquivo não encontrado ou você não tem permissão para acessá-lo.")


def visualizar_compartilhamentos(id_usuario):
  
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT A.id_arquivo, A.nome, C.data_compartilhamento 
        FROM Arquivo A
        JOIN Compartilhamento C ON A.id_arquivo = C.id_arquivo
        WHERE C.id_compartilhado = ?
    """, (id_usuario,))

    compartilhamentos = cursor.fetchall()

    if compartilhamentos:
        print("\nArquivos compartilhados com você:")
        for compartilhamento in compartilhamentos:
            print(f"ID Arquivo: {compartilhamento[0]}, Nome: {compartilhamento[1]}, Data de Compartilhamento: {compartilhamento[2]}")
    else:
        print("Nenhum arquivo foi compartilhado com você.")

    conn.close()


def listar_usuarios():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, login, email FROM Usuario")
    usuarios = cursor.fetchall()
    
    if usuarios:
        print("\n----- Lista de Usuários -----")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Login: {usuario[1]}, Email: {usuario[2]}")
    else:
        print("Nenhum usuário encontrado.")
    
    conn.close()

def listar_administradores():
    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT Usuario.id_usuario, Usuario.login, Usuario.email
        FROM Administrador
        JOIN Usuario ON Administrador.id_usuario = Usuario.id_usuario
    """)
    administradores = cursor.fetchall()
    
    if administradores:
        print("\n----- Lista de Administradores -----")
        for admin in administradores:
            print(f"ID: {admin[0]}, Login: {admin[1]}, Email: {admin[2]}")
    else:
        print("Nenhum administrador encontrado.")
    
    conn.close()


def visualizar_instituicoes_e_planos():
    conn = connect()
    cursor = conn.cursor()
    
    print("\n----- Instituições e Planos -----")
    
    cursor.execute("""
        SELECT I.id_instituicao, I.nome, I.causa_social, I.endereco, P.id_plano, P.nome, P.duracao, P.espaco_usuario
        FROM Instituicao I
        JOIN Instituicao_Plano IP ON I.id_instituicao = IP.id_instituicao
        JOIN Plano P ON IP.id_plano = P.id_plano
    """)
    
    instituicoes_planos = cursor.fetchall()
    
    if instituicoes_planos:
        for instituicao_plano in instituicoes_planos:
            print(f"\nID Instituição: {instituicao_plano[0]}")
            print(f"Nome da Instituição: {instituicao_plano[1]}")
            print(f"Causa Social: {instituicao_plano[2]}")
            print(f"Endereço: {instituicao_plano[3]}")
            print(f"ID Plano: {instituicao_plano[4]}")
            print(f"Nome do Plano: {instituicao_plano[5]}")
            print(f"Duração: {instituicao_plano[6]} meses")
            print(f"Espaço por Usuário: {instituicao_plano[7]} MB")
            print("-" * 50)
    else:
        print("Nenhuma instituição ou plano encontrado.")
    
    conn.close()

    menu_instituicao_plano()  


def compartilhar_arquivo(id_usuario):

    id_arquivo = int(input("Informe o ID do arquivo que deseja compartilhar: "))
    id_compartilhado = int(input("Informe o ID do usuário com quem deseja compartilhar o arquivo: "))

    insert_compartilhamento(id_arquivo, id_usuario, id_compartilhado)
    print(f"Arquivo {id_arquivo} compartilhado com o usuário {id_compartilhado}!")


    

if __name__ == "__main__":
    main()
if __name__ == "__main__":
  
    inserir_instituicoes()  
    inserir_planos()  
