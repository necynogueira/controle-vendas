# Sistema de Gestão de Produtos e Vendas

Este sistema em Django permite a gestão de produtos e vendas. Ele oferece funcionalidades para listar, criar, editar, excluir produtos, além de registrar vendas e gerar relatórios de vendas e estoque. A URL principal do sistema é `http://localhost:8000/`.

## Endpoints Disponíveis

### 1. Listar Produtos
- **URL:** `/vendas/produtos/`
- **Método:** GET
- **Descrição:** Exibe uma lista de todos os produtos cadastrados.
- **Como usar:** Acesse `http://localhost:8000/vendas/produtos/` no navegador.

### 2. Criar um Novo Produto
- **URL:** `/vendas/produtos/novo/`
- **Método:** GET e POST
- **Descrição:** Permite criar um novo produto no sistema.
- **Como usar:** 
  - Acesse `http://localhost:8000/vendas/produtos/novo/` para visualizar o formulário de criação de produto.
  - Preencha o formulário e envie-o para criar o produto.

### 3. Editar um Produto Existente
- **URL:** `/vendas/produtos/editar/<int:id>/`
- **Método:** GET e POST
- **Descrição:** Permite editar as informações de um produto existente.
- **Como usar:** 
  - Substitua `<int:id>` pelo ID do produto que deseja editar.
  - Acesse `http://localhost:8000/vendas/produtos/editar/1/` para editar o produto com ID 1, por exemplo.

### 4. Excluir um Produto
- **URL:** `/vendas/produtos/excluir/<int:id>/`
- **Método:** GET e POST
- **Descrição:** Exibe uma confirmação e permite excluir um produto.
- **Como usar:** 
  - Substitua `<int:id>` pelo ID do produto que deseja excluir.
  - Acesse `http://localhost:8000/vendas/produtos/excluir/1/` para excluir o produto com ID 1, por exemplo.

### 5. Registrar Venda
- **URL:** `/vendas/registrar-venda/`
- **Método:** GET e POST
- **Descrição:** Permite registrar uma nova venda de um produto, atualizando o estoque do produto vendido.
- **Como usar:** Acesse `http://localhost:8000/vendas/registrar-venda/` para registrar uma nova venda.

### 6. Gerar Relatório de Vendas (CSV)
- **URL:** `/vendas/relatorio-vendas/`
- **Método:** GET
- **Descrição:** Gera e faz o download de um arquivo CSV com as vendas registradas no sistema.
- **Como usar:** Acesse `http://localhost:8000/vendas/relatorio-vendas/` para baixar o relatório de vendas.

### 7. Gerar Relatório de Estoque (TXT)
- **URL:** `/vendas/relatorio-estoque/`
- **Método:** GET
- **Descrição:** Gera e faz o download de um arquivo de texto contendo a lista de produtos e suas quantidades em estoque.
- **Como usar:** Acesse `http://localhost:8000/vendas/relatorio-estoque/` para baixar o relatório de estoque.

## Requisitos para Executar o Sistema

- Django 3.x ou superior
- Pandas (para geração de relatórios CSV)
- Python 3.x
- Banco de dados configurado e migrado (PostgreSQL)

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/necynogueira/controle-vendas.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Realize as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
4. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
5. Acesse o sistema em `http://localhost:8000/`.

# Se preferir, você pode subir o projeto com o Dev Container.

Este guia explica como configurar e usar um Dev Container no Visual Studio Code (VS Code) para subir seu projeto no ambiente local.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/) (necessário para rodar containers)
- Extensão **Dev Containers** no VS Code

## Passos para Usar o Dev Container

1. **Instale a Extensão Dev Containers**  
   No VS Code, vá para o Marketplace de extensões e instale a extensão **Dev Containers**.

2. **Abra o Projeto no VS Code**  
   Navegue até o diretório do seu projeto e abra-o no VS Code.

3. **Abra o Projeto no Dev Container**  
   Pressione `F1` no VS Code para abrir o painel de comandos e selecione a opção **Dev Containers: Reopen in Container**. O VS Code abrirá o projeto dentro de um Dev Container, onde você terá um ambiente de desenvolvimento isolado e configurado conforme definido no arquivo `devcontainer.json`.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o sistema.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
