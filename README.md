# Projeto_BancoDeDados : Minimundo
Linguagem: Deve ser feito usando uma linguagem de apoio a escolha do grupo e SQL. 
## **Integrantes**
- Malu de Faria Neves 
- Marina Mendes
- Nathan Mansur
- Vinicius Anderson

## **Atividade em pares:**
- Modelo conceitual: Nathan, Marina
- Modelo lógico: Nathan, Marina
- Modelo físico: Vinicius, Malu
- Banco de Dados SQL: Vinicius, Malu
- Intercafe python: Vinicius, Malu

## Atividades:
1. Fazer o modelo conceitual  
2. Fazer o modelo lógico  
3. Fazer o modelo físico com as seguintes funcionalidades:  
    a. Criação da base de dados  
    b. Inserir objeto  
    c. Buscar  
    d. Atualizar  
    e. Remover 

---


#### Características do Drive: 
- Os usuários possuem arquivos, estes arquivos podem ser de mídias diversas; 
- Um usuário deve ter um id, login, senha, data de ingresso e email; 
- Arquivos possuem id, nome, tipo, permissões de acesso, tamanho, data de última 
 modificação, localização e URL; 
- O usuário opera os arquivos, podendo ser as seguintes operações: Carregar, atualizar e 
 remover, todas as operações registradas devem ter a data e a hora associadas à elas. 
- Os arquivos podem ser compartilhados com outros usuários, tendo as seguintes informações: 
 id do arquivo, id do dono, id do compartilhado e data de compartilhamento; 
- Um usuário pode ter vários arquivos mas um arquivo deve estar associado a um usuário; 
- Um usuário pode compartilhar um arquivo com vários usuários; 
- O usuário também pode fazer um comentário sobre o seu arquivo, o comentário possui um 
 id, conteúdo, data e hora. Um usuário pode fazer vários arquivos e um arquivo pode ser 
 comentado por vários usuários; 
- A plataforma também acomoda instituições, a instituição possui um id, nome, causa social e 
 endereço; 
- A instituição pode ter vários usuários mas cada usuário só pode estar ligado à uma instituição; 
- A instituição adere a um plano que possui um id, nome, duração, data de aquisição e espaço 
 por usuário(constraint em modelo físico, será implementado na segunda parte). 
- Cada instituição pode ter um plano 
- O sistema também possui um suporte com o administrador, o administrador possui todas as 
- informações que o usuário possui mais um id_administrador; 
- Um usuário pode ter acesso a vários adms e um adm pode suportar vários usuários; 
- Um usuário pode pedir suporte sobre um arquivo específico ou não, este suporte possui id, 
 dia, hora e descrição; 
- Os arquivos possuem um histórico de versionamento, o histórico possui um id, data, hora, 
 operação, id do usuário que alterou o arquivo e conteúdo mudado(sempre em formato de 
 texto).
- Um arquivo pode possuir um ou vários registros de versionamento, mas o registro de 
 versionamento só pode estar vinculado a um único arquivo.

##### Alterações da parte 2:
- Crie uma tabela extra para controle de arquivos. A proposta é que arquivos que não são editados ou 
 operados com frequência tendem a ser cada vez menos usado, a plataforma quer destinar acesso de 
 qualidade aos arquivos com maior atividade. Nenhum usuário pode ter acesso à esta tabela exceto o 
 usuário Root. Segue a estrutura da tabela:
Atividades_recentes: 
    - Id_arquivo(FK) - id do arquivo que está sendo avaliado; 
    - Ultima_versao – um atributo tipo date que registra a ultima data editada do arquivo; 
    - Acesso – pode ser prioritário ou não prioritário. 


---


#### 1 - Implemente as seguintes visões:  
- O usuário não deve ver informações de arquivos que ele não tenha acesso, ele só verá e irá operar arquivos que ele possua acesso;  
- Os administradores terão acesso a toda base de dados;  
- O usuário terá acesso ao histórico de operações, mas ele pode apenas visualizar ela;  
- Em todas as visões implementadas os ids estão ocultos e o usuário não terá acesso a eles;

---


#### 2 - Implemente as seguintes roles:  
- PapelUsuario – Ele terá acesso apenas aos seus arquivos ele pode selecionar, inserir e atualizar os arquivos que ele tenha permissão de acesso;  
- PapelEmpresa – Ele terá acesso aos usuários que fazem parte da empresa e aos arquivos dos funcionários, ela poderá apenas visualizar os usuários e os arquivos;  
- PapelAdm – Ele terá acesso à toda base de dados podendo visualizar, inserir, atualizar ou deletar.  

---


#### 3 - Crie os seguintes procedures:  
- Verificar_atividades – o procedure deve atualizar toda a tabela de atividades_recentes com a data atual;  
- Conta_usuários - Crie um procedure que receba um id de um arquivo e conte quantos  usuários diferentes o mesmo possui;  
- Chavear – Atualiza o arquivo de prioritário para não prioritário e vice-versa.  
- Remover_acessos – Crie um procedure que recebe o id de um arquivo e remove o acesso de todos os usuários menos do proprietário.  

---


#### 4 - Crie as seguintes funções: 
- Crie uma função que verifica se tem mais de 100 dias que o arquivo recebeu uma última alteração, caso sim retorne verdadeiro, caso não, retorne falso;  

---


#### 5 - Crie os seguintes triggers: 
- Safe_security – impeça que arquivos executáveis sejam inseridos no drive;  
- Registrar_operacao – Sempre que um arquivo tiver uma nova operação atualize a data da operação na tabela atividades_recentes;  
- Atualizar_acesso – Sempre que um usuário conseguir acesso a um novo arquivo, atualize os registros de arquivo dele também; 


- Safe_security – impeça que arquivos executáveis sejam inseridos no drive;  
- Registrar_operacao – Sempre que um arquivo tiver uma nova operação atualize a data da operação na tabela atividades_recentes;  
- Atualizar_acesso – Sempre que um usuário conseguir acesso a um novo arquivo, atualize os registros de arquivo dele também; 


---


Claro, Vinicius! Aqui está um **relato completo das dificuldades** que esse projeto de SQL do WebDrive pode apresentar, tanto do ponto de vista técnico quanto de lógica e organização:

---

##  Dificuldades do Projeto WebDrive (SQL e Integração com Python)

###  1. **Modelagem Complexa do Banco de Dados**

* **Relacionamentos muitos-para-muitos**, como:

  * `usuario_instituicao`
  * `instituicao_plano`
* **Dependências fortes** entre tabelas, exigindo controle rigoroso de chaves estrangeiras.
* Exemplo: não é possível inserir um `arquivo` sem que o `usuario` e a `instituicao` já existam.

---

###  2. **Manutenção da Integridade Referencial**

* **Problemas com ordem de inserção**:

  * É necessário seguir uma ordem específica (ex: criar `plano` → `instituicao` → `usuario`).
* **Exclusão de dados**:

  * Ao deletar, você precisa cuidar das tabelas filhas primeiro para evitar erros por FK.
  * Requer **cascateamento manual** ou definição de `ON DELETE CASCADE` corretamente.

---

###  3. **Criação de Procedures, Triggers e Views**

* Sintaxe do MySQL pode ser confusa:

  * Uso obrigatório de `DELIMITER`.
  * Escopo de variáveis em procedures.
* Manter consistência entre procedures e o que está implementado em Python exige atenção.
* **Testes manuais difíceis** para triggers e procedures que envolvem muitos dados conectados.

---

###  4. **Gerenciamento de Versionamento e Histórico**

* A tabela `historico` exige:

  * Registro automático de operações (idealmente via `trigger`).
  * Lidar com conteúdos modificados, horários, e usuários responsáveis.
* Difícil manter sincronização entre `arquivo`, `historico` e `opera`.

---

###  5. **Compartilhamento e Comentários**

* Lógica de compartilhamento exige:

  * Garantir que o `usuário destinatário` exista.
  * Lidar com **acesso duplicado** ou tentativas de compartilhamento redundante.
* Comentários dependem de dois `JOINs` para cruzar com `arquivo` e `usuário`.

---

### 6. **Controle de Acesso e Permissões**

* Atributo `Permissoes_acesso` no arquivo precisa ser bem definido (ex: leitura, escrita, admin).
* Falta de padronização nesse campo pode causar **erros de segurança e lógica.**

---

###  7. **Conectividade com Python**

* Perigo de **SQL Injection**, já que os comandos estão montados com `f-strings`.

  * Correto seria usar `cursor.execute(query, valores)` com parâmetros.
* Manter a consistência dos dados entre código Python e banco é trabalhoso sem uma camada ORM (como SQLAlchemy).
* Difícil testar o projeto sem uma interface amigável (GUI ou web), já que tudo está via terminal.

---

###  8. **Carga de Dados e Testes**

* Testar todas as tabelas exige dados bem encadeados.

  * Ex: um `comentário` precisa de `usuario`, `arquivo`, `instituicao`, etc.
* Geração de massa de teste manual é **trabalhosa**.
* Bugs podem surgir com dados nulos, formatos de data/hora errados ou id’s inexistentes.


