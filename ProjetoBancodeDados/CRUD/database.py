import sqlite3

def connect():
    """Conecta ao banco de dados SQLite (será criado no mesmo diretório do script)"""
    conn = sqlite3.connect('projetowb.db')  # Nome do arquivo do banco de dados SQLite
    return conn
