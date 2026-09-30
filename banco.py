"""
Funções responsáveis pela conexão e pelo gerenciamento do banco de dados SQLite da biblioteca.
"""

import sqlite3

def conectar_banco():
    #Cria a conexão com o banco de dados e retorna a conexão e o cursor.
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    return conexao, cursor

def criar_tabela():
    #Cria a tabela de livros caso ela ainda não exista.
    conexao, cursor = conectar_banco()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT NOT NULL,
        genero TEXT NOT NULL,
        ano_leitura INTEGER NOT NULL,
        nota REAL,
        comentario TEXT
        )
""")
    
    conexao.commit()
    conexao.close()

def cadastrar_livro(livro):
    #Insere um novo livro no banco de dados.
    conexao, cursor = conectar_banco()

    cursor.execute('''
        INSERT INTO livros (titulo, autor, genero, ano_leitura, nota, comentario)
        VALUES (?, ?, ?, ?, ?, ?)
''', (
    livro.titulo,
    livro.autor,
    livro.genero,
    livro.ano_leitura,
    livro.nota,
    livro.comentario
))
    conexao.commit()
    conexao.close()

def listar_livros():
    #Retorna todos os livros cadastrados.
    conexao, cursor = conectar_banco()

    cursor.execute('''
        SELECT * FROM livros
''')

    livros = cursor.fetchall()

    conexao.close()

    return livros

def buscar_livro(titulo):
    #Busca um livro pelo título informado.
    conexao, cursor = conectar_banco()

    cursor.execute('''
        SELECT * FROM livros
        WHERE LOWER(titulo) = LOWER(?)
''', (titulo,))

    livro = cursor.fetchone()

    conexao.close()

    return livro

def quantidade_livros_por_ano():
    #etorna a quantidade de livros lidos em cada ano.
    conexao, cursor = conectar_banco()

    cursor.execute('''
        SELECT ano_leitura, COUNT(*)
        FROM livros
        GROUP BY ano_leitura
''')

    livros = cursor.fetchall()

    conexao.close()

    return livros

def quantidade_livros_por_genero():
    #Retorna a quantidade de livros agrupados por gênero.
    conexao, cursor = conectar_banco()

    cursor.execute('''
        SELECT genero, COUNT(*)
        FROM livros
        GROUP BY genero
''')

    livros = cursor.fetchall()
    conexao.close()

    return livros

def quantidade_livros_por_autor():
    #Retorna a quantidade de livros agrupados por autor.
    conexao, cursor = conectar_banco()

    cursor.execute('''
        SELECT autor, COUNT(*)
        FROM livros
        GROUP BY autor
''')

    livros = cursor.fetchall()
    conexao.close()

    return livros

criar_tabela()