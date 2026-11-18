# Documentação Técnica: Sistema de Gerenciamento de Biblioteca Comunitária

**Curso:** Técnico em Desenvolvimento de Sistemas  
**Responsável pelo Desenvolvimento:** [Nome do estudante]  
**Data:** [Data de elaboração]  
**Versão do Documento:** 2.0  

---

## Histórico de Revisões

| Versão | Data | Descrição | Responsável |
| :--- | :--- | :--- | :--- |
| **1.0** | [Data] | Planejamento inicial do sistema. | [Nome do estudante] |
| **2.0** | [Data] | Revisão com base no modelo de SRS: inclusão de perfis de usuário, requisitos com prioridade e critérios de aceite, modelagem de dados e plano de testes. | [Nome do estudante] |

---

## 1. Visão Geral do Projeto

* **Nome do Projeto:** Sistema de Gerenciamento de Biblioteca Comunitária
* **Versão:** 2.0

### 1.1. Descrição e Propósito

A biblioteca comunitária realiza sua rotina de atendimento sem um sistema informatizado. O controle manual de empréstimos e de registros de leitores e livros pode causar perda de obras, duplicidade de informações e falhas no armazenamento dos dados. Além disso, a ausência de proteção adequada para informações pessoais, como o CPF dos leitores, representa risco à privacidade e ao cumprimento da Lei Geral de Proteção de Dados (LGPD).

O sistema tem como propósito centralizar os registros de leitores, livros e empréstimos, controlar o acesso por perfil de usuário e proteger as informações armazenadas. O valor gerado está na melhoria do atendimento ao público, na organização das atividades administrativas e na confiabilidade dos dados.

### 1.2. Público-alvo

* **Técnico (bibliotecário):** Responsável por administrar leitores, livros e empréstimos e executar as operações internas da biblioteca.
* **Usuário comum (leitor):** Pessoa cadastrada na biblioteca que consulta o catálogo de livros e, quando disponível, os próprios empréstimos.

### 1.3. Objetivos

* **Objetivo Geral:** Desenvolver um sistema informatizado para gerenciar leitores, livros e empréstimos de uma biblioteca comunitária, proporcionando organização, segurança e confiabilidade no armazenamento e na consulta das informações.
* **Objetivos Específicos:**
  * Implementar autenticação de usuários com validação de credenciais e expiração de sessão.
  * Diferenciar os perfis de técnico (bibliotecário) e usuário comum (leitor), com permissões específicas.
  * Permitir o cadastro e o gerenciamento de leitores e livros.
  * Disponibilizar busca de leitores e consulta do catálogo de livros.
  * Permitir o registro e a consulta de empréstimos associados a leitores e livros, organizados por data.
  * Proteger os dados sensíveis armazenados no banco de dados.
  * Elaborar a documentação técnica e o diagrama entidade-relacionamento do sistema.

### 1.4. Escopo

* **Incluso no Escopo:** Autenticação com identificação de perfil, tela principal, gerenciamento de leitores e livros, pesquisa de leitores, catálogo de livros para leitores, registro e consulta de empréstimos, criação e população do banco de dados, definição dos relacionamentos entre entidades, proteção das informações sensíveis e elaboração da documentação técnica.
* **Fora do Escopo / Não Previsto:** Funcionalidades não previstas neste documento serão avaliadas conforme o tempo disponível e não poderão comprometer a entrega dos requisitos obrigatórios.

---

## 2. Perfis de Usuário e Controle de Acesso

O sistema possui dois perfis de usuário, cada um com permissões específicas de acordo com suas responsabilidades.

### 2.1. Técnico (bibliotecário)

Após a autenticação, o técnico tem acesso às funcionalidades administrativas:

* Cadastrar, consultar, atualizar e excluir registros de leitores, conforme as regras do sistema.
* Cadastrar, consultar, atualizar e excluir registros de livros.
* Registrar e consultar empréstimos, bem como os dados relacionados a leitores e livros.
* Encerrar sua sessão com segurança.

### 2.2. Usuário comum (leitor)

As permissões do leitor são limitadas às funcionalidades destinadas a ele:

* Consultar o catálogo de livros e pesquisar livros cadastrados (somente leitura).
* Consultar seus próprios empréstimos, quando essa funcionalidade estiver disponível e sua conta estiver vinculada ao seu cadastro de leitor.
* Encerrar sua sessão com segurança.

> **Observação:** O usuário comum não acessa funções administrativas nem visualiza informações pessoais ou empréstimos de outros leitores.

### 2.3. Controle de permissões

O sistema identifica o perfil do usuário autenticado e disponibiliza somente as funcionalidades autorizadas. A restrição é aplicada no back-end, e não apenas pela ocultação de botões ou menus na interface; assim, tentativas de acesso direto a funções administrativas por usuários comuns também são bloqueadas.

---

## 3. Requisitos Funcionais (RF)

Os requisitos funcionais definem as funcionalidades, ações e comportamentos que o sistema deve executar.  
**Prioridades:** Alta (Obrigatório), Média (Importante), Baixa (Desejável).

| ID | Nome do Requisito | Descrição Detalhada | Prioridade |
| :--- | :--- | :--- | :--- |
| **RF-001** | Autenticação de usuário | Permitir o acesso ao sistema por meio de login com nome de usuário e senha. | Alta |
| **RF-002** | Validação de credenciais | Validar as credenciais informadas e exibir mensagem de erro em caso de falha, sem indicar qual dado está incorreto. | Alta |
| **RF-003** | Identificação de perfil | Identificar, durante a autenticação, o perfil do usuário (técnico ou leitor) e liberar somente as funcionalidades desse perfil. | Alta |
| **RF-004** | Sessão e encerramento | Manter a sessão autenticada durante o uso, permitir o encerramento manual (logout) e encerrá-la após o período de inatividade definido em RNF-004. | Alta |
| **RF-005** | Tela principal | Exibir a tela principal com o nome do usuário autenticado e o acesso às funcionalidades disponíveis ao seu perfil. | Média |
| **RF-006** | Gerenciar leitores | Cadastrar, consultar, atualizar e excluir registros de leitores. Função exclusiva do técnico. | Alta |
| **RF-007** | Pesquisar leitores | Buscar leitores por um termo informado pelo usuário e atualizar a listagem após a confirmação da pesquisa. | Alta |
| **RF-008** | Gerenciar livros | Cadastrar, consultar, atualizar e excluir registros de livros. Função exclusiva do técnico. | Alta |
| **RF-009** | Consultar catálogo de livros | Permitir ao usuário comum consultar e pesquisar os livros cadastrados, sem possibilidade de alteração. | Média |
| **RF-010** | Registrar empréstimo | Cadastrar empréstimo associando obrigatoriamente um leitor cadastrado e um livro cadastrado. | Alta |
| **RF-011** | Listar empréstimos por data | Exibir a listagem de empréstimos ordenada por data, apresentando os dados do leitor e do livro associados. | Alta |
| **RF-012** | Consultar próprios empréstimos | Permitir ao leitor consultar somente os empréstimos vinculados ao seu cadastro. Condicionado à vinculação da conta ao cadastro de leitor. | Baixa |
| **RF-013** | Restrição de funções administrativas | Bloquear, no servidor, o acesso de usuários comuns às funções administrativas, inclusive por acesso direto. | Alta |

---

## 4. Requisitos Não-Funcionais (RNF)

Os requisitos não-funcionais definem qualidades, restrições e critérios de segurança, conformidade, integridade e manutenção.

| ID | Categoria | Descrição e Critério de Aceite | Prioridade |
| :--- | :--- | :--- | :--- |
| **RNF-001** | Segurança | As senhas devem ser armazenadas somente como hash criptográfico específico para senhas (ex.: `bcrypt` ou `Argon2`), nunca em texto puro.<br>**Critério:** Nenhuma senha legível no banco de dados. | Crítica |
| **RNF-002** | Segurança | Os dados sensíveis, como o CPF do leitor, devem ser protegidos por criptografia no banco de dados.<br>**Critério:** O CPF não é legível em consulta direta ao banco e é exibido de forma mascarada na interface. | Crítica |
| **RNF-003** | Conformidade | O sistema deve cumprir as diretrizes da LGPD: coletar somente os dados necessários ao funcionamento e restringir o acesso a dados pessoais aos perfis autorizados.<br>**Critério:** Um leitor não consegue acessar dados pessoais de outros leitores. | Crítica |
| **RNF-004** | Sessão | A sessão autenticada deve expirar após um período de inatividade (sugestão: 30 minutos, a confirmar pela equipe).<br>**Critério:** Após o período, nova ação exige novo login; uma sessão encerrada não pode ser reutilizada. | Alta |
| **RNF-005** | Autorização | As permissões devem ser verificadas pelo servidor em cada operação protegida.<br>**Critério:** Requisições sem permissão retornam erro de acesso negado, mesmo quando feitas diretamente. | Crítica |
| **RNF-006** | Integridade | O banco deve usar tipos de dados adequados, chaves primárias e chaves estrangeiras.<br>**Critério:** Não é possível inserir um empréstimo com leitor ou livro inexistente. | Alta |
| **RNF-007** | Manutenibilidade | O código-fonte e a documentação devem ser organizados para facilitar a manutenção futura.<br>**Critério:** Documentação técnica atualizada ao final de cada entrega. | Média |

---

## 5. Regras de Negócio (RN)

* **RN-001:** O acesso às funcionalidades protegidas depende de autenticação válida.
* **RN-002:** Todo usuário possui um perfil de acesso definido: técnico (bibliotecário) ou leitor.
* **RN-003:** As funções administrativas (gerenciamento de leitores, livros e empréstimos) são exclusivas do técnico.
* **RN-004:** Todo novo empréstimo deve estar relacionado a um leitor cadastrado e a um livro cadastrado.
* **RN-005:** A listagem de empréstimos é ordenada por data e apresenta as informações do leitor e do livro associados.
* **RN-006:** Quando a consulta de empréstimos pelo leitor for implementada, os resultados devem se limitar aos empréstimos vinculados ao seu cadastro.
* **RN-007:** Uma conta do tipo leitor pode ser vinculada ao respectivo cadastro de leitor, o que permite identificar os registros de cada leitor autenticado.
* **RN-008:** As permissões são verificadas pelo servidor em cada operação protegida.
* **RN-009:** O script do banco de dados deve criar e popular cada tabela com pelo menos três registros.

---

## 6. Modelagem do Banco de Dados

### 6.1. Dicionário de Entidades

| Entidade | Finalidade | Atributos Principais | Relacionamento |
| :--- | :--- | :--- | :--- |
| **USUARIO** | Dados de autenticação e perfil de acesso. | `id_usuario` (PK), `nome_usuario` (único), `senha_hash`, `perfil` (bibliotecário ou leitor), `id_leitor` (FK, opcional e único) | 0..1 com **LEITORES** |
| **LEITORES** | Dados cadastrais das pessoas atendidas. | `id_leitor` (PK), `nome`, `cpf` (criptografado), `email`, `telefone`, `data_cadastro` | 1 para N com **EMPRESTIMO** |
| **LIVROS** | Informações das obras cadastradas. | `id_livro` (PK), `titulo`, `autor`, `editora`, `ano_publicacao`, `isbn` | 1 para N com **EMPRESTIMO** |
| **EMPRESTIMO** | Registro das operações de empréstimo. | `id_emprestimo` (PK), `id_leitor` (FK), `id_livro` (FK), `data_emprestimo`, `data_devolucao_prevista`, `data_devolucao` | N para 1 com **LEITORES** e **LIVROS** |

### 6.2. Diagrama Entidade-Relacionamento (DER)

Baseado na modelagem lógica extraída do arquivo de diagrama:

```
+------------------+             +--------------------------+
|     USUARIO      |             |         LEITORES         |
+------------------+             +--------------------------+
| PK id_usuario    |             | PK id_leitor             |
|    nome_usuario  |             |    nome                  |
|    senha_hash    | (0..1)  (1) |    cpf                   |
|    perfil        |------------>|    email                 |
| FK id_leitor     |             |    telefone              |
+------------------+             |    data_cadastro         |
                                 +--------------------------+
                                              | (1)
                                              |
                                              | (N)
+------------------+             +--------------------------+
|      LIVROS      |             |        EMPRESTIMO        |
+------------------+             +--------------------------+
| PK id_livro      | (1)     (N) | PK id_emprestimo         |
|    titulo        |------------>| FK id_leitor             |
|    autor         |             | FK id_livro              |
|    editora       |             |    data_emprestimo       |
|    ano_publicacao|             |    data_devolucao_prevista|
|    isbn          |             |    data_devolucao        |
+------------------+             +--------------------------+
```

---

## 7. Stack Tecnológica e Arquitetura

| Camada | Tecnologia | Finalidade |
| :--- | :--- | :--- |
| **Front-end** | HTML5 | Estruturar as páginas do sistema. |
| **Front-end** | CSS3 | Definir a apresentação visual e o layout. |
| **Front-end** | JavaScript | Implementar interações na interface. |
| **Back-end** | Python 3 | Desenvolver as regras de negócio e o processamento no servidor. |
| **Back-end** | Flask | Gerenciar as rotas e integrar a interface ao back-end. |
| **Banco de dados** | MySQL / MariaDB | Armazenar os dados e os relacionamentos entre as tabelas. |
| **Linguagem BD** | SQL | Criar, consultar e manipular os dados. |
| **Modelagem** | Draw.io / MySQL Workbench | Modelar e representar o diagrama entidade-relacionamento. |

---

## 8. Plano de Testes

Os testes verificam os critérios de aceite dos requisitos. Os resultados serão registrados após a implementação de cada funcionalidade.

| Teste | Requisitos Relacionados |
| :--- | :--- |
| Autenticação com credenciais válidas e inválidas | RF-001, RF-002 |
| Identificação de perfil e bloqueio de funções administrativas, inclusive por acesso direto | RF-003, RF-013, RNF-005 |
| Expiração e encerramento da sessão | RF-004, RNF-004 |
| Cadastro, consulta e atualização de leitores; busca de leitores | RF-006, RF-007 |
| Cadastro e consulta de livros; catálogo para o leitor | RF-008, RF-009 |
| Cadastro de empréstimos com leitor e livro associados | RF-010, RN-004 |
| Ordenação dos empréstimos por data, com dados de leitor e livro | RF-011, RN-005 |
| Integridade das chaves primárias e estrangeiras | RNF-006 |
| Proteção de senhas e de dados sensíveis | RNF-001, RNF-002, RNF-003 |
| Existência de pelo menos três registros em cada tabela | RN-009 |

---

## 9. Considerações Finais

Este documento estabelece a base para o desenvolvimento do sistema, com requisitos priorizados, critérios de aceite verificáveis e uma proposta inicial de modelagem de dados. Essa definição antecipada orienta a implementação e reduz inconsistências ao longo do desenvolvimento.

Após a implementação, o documento deverá ser revisado para incluir o diagrama entidade-relacionamento final, a configuração do ambiente e os resultados dos testes realizados.
