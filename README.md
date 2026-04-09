# Inventário de livros - Back-end
Este repositório contém o back-end de uma Single Page Application (SPA) desenvolvida como parte do MVP para a disciplina de Desenvolvimento Full Stack Básico. A aplicação provê os endpoints para o usuário interagir com a base de dados e manipular suas informações. com uma API Python/Flask para gerenciar um inventário pessoal de livros.

# Tecnologias Utilizadas

- Python (linguagem)
- Flask (framework)
- SQLite (banco de dados)
- OpenAPI / Swagger (documentação)

# Como Executar o Projeto
Para rodar a a API e subir o banco de dados, siga os passos abaixo:

1. Clonar o repositório e navegar para a o diretório raiz do projeto:

git clone https://github.com/vinicius-lamberti/back-basico-puc1.git && cd back-basico-puc1

2. Criar e ativar o ambiente virtual do Python:

python3 -m venv venv && source ./venv/bin/activate

3. Instalar as dependências do projeto no ambiente virtual:

pip install -r requirements.txt

4. Executar o projeto com o comando:

python3 -m flask run --host 0.0.0.0 --port 5000

# Como acessar a documentação
Através da url: http://127.0.0.1:5000/openapi/swagger#/