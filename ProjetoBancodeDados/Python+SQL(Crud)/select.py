from database import connect


def get_usuario(id_usuario):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario WHERE id_usuario = ?", (id_usuario,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def get_arquivo(id_arquivo, id_usuario):
    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT * FROM Arquivo WHERE id_arquivo = ?
    """, (id_arquivo,))

    arquivo = cursor.fetchone()
    if arquivo:
        permissao = arquivo[3]  

        cursor.execute("""
            SELECT COUNT(*) FROM Administrador WHERE id_usuario = ?
        """, (id_usuario,))
        is_admin = cursor.fetchone()[0] > 0

        if is_admin:
       
            return arquivo

       
        if permissao == 'público':
          
            return arquivo
        elif permissao == 'privado':
       
            cursor.execute("""
                SELECT id_usuario FROM Arquivo WHERE id_arquivo = ?
            """, (id_arquivo,))
            dono_arquivo = cursor.fetchone()[0]

            if dono_arquivo == id_usuario:
                return arquivo
        elif permissao == 'restrito':
            
            pass  
    conn.close()
    return None  
    return result

def get_compartilhamentos(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Compartilhamento WHERE id_arquivo = ?", (id_arquivo,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def get_comentarios(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Comentario WHERE id_arquivo = ?", (id_arquivo,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result



def get_historico_arquivo(id_arquivo):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_historico, id_arquivo, id_usuario, operacao, data, hora, conteudo_mudado 
        FROM Historico
        WHERE id_arquivo = ?
    """, (id_arquivo,))
    
    historico = cursor.fetchall()  
    conn.close()
    
    return historico


def get_arquivos_usuario(id_usuario):
    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT id_arquivo, nome FROM Arquivo 
        WHERE id_usuario = ? OR permissao_de_acesso = 'público'
    """, (id_usuario,))
    
    arquivos = cursor.fetchall()
    conn.close()
    return arquivos

    
    conn.close()
    return historico

def verificar_id_usuario_existente(id_usuario):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Usuario WHERE id_usuario = ?", (id_usuario,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] > 0







#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR

#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR