# 📚 Sua Biblioteca

Sistema de gerenciamento de uma biblioteca pessoal desenvolvido em Python.

## Sobre o projeto

O projeto permite cadastrar e consultar livros já lidos, armazenando informações como título, autor, gênero, ano da leitura, nota e comentário.

Os dados são armazenados em um banco de dados SQLite e o sistema também possui uma área de estatísticas com gráficos.

## Tecnologias utilizadas

- Python
- SQLite
- Matplotlib
- Seaborn

## Funcionalidades

- Cadastro de livros
- Listagem de livros
- Busca de livros por título
- Armazenamento dos dados em SQLite
- Estatísticas da biblioteca
- Gráfico de livros por ano
- Gráfico de livros por gênero
- Gráfico de livros por autor

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o sistema

```bash
python main.py
```

## Banco de dados

O projeto utiliza SQLite para armazenar os dados dos livros.

O arquivo `biblioteca.db` é criado localmente e não é enviado ao GitHub, pois contém os dados pessoais cadastrados na biblioteca.