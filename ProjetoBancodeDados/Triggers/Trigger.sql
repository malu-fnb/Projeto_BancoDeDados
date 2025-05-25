USE projetowb;
-- Trigger SAFE_SECURITY  impeça que arquivos executáveis sejam inseridos no drive; 
DELIMITER $$
CREATE TRIGGER Safe_security
BEFORE INSERT ON Arquivo
FOR EACH ROW
BEGIN
    IF NEW.tipo= 'exe' THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Arquivos executaveis(.exe) nãp podem ser inseridos no drive!'
    END IF;
    END $$
    DELIMITER ;

    -- Trigger Registrar_operacoes( Sempre que um arquivo tiver uma nova operação atualize a data da operação na tabela atividades_recentes; )
    DELIMITER $$
    CREATE TRIGGER Registrar_operacao
    AFTER INSERT ON Operar
    FOR EACH ROW 
    BEGIN
    UPDATE Atividades_recentes
    SET ultima_versao = CURDATE()
    WHERE id_arquivo = NEW.id_arquivo;
    UPDATE Arquivo
    SET data_mode = CURDATE()
    WHERE id_arquivo = NEW.id_arquivo;
    END $$
    DELIMITER $$
    
    -- Trigger Atualizar_Acesso ( Sempre que um usuário conseguir acesso a um novo arquivo, atualize os registros de arquivo dele também;)
    DELIMITER $$
    CREATE TRIGGER Atualizar_Acesso
    AFTER INSERT ON Compartilhamento
    FOR EACH ROW 
    BEGIN
UPDATE Atividades_recentes
SET ultima_versao = CURDATE()
WHERE id_arquivo = NEW.id_arquivo;
UPDATE Arquivo
SET data_mode = CURDATE()
WHERE id_arquivo = NEW.id_arquivo;
END $$
DELIMITER ;
