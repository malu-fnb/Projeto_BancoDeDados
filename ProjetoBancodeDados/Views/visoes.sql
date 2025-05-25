USE projetowb;
-- VIEW

--  usuário não deve ver informações de arquivos que ele não tenha acesso, ele só verá e irá operar arquivos que ele possua acesso;
CREATE VIEW view_arquivo_usuario AS
SELECT a.nome, a.tipo, a.permissao_de_acesso, a.tamanho, a.URL, a.data_mode, a.localizacao
FROM 
arquivo a
JOIN
Acesso ac on a.id_arquivo = ac.id_arquivo
WHERE
ac.id_usuario = CURRENT_USER();

-- os administradores terão acesso a toda base de dados.
CREATE VIEW view_adm AS
SELECT 
nome, tipo, permissao_de_acesso, tamanho, URL, data_mode, localizacao
FROM Arquivo;

-- usuário terá acesso ao histórico de operações, mas ele pode apenas visualizar ela
CREATE VIEW view_historico_operacao AS
SELECT 
data, hora, conteudo_mudado, operacao
FROM Historico
WHERE id_usuario_alteracao = CURRENT_USER();