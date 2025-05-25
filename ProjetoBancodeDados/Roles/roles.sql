USE projetowb;
-- Usuario pode selecionar, inseriir e atualizar arquivos com acesso
CREATE ROLE pUsuario;
GRANT SELECT, INSERT, UPDATE ON Arquivo TO pUsuario;
GRANT SELECT ON Historico TO pUsuario;

-- Empresa pode ver (usuarios e arquivos) apenas ver.
CREATE ROLE pEmpresa;
GRANT SELECT ON Usuario TO pEmpresa;
GRANT SELECT ON Arquivo TO pEmpresa;

-- Adm pode fazer tudo.

CREATE ROLE pAdm;
GRANT ALL PRIVILEGES ON projetowb.* TO pAdm;