#print("hello, world!")
#0(inporta ou manda o sqllite3 e apilida (nenomea)para facilitar no codigo)
import sqlite3 as sql


def criar_banco_dados():
    # 1. Conecta ao banco de dados (certifique-se de salvar o arquivo no lugar certo)
    conexao = sql.connect("banco.db")
    cursor = conexao.cursor()
    print("banco de dados conctado")

    cursor.execute("PRAGMA foreign_Key = ON;")

    cursor.execute("""
            CREATE TABLE livro(
                id_livro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                editora TEXT,
                isbn TEXT UNIQUE,
                ano_publicacao DATE NOT NULL,
                edicao INTEGER
    )""")

    cursor.execute("""CREATE TABLE aluno(
                    id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    ) """)

    cursor.execute("""CREATE TABLE bibliotecario(
                    id_bibliotecario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    ) """)

    cursor.execute("""CREATE TABLE usuario(
                    martricula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_usuario TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    id_bibliotecario INTEGER,
                    id_aluno INTEGER,
                    FOREIGN KEY (id_bibliotecario)REFERENCES bibliotecario(id_bibliotecario) ON DELETE SET NULL,
                    FOREIGN KEY (id_aluno)REFERENCES aluno(id_aluno) ON DELETE SET NULL
                    ) """)
    
    cursor.execute("""CREATE TABLE emprestimo(
                    id_emprestimo INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
                    id_livro INTEGER,
                    id_aluno INTEGER,
                    data_emprestimo DATE,
                    data_devolucao DATE,
                    FOREIGN KEY (id_livro) REFERENCES livro(id_livro)ON DELETE SET NULL,
                    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)ON DELETE SET NULL
                    ) """)

    conexao.commit()
    conexao.close()
    print("banco de dados concluído!")

criar_banco_dados()