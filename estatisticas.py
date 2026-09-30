"""
Funções responsáveis pelo menu de estatísticas
e pela geração dos gráficos da biblioteca.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from banco import quantidade_livros_por_ano, quantidade_livros_por_genero, quantidade_livros_por_autor
from time import sleep 

sns.set(style='whitegrid')

def menu_estatisticas():
    #Exibe o menu de estatísticas e permite escolher o gráfico.
    while True:
            sleep(0.5)
            print('------ ESTATÍSTICAS ------')
            print('''Suas opções:
    \033[32m1 - Quantidade de Livros por ano\033[m
    \033[33m2 - Quantidade de Livros por gênero\033[m
    \033[34m3 - Quantidade de Livros por autor\033[m
    \033[31m4 - Voltar\033[m
    ''')
            try:
                opcao = int(input('Escolha uma opção: '))
                sleep(0.5)
    
                if opcao == 1:
                    grafico_livros_por_ano()
                elif opcao == 2:
                    grafico_livros_por_genero()
                    
                elif opcao == 3:
                    grafico_livros_por_autor()
                elif opcao == 4:
                    break
                else:
                    print('Escolha uma opção VÁLIDA!')
    
            except: 
                print('Escolha uma opção VÁLIDA!')

def grafico_livros_por_ano():
    #Gera um gráfico com a quantidade de livros lidos por ano.
    livros = quantidade_livros_por_ano()

    anos = []
    quantidades = []

    for ano, quantidade in livros:
        anos.append(ano)
        quantidades.append(quantidade)

    sns.barplot(x = anos, y = quantidades, palette='Set2')
    plt.xlabel('ANOS')
    plt.ylabel('Quantidade de livros')
    plt.show()

def grafico_livros_por_genero():
    #Gera um gráfico com a quantidade de livros por gênero.
    livros = quantidade_livros_por_genero()

    quantidades = []
    generos = []

    for genero, quantidade in livros:
        generos.append(genero)
        quantidades.append(quantidade)

    sns.barplot(x = generos, y = quantidades, palette='Set1')
    plt.xlabel('Gêneros')
    plt.ylabel('Quantidade de livros')
    plt.show()

def grafico_livros_por_autor():
    #Gera um gráfico com a quantidade de livros por autor.
    livros = quantidade_livros_por_autor()

    quantidades = []
    autores = []

    for autor, quantidade in livros:
        autores.append(autor)
        quantidades.append(quantidade)

    plt.figure(figsize = (8, 5))
    sns.barplot(x = autores, y = quantidades, palette='Set1')
    plt.xticks(fontsize = 9)
    plt.xlabel('Autores')
    plt.ylabel('Quantidade de livros')
    plt.tick_params(axis='x', rotation=25)
    plt.show()