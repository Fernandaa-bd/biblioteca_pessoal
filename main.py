"""
Sistema de Biblioteca Pessoal.

Responsável pelo menu principal e pela interação do usuário com as funcionalidades do sistema.
"""

from livro import Livro
from banco import cadastrar_livro, listar_livros, buscar_livro
from time import sleep
from estatisticas import menu_estatisticas

def cadastrar_novo_livro():

    # Solicita os dados do livro e realiza seu cadastro no banco de dados.
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    ano_leitura = int(input('Digite o ano em que você leu: '))
    nota = float(input('Digite a nota do livro(0 a 5): '))
    comentario = input('Digite um comentário/resenha sobre o livro: ')

    livro = Livro(
        titulo,
        autor,
        genero,
        ano_leitura,
        nota,
        comentario
    )

    cadastrar_livro(livro)

def mostrar_livros():
    # Busca e exibe todos os livros cadastrados.
    livros = listar_livros()

    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Gênero: {livro[3]}")
        print(f"Ano da leitura: {livro[4]}")
        print(f"Nota(0 a 5): {livro[5]}")
        print(f"Comentário: {livro[6]}")
        print("-" * 30)

def buscar_livro_titulo():
    #Solicita um título ao usuário e exibe o livro encontrado.
    titulo = input('Digite o título do livro que deseja buscar: ')

    livro = buscar_livro(titulo)

    if livro:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Gênero: {livro[3]}")
        print(f"Ano da leitura: {livro[4]}")
        print(f"Nota(0 a 5): {livro[5]}")
        print(f"Comentário: {livro[6]}")

    else:
        print('Livro não encontrado!')

def menu():
    #Exibe o menu principal e controla a navegação do sistema.
    while True:
        print('------ SUA BIBLIOTECA ------')
        print('''Suas opções:
\033[32m1 - Cadastrar Livro\033[m
\033[33m2 - Buscar Livro\033[m
\033[34m3 - Listar Livros\033[m
\033[35m4 - Estatísticas\033[m
\033[31m5 - Encerrar programa\033[m
''')
        try:
            opcao = int(input('Escolha uma opção: '))
            sleep(0.5)

            if opcao == 1:
                cadastrar_novo_livro()
            elif opcao == 2:
                buscar_livro_titulo()
            elif opcao == 3:
                mostrar_livros()
            elif opcao == 4:
                menu_estatisticas()
            elif opcao == 5:
                print('Programa encerrado!')
                break
            else:
                print('Escolha uma opção VÁLIDA!')

        except: 
            print('Escolha uma opção VÁLIDA!')

menu()