# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construir uma API REST em Python com o framework FastAPI, criando rotas para ler, criar, atualizar e remover recursos, com validação automática de dados.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota

#### Descrição
Instale as dependências, abra o arquivo `starter-code.py` (salve-o como `main.py`) e crie a primeira rota da API. Depois, rode o servidor e acesse a rota no navegador.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `pip install fastapi uvicorn`
- Criar uma rota `GET /` que retorna um dicionário com a chave `"message"`
- Rodar o servidor com `uvicorn main:app --reload`
- Mostrar a resposta JSON ao acessar `http://127.0.0.1:8000/` no navegador

### 🛠️ Implementar Rotas de Leitura e Criação

#### Descrição
Use o modelo `Item` e o dicionário `items` do starter code para criar rotas que listam, buscam e cadastram itens.

#### Requisitos
O programa concluído deve:

- Criar a rota `POST /items` que recebe um `Item`, salva o item no dicionário com um novo `id` e retorna o item criado
- Criar a rota `GET /items` que retorna todos os itens cadastrados
- Criar a rota `GET /items/{item_id}` que retorna um item pelo `id`
- Gerar a documentação interativa automaticamente em `http://127.0.0.1:8000/docs`

### 🛠️ Atualizar, Remover e Tratar Erros

#### Descrição
Complete o CRUD da API. Quando um item não existir, a API deve responder com erro apropriado, em vez de quebrar.

#### Requisitos
O programa concluído deve:

- Criar a rota `PUT /items/{item_id}` que substitui os dados de um item existente
- Criar a rota `DELETE /items/{item_id}` que remove um item
- Retornar status `404` com `HTTPException` quando o `item_id` não existir, nas rotas de busca, atualização e remoção
- Rejeitar automaticamente um `price` com tipo inválido (por exemplo, texto), mostrando que a validação do Pydantic funciona
