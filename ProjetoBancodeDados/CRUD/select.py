from database import connect

# Consultar usuário por ID
def get_usuario(id_usuario):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario WHERE id_usuario = ?", (id_usuario,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Consultar arquivo por ID
def get_arquivo(id_arquivo, id_usuario):
    conn = connect()
    cursor = conn.cursor()

    # Consultando o arquivo com base no id
    cursor.execute("""
        SELECT * FROM Arquivo WHERE id_arquivo = ?
    """, (id_arquivo,))

    arquivo = cursor.fetchone()
    if arquivo:
        permissao = arquivo[3]  # Coluna de permissão de acesso na tabela Arquivo

        # Verifica se o usuário é administrador
        cursor.execute("""
            SELECT COUNT(*) FROM Administrador WHERE id_usuario = ?
        """, (id_usuario,))
        is_admin = cursor.fetchone()[0] > 0

        if is_admin:
            # O administrador pode ver todos os arquivos
            return arquivo

        # Verificar permissão do usuário
        if permissao == 'público':
            # Arquivo público é acessível por qualquer usuário
            return arquivo
        elif permissao == 'privado':
            # O arquivo é privado, apenas o dono pode acessar
            cursor.execute("""
                SELECT id_usuario FROM Arquivo WHERE id_arquivo = ?
            """, (id_arquivo,))
            dono_arquivo = cursor.fetchone()[0]

            if dono_arquivo == id_usuario:
                return arquivo
        elif permissao == 'restrito':
            # Implementar lógica para acesso restrito (grupo específico)
            pass  # Se houver um controle de grupos, deve ser checado aqui

    conn.close()
    return None  # Retorna None se o usuário não tem acesso
    return result
# Consultar compartilhamentos de um arquivo
def get_compartilhamentos(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Compartilhamento WHERE id_arquivo = ?", (id_arquivo,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Consultar comentários de um arquivo
def get_comentarios(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Comentario WHERE id_arquivo = ?", (id_arquivo,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

from database import connect

def get_historico_arquivo(id_arquivo):
    conn = connect()  # Conecta ao banco de dados
    cursor = conn.cursor()
    
    # Consulta o histórico de operações do arquivo
    cursor.execute("""
        SELECT id_historico, id_arquivo, operacao, data, hora, conteudo_mudado
        FROM Historico
        WHERE id_arquivo = ?
    """, (id_arquivo,))
    
    historico = cursor.fetchall()  # Retorna todas as entradas de histórico encontradas
    
    conn.close()
    return historico
