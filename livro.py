"""
Define a classe Livro e suas informações.
"""

class Livro:
    def __init__(self, titulo, autor, genero, ano_leitura, nota, comentario):

        # Inicializa um livro com seus dados de cadastro.
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_leitura = ano_leitura
        self.nota = nota
        self.comentario = comentario

    def exibir_informacoes(self):
        #Exibe as informações do livro no terminal.

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Gênero: {self.genero}")
        print(f'Ano da leitura: {self.ano_leitura}')
        print(f'Nota: {self.nota}')
        print(f'Comentário: {self.comentario}')