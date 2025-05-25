from conexao import criar_conexao
from datetime import date

def criarUsuario():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    login = input("Digite o login do usuario: ")
    senha = input("Digite a senha do usuario: ")