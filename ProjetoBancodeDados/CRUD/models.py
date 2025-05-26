from database import connect

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Tabela de Usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            data_ingresso TEXT,
            email TEXT
        );
    """)

    # Tabela de Administradores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Administrador (
            id_administrador INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
        );
    """)

    # Tabela de Arquivos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Arquivo (
            id_arquivo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            tipo TEXT,
            permissao_de_acesso TEXT,
            tamanho REAL,
            URL TEXT,
            data_mode TEXT,
            localizacao TEXT,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
        );
    """)

    # Tabela de Histórico de Operações
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Historico (
            id_historico INTEGER PRIMARY KEY AUTOINCREMENT,
            id_arquivo INTEGER,
            id_usuario INTEGER,
            operacao TEXT,
            data TEXT,
            hora TEXT,
            FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo),
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
        );
    """)

    # Tabela de Compartilhamento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Compartilhamento (
            id_compartilhamento INTEGER PRIMARY KEY AUTOINCREMENT,
            id_arquivo INTEGER,
            id_dono INTEGER,
            id_compartilhado INTEGER,
            data_compartilhamento TEXT,
            FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo),
            FOREIGN KEY (id_dono) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_compartilhado) REFERENCES Usuario(id_usuario)
        );
    """)

    # Tabela de Comentários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comentario (
            id_comentario INTEGER PRIMARY KEY AUTOINCREMENT,
            conteudo TEXT,
            data TEXT,
            hora TEXT,
            id_usuario INTEGER,
            id_arquivo INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo)
        );
    """)

    # Tabela de Suporte
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Suporte (
            id_suporte INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            id_arquivo INTEGER,
            data TEXT,
            hora TEXT,
            descricao TEXT,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo)
        );
    """)

    # Tabela de Instituições
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Instituicao (
            id_instituicao INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            causa_social TEXT,
            endereco TEXT
        );
    """)

    # Tabela de Planos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Plano (
            id_plano INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao INTEGER,  -- em meses
            espaco_usuario REAL,  -- espaço em MB ou outro valor relevante
            data_aquisicao TEXT
        );
    """)

    # Relacionamento entre Usuários e Instituições
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuario_Instituicao (
            id_usuario INTEGER,
            id_instituicao INTEGER,
            PRIMARY KEY (id_usuario, id_instituicao),
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_instituicao) REFERENCES Instituicao(id_instituicao)
        );
    """)

    # Relacionamento entre Instituições e Planos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Instituicao_Plano (
            id_instituicao INTEGER,
            id_plano INTEGER,
            PRIMARY KEY (id_instituicao, id_plano),
            FOREIGN KEY (id_instituicao) REFERENCES Instituicao(id_instituicao),
            FOREIGN KEY (id_plano) REFERENCES Plano(id_plano)
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

# Rodar a função para garantir que as tabelas sejam criadas ao iniciar o script.
create_tables()
