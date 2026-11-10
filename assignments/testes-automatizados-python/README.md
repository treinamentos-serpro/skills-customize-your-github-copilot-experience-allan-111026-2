# 📘 Atividade: Testes Automatizados com pytest

## 🎯 Objetivo

Pratique como escrever e executar testes automatizados para funções em Python usando `pytest`. Você vai testar resultados esperados e casos-limite para encontrar erros com confiança.

## 📝 Tarefas

### 🛠️ Escrever o Primeiro Teste

#### Descrição
Crie o arquivo `calculator.py` com uma função `add(a, b)` e o arquivo `test_calculator.py` com seu primeiro teste automatizado.

#### Requisitos
O programa concluído deve:

- Fazer `add(a, b)` retornar a soma dos dois números.
- Incluir em `test_calculator.py` uma função de teste cujo nome comece com `test_` e que use `assert` para verificar `add(2, 3) == 5`.
- Instalar `pytest` com `python -m pip install pytest` e executar os testes com `python -m pytest -v`.

### 🛠️ Testar Números Pares e Ímpares

#### Descrição
Adicione a função `is_even(number)` ao arquivo `calculator.py` e escreva testes para verificar seu resultado com diferentes números.

#### Requisitos
O programa concluído deve:

- Fazer `is_even(number)` retornar `True` quando o número for par e `False` quando for ímpar.
- Verificar pelo menos o zero, um número par positivo, um número ímpar positivo e um número negativo ímpar.
- Manter os testes organizados em funções com nomes que começam com `test_`.

### 🛠️ Verificar uma Média e um Caso-Limite

#### Descrição
Adicione a função `average(numbers)` e teste tanto uma lista com valores quanto uma lista vazia. Para esta atividade, a função deve retornar `None` quando receber uma lista vazia.

#### Requisitos
O programa concluído deve:

- Fazer `average(numbers)` retornar a média aritmética dos valores da lista.
- Verificar que `average([2, 4, 6])` retorna `4` e que uma lista com um único valor retorna esse valor.
- Verificar que `average([])` retorna `None`.
- Executar a suíte completa com `python -m pytest -v` e confirmar que todos os testes passam.