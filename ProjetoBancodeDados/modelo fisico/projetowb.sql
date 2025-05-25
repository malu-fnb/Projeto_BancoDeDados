USE projetowb;

-- Usuario
CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    data_ingresso DATE,
    email VARCHAR(100)
);

--  Adm
CREATE TABLE Adm (
    id_adm INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    data_ingresso DATE,
    email VARCHAR(100),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

--  Instituicao
CREATE TABLE Instituicao (
    id_instituicao INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    causa_social VARCHAR(100),
    endereco VARCHAR(150)
);

-- Relacionamento contem 
CREATE TABLE Usuario_Instituicao (
    id_usuario INT,
    id_instituicao INT,
    PRIMARY KEY (id_usuario, id_instituicao),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_instituicao) REFERENCES Instituicao(id_instituicao)
);

-- Plano
CREATE TABLE Plano (
    id_plano INT PRIMARY KEY AUTO_INCREMENT,
    duracao INT,
    data_aquisicao DATE,
    espaco_usuario FLOAT
);

-- Relacionamento Adere
CREATE TABLE Instituicao_Plano (
    id_instituicao INT,
    id_plano INT,
    PRIMARY KEY (id_instituicao, id_plano),
    FOREIGN KEY (id_instituicao) REFERENCES Instituicao(id_instituicao),
    FOREIGN KEY (id_plano) REFERENCES Plano(id_plano)
);

--  Arquivo
CREATE TABLE Arquivo (
    id_arquivo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    tipo VARCHAR(50),
    permissao_de_acesso VARCHAR(50),
    tamanho FLOAT,
    URL TEXT,
    data_mode DATE,
    localizacao VARCHAR(100)
);

-- Comentario
CREATE TABLE Comentario (
    id_comentario INT PRIMARY KEY AUTO_INCREMENT,
    conteudo TEXT,
    data DATE,
    hora TIME
);

-- Relacionamento faz 
CREATE TABLE Usuario_Comentario (
    id_usuario INT,
    id_comentario INT,
    PRIMARY KEY (id_usuario, id_comentario),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_comentario) REFERENCES Comentario(id_comentario)
);

-- Relacionamento Compartilha 
CREATE TABLE Compartilhamento (
    id_compartilhamento INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_arquivo INT,
    id_dono INT,
    data_compartilhamento DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo),
    FOREIGN KEY (id_dono) REFERENCES Usuario(id_usuario)
);

-- Relacionamento Acesso 
CREATE TABLE Acesso (
    id_usuario INT,
    id_arquivo INT,
    PRIMARY KEY (id_usuario, id_arquivo),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo)
);

--  Operar 
CREATE TABLE Operar (
    id_usuario INT,
    id_arquivo INT,
    tipo_de_operacao VARCHAR(50),
    data DATE,
    hora TIME,
    PRIMARY KEY (id_usuario, id_arquivo, data, hora),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo)
);

-- Tabela Suporte
CREATE TABLE Suporte (
    id_suporte INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_arquivo INT,
    data DATE,
    hora TIME,
    descricao TEXT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo)
);

-- Historico
CREATE TABLE Historico (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    id_arquivo INT,
    id_usuario_alteracao INT,
    data DATE,
    hora TIME,
    conteudo_mudado TEXT,
    operacao VARCHAR(50),
    FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo),
    FOREIGN KEY (id_usuario_alteracao) REFERENCES Usuario(id_usuario)
);
-- parte 2 atividades
CREATE TABLE Atividades_recentes (
    id_arquivo INT,
    ultima_versao DATE,
    acesso ENUM('prioritário', 'não prioritário') DEFAULT 'não prioritário',
    PRIMARY KEY (id_arquivo),
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
);
