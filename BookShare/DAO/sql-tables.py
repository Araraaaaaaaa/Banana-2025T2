import sqlite3

class Database:
    conn = None
    nome_bd="agenda.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def criar_tabelas(cls):
        # --------------------- Tabela Usuario ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                email TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                idade INTEGER DEFAULT 17 CHECK( idade >=17 ),
                senha TEXT NOT NULL
            );
        """)

        # --------------------- Tabela Exemplar ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS exemplar (
                id_exemplar INTEGER PRIMARY KEY AUTOINCREMENT,
                email_usuario TEXT NOT NULL,
                id_livro INTEGER NOT NULL,
                status_emprestim TEXT NOT NULL,
                FOREIGN KEY (email_cliente) REFERENCES cliente(email) ON DELETE CASCADE,
               FOREIGN KEY (id_livro) REFERENCES livro(id_livro) ON DELETE CASCADE,
            );
        """)

        # --------------------- Tabela Livro ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS livro (
                id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                paginas INTEGER NOT NULL,
                capa TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL
            );
        """)

if _name_ == "_main_":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()