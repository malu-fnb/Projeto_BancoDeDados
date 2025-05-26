from database import connect
from insert import insert_usuario, insert_arquivo, insert_administrador, insert_compartilhamento, insert_comentario, insert_suporte, insert_historico, insert_instituicao, insert_plano, associate_instituicao_plano
from select import get_usuario, get_arquivo, get_compartilhamentos, get_comentarios, get_historico_arquivo
from update import update_usuario, update_arquivo
from delete import delete_usuario, delete_arquivo
from models import create_tables

# Função para mostrar o menu principal
def mostrar_menu():
    print("\nMenu:")
    print("1. Inserir Usuário - Cadastrar um novo usuário no sistema")
    print("2. Buscar Usuário - Consultar um usuário existente no sistema")
    print("3. Atualizar Usuário - Atualizar os dados de um usuário existente")
    print("4. Remover Usuário - Excluir um usuário do sistema")
    print("5. Inserir Arquivo - Adicionar um novo arquivo ao sistema")
    print("6. Buscar Arquivo - Consultar um arquivo existente")
    print("7. Atualizar Arquivo - Atualizar os dados de um arquivo existente")
    print("8. Remover Arquivo - Excluir um arquivo do sistema")
    print("9. Compartilhar Arquivo - Compartilhar um arquivo com outro usuário")
    print("10. Comentar Arquivo - Adicionar um comentário sobre um arquivo")
    print("11. Inserir Administrador - Associar um usuário a um administrador")
    print("12. Solicitar Suporte - Pedir suporte para um arquivo")
    print("13. Gerenciar Instituições e Planos - Inserir e associar instituições e planos")
    print("14. Sair - Fechar o sistema")

# Função de login simplificado (sem consulta ao banco)
def login():
    print("\n----- Sistema de Login -----")
    tipo_usuario = input("Você é um(a): \n1. Administrador\n2. Usuário\nEscolha (1-2): ")

    # Solicitar a senha após a escolha do tipo de usuário
    senha = input("Digite sua senha: ")

    # Conectar ao banco de dados
    conn = connect()
    cursor = conn.cursor()

    # Se for Administrador
    if tipo_usuario == "1" and senha == "admin123":
        print("Bem-vindo, Administrador!")
        conn.close()
        return 'admin', None  # Retorna 'admin' se for administrador e None para o id_usuario

    # Se for Usuário
    elif tipo_usuario == "2":
        cursor.execute(""" 
            SELECT id_usuario FROM Usuario WHERE senha = ?
        """, (senha,))
        user = cursor.fetchone()
        if user:
            id_usuario = user[0]  # Captura o id do usuário autenticado
            print("Bem-vindo, Usuário!")
            conn.close()
            return 'user', id_usuario  # Retorna 'user' e o id_usuario para o usuário autenticado
        else:
            print("Senha incorreta.")
            conn.close()
            return None, None  # Retorna None se a senha estiver incorreta

    else:
        print("Opção inválida!")
        conn.close()
        return None, None  # Se a opção for inválida, retorna None

def main():
    while True:
        usuario_tipo, id_usuario = login()  # Recebe tipo e id_usuario após o login

        if usuario_tipo == 'admin':
            menu_admin()  # Se for admin, chama o menu do administrador
        elif usuario_tipo == 'user' and id_usuario:  # Verifica se o id_usuario existe
            menu_usuario(id_usuario)  # Passa o id_usuario para o menu
        else:
            print("Tentando novamente...")



# Função para o menu do Administrador
# Função para o menu do Administrador
def menu_admin():
    print("\n----- Menu Administrador -----")
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Arquivos")
    print("3. Gerenciar Instituições e Planos")
    print("4. Visualizar Suporte")
    print("5. Sair")
    
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        menu_gerenciar_usuarios()  # Chama a função de gerenciamento de usuários
    elif escolha == "2":
        menu_arquivo_admin()
    elif escolha == "3":
        menu_instituicao_plano()
    elif escolha == "4":
        menu_suporte_admin()
    elif escolha == "5":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida.")

# Função para o menu de Gerenciamento de Usuários do Administrador
def menu_gerenciar_usuarios():
    print("\n----- Gerenciamento de Usuários -----")
    print("1. Inserir Novo Usuário")
    print("2. Buscar Usuário")
    print("3. Atualizar Usuário")
    print("4. Remover Usuário")
    print("5. Voltar ao Menu Administrador")
    
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        insert_usuario()  # Função para inserir um novo usuário
    elif escolha == "2":
        buscar_usuario()  # Função para buscar um usuário
    elif escolha == "3":
        atualizar_usuario()  # Função para atualizar um usuário
    elif escolha == "4":
        remover_usuario()  # Função para remover um usuário
    elif escolha == "5":
        menu_admin()  # Volta para o menu administrador
    else:
        print("Opção inválida.")
        menu_gerenciar_usuarios()  # Retorna ao menu de gerenciamento de usuários


# Função para o menu do Usuário
# Função para o menu do Usuário
def menu_usuario(id_usuario):  # Agora a função aceita o argumento id_usuario
    print("\n----- Menu Usuário -----")
    print("1. Gerenciar Arquivos")
    print("2. Visualizar Histórico de Operações")
    print("3. Solicitar Suporte")
    print("4. Sair")
    
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        menu_arquivo_user(id_usuario)  # Passa id_usuario para a próxima função
    elif escolha == "2":
        menu_historico(id_usuario)  # Passa id_usuario para o menu de histórico
    elif escolha == "3":
        menu_suporte_user(id_usuario)  # Passa id_usuario para a próxima função
    elif escolha == "4":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida.")
        menu_usuario(id_usuario)  # Passa id_usuario para o menu novamente


# Função para o menu de Arquivos do Administrador
def menu_arquivo_admin():
    print("\n----- Menu Arquivos (Administrador) -----")
    print("1. Inserir Arquivo")
    print("2. Buscar Arquivo")
    print("3. Atualizar Arquivo")
    print("4. Remover Arquivo")
    print("5. Voltar")
    
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
        print("Opção inválida.")

# Função para o menu de Arquivos do Usuário
def menu_arquivo_user(id_usuario):  # Agora a função aceita o argumento id_usuario
    print("\n----- Menu Arquivos (Usuário) -----")
    print("1. Buscar Arquivo")
    print("2. Atualizar Arquivo")
    print("3. Voltar")
    
    escolha = input("Escolha uma opção (1-3): ")
    
    if escolha == "1":
        buscar_arquivo_user(id_usuario)  # Passa id_usuario para a próxima função
    elif escolha == "2":
        atualizar_arquivo_user(id_usuario)  # Passa id_usuario para a próxima função
    elif escolha == "3":
        menu_usuario(id_usuario)  # Passa id_usuario para o menu de usuário
    else:
        print("Opção inválida.")
        menu_arquivo_user(id_usuario)  # Passa id_usuario para o menu novamente

# Função para o menu de Histórico
def menu_historico(id_usuario):  # Agora a função aceita o argumento id_usuario
    print("\nHistórico de Operações")
    id_arquivo = int(input("Informe o ID do arquivo para visualizar o histórico: "))
    
    # Chama a função que retorna o histórico do arquivo
    historico = get_historico_arquivo(id_arquivo)
    
    if historico:
        for registro in historico:
            print(f"ID Histórico: {registro[0]}")
            print(f"Operação: {registro[2]}")
            print(f"Data: {registro[3]}")
            print(f"Hora: {registro[4]}")
            print(f"Conteúdo Alterado: {registro[5]}")
            print("-" * 30)  # Linha separadora para cada operação
    else:
        print("Nenhum histórico encontrado para este arquivo.")

# Função para o menu de Suporte (Usuário)
# Função para o menu de Suporte (Usuário)
# Função para o menu de Suporte (Usuário)
def menu_suporte_user(id_usuario):
    print("\n----- Suporte (Usuário) -----")
    print("1. Solicitar Suporte para Arquivo")
    print("2. Voltar")
    
    escolha = input("Escolha uma opção (1-2): ")

    if escolha == "1":
        solicitar_suporte(id_usuario)  # Passando o ID do usuário para a função
    elif escolha == "2":
        menu_usuario(id_usuario)
    else:
        print("Opção inválida.")


        # Função para o menu de Gerenciamento de Instituições e Planos
# Função para o menu de Instituições e Planos
# Função para o menu de Instituições e Planos
def menu_instituicao_plano():
    print("\n----- Menu Instituições e Planos -----")
    print("1. Inserir Instituição")
    print("2. Associar Instituição a um Plano")
    print("3. Voltar ao Menu Administrador")
    
    escolha = input("Escolha uma opção (1-3): ")

    if escolha == "1":
        nome = input("Nome da Instituição: ")
        causa_social = input("Causa Social da Instituição: ")
        endereco = input("Endereço da Instituição: ")
        insert_instituicao(nome, causa_social, endereco)  # Chama a função de inserção de instituição
    elif escolha == "2":
        id_instituicao = int(input("Informe o ID da Instituição: "))
        id_plano = int(input("Informe o ID do Plano: "))
        associate_instituicao_plano(id_instituicao, id_plano)  # Chama a função de associação de instituição a plano
    elif escolha == "3":
        menu_admin()  # Volta ao menu administrador
    else:
        print("Opção inválida.")
        menu_instituicao_plano()  # Retorna ao menu de instituições e planos


# Função para o menu de Suporte (Administrador)
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
    
    # Obtém o histórico de operações do arquivo
    historico = get_historico_arquivo(id_arquivo)
    
    if historico:
        for registro in historico:
            print(f"ID Histórico: {registro[0]}")
            print(f"Operação: {registro[2]}")
            print(f"Data: {registro[3]}")
            print(f"Hora: {registro[4]}")
            print(f"Conteúdo Alterado: {registro[5]}")
            print("-" * 30)  # Linha separadora para cada operação
    else:
        print("Nenhum histórico encontrado para este arquivo.")


# Função para adicionar um arquivo
# Função para adicionar um arquivo
def insert_arquivo_admin():
    nome = input("Nome do Arquivo: ")
    tipo = input("Tipo do Arquivo: ")
    
    # Exibe as opções de permissão de acesso
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
    
    # Inserir no banco de dados o arquivo com as informações fornecidas
    insert_arquivo(nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_usuario)
    print(f"Arquivo '{nome}' inserido com sucesso!")


# Função para buscar um arquivo
def buscar_arquivo_admin():
    id_arquivo = int(input("Informe o ID do Arquivo para buscar: "))
    
    arquivo = get_arquivo(id_arquivo, None)  # Administrador tem acesso a todos os arquivos
    
    if arquivo:
        print(f"Arquivo encontrado: {arquivo}")
    else:
        print("Arquivo não encontrado.")

# Função para atualizar um arquivo
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

# Função para remover um arquivo
def remover_arquivo_admin():
    id_arquivo = int(input("Informe o ID do Arquivo para remover: "))
    
    delete_arquivo(id_arquivo)
    print(f"Arquivo {id_arquivo} removido com sucesso!")

# Função para buscar arquivo do usuário
def buscar_arquivo_user(id_usuario):
    id_arquivo = int(input("Informe o ID do Arquivo para buscar: "))
    
    arquivo = get_arquivo(id_arquivo, id_usuario)  # Passando o id_usuario para verificar o acesso
    
    if arquivo:
        print(f"Arquivo encontrado: {arquivo}")
    else:
        print("Você não tem acesso a este arquivo.")

# Função para atualizar arquivo do usuário
def atualizar_arquivo_user():
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

# Função para solicitar suporte
def solicitar_suporte(id_usuario):
    id_arquivo = int(input("Informe o ID do Arquivo para solicitar suporte: "))
    descricao = input("Descrição do Suporte: ")
    
    insert_suporte(id_usuario, id_arquivo, descricao)
    print(f"Suporte solicitado para o Arquivo {id_arquivo}.")

   


# Função para visualizar suporte (admin)
# Função para visualizar suporte (admin)
def visualizar_suporte():
    print("\n----- Visualização de Suporte -----")
    
    # Conectando ao banco de dados
    conn = connect()  # Cria a conexão com o banco de dados
    cursor = conn.cursor()
    
    # Executando a consulta para visualizar todos os suportes
    cursor.execute("SELECT * FROM Suporte")
    suportes = cursor.fetchall()
    
    if suportes:
        for suporte in suportes:
            print(f"ID Suporte: {suporte[0]}, ID Usuário: {suporte[1]}, ID Arquivo: {suporte[2]}, Descrição: {suporte[5]}")
    else:
        print("Nenhuma solicitação de suporte encontrada.")
    
    # Fechar a conexão
    conn.close()


def verificar_estrutura_historico():
    conn = connect()  # Conecta ao banco de dados
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(Historico);")  # Consulta a estrutura da tabela
    colunas = cursor.fetchall()
    
    for coluna in colunas:
        print(coluna)  # Exibe as informações de cada coluna
    
    conn.close()

# Se você precisar verificar a estrutura da tabela, chame esta função em um ponto de teste
verificar_estrutura_historico()



def verificar_estrutura_historico():
    conn = connect()  # Conecta ao banco de dados
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(Historico);")  # Consulta a estrutura da tabela
    colunas = cursor.fetchall()
    
    for coluna in colunas:
        print(coluna)  # Exibe as informações de cada coluna
    
    conn.close()

# Chame a função para verificar a estrutura da tabela (para depuração)
verificar_estrutura_historico()


    

if __name__ == "__main__":
    main()
