from database import connect
from datetime import datetime

# Atualizar usuário
def update_usuario(id_usuario, login, senha, data_ingresso, email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Usuario SET login = ?, senha = ?, data_ingresso = ?, email = ? WHERE id_usuario = ?
    """, (login, senha, data_ingresso, email, id_usuario))
    conn.commit()
    cursor.close()
    conn.close()

# Atualizar arquivo
def update_arquivo(id_arquivo, nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Arquivo SET nome = ?, tipo = ?, permissao_de_acesso = ?, tamanho = ?, URL = ?, 
        data_mode = ?, localizacao = ? WHERE id_arquivo = ?
    """, (nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao, id_arquivo))
    conn.commit()
    cursor.close()
    conn.close()

# Registrar operação no histórico (carregar, atualizar, remover)
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
