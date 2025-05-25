USE projetowb;

--Procedures 

-- Verificar_atividades – o procedure deve atualizar toda a tabela de atividades_recentes com a data atual; 
DELIMITER $$
CREATE PROCEDURE Verificar_atividades()
BEGIN
    UPDATE Atividades_recentes
    SET ultima_versao = CURDATE();
END $$
DELIMITER ;

--  Crie um procedure que receba um id de um arquivo e conte quantos usuários diferentes o mesmo possui;
DELIMITER $$
CREATE PROCEDURE Conta_usuarios(IN idArquivo INT)
BEGIN
    SELECT COUNT(DISTINCT id_usuario) AS total_usuarios
    FROM Acesso
    WHERE id_arquivo = idArquivo;
END $$
DELIMITER ;

--  Atualiza o arquivo de prioritário para não prioritário e vice-versa. 
DELIMITER $$
CREATE PROCEDURE Chavear(IN idArquivo INT)
BEGIN
    UPDATE Atividades_recentes
    SET acesso = 
        CASE 
            WHEN acesso = 'prioritário' THEN 'não prioritário'
            ELSE 'prioritário'
        END
    WHERE id_arquivo = idArquivo;
END $$
DELIMITER ;

--   Crie um procedure que recebe o id de um arquivo e remove o acesso de todos os usuários menos do proprietário. 
DELIMITER $$
CREATE PROCEDURE Remover_acessos(IN idArquivo INT, IN idProprietario INT)
BEGIN
    DELETE FROM Acesso
    WHERE id_arquivo = idArquivo AND id_usuario != idProprietario;
END $$
DELIMITER ;


































-- anti-copia* not IA