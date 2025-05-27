from database import connect


def delete_usuario(id_usuario):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Usuario WHERE id_usuario = ?", (id_usuario,))
    
    conn.commit()
    conn.close()
    print(f"Usuário de ID {id_usuario} removido com sucesso!")



#PROJETO DE BANCO DE DADOS: VINICIUS ANDERSON, MALU DE FARIA NEVES, MARINA DURAND E NATHAN MANSUR
def delete_arquivo(id_arquivo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Arquivo WHERE id_arquivo = ?", (id_arquivo,))
    conn.commit()
    cursor.close()
    conn.close()
