# 🏦 Desafio: Otimizando o Sistema Bancário com Funções Python

![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg) ![Status](https://img.shields.io/badge/Status-Completed-green) ![Bootcamp](https://img.shields.io/badge/Bootcamp-NTT%20DATA-orange) ![DIO](https://img.shields.io/badge/Powered%20by-DIO-yellow)

Bem-vindo ao **Sistema Bancário com Python**! Este projeto é uma simulação de um sistema bancário que permite realizar operações básicas e avançadas como **Depósito**, **Saque**, **Extrato**, **Cadastro de Clientes** e **Criação de Contas Correntes**.

## 📋 Funcionalidades

- 📥 **Depósito:** Permite adicionar saldo à conta.
- 💸 **Saque:** Realize saques respeitando limites diários e saldo disponível.
- 📜 **Extrato:** Resumo de todas as transações realizadas.
- 👤 **Cadastro de Clientes:** Crie novos clientes no sistema.
- 🏦 **Criação de Contas Correntes:** Crie e associe contas correntes aos clientes.
- 📄 **Listar Contas:** Visualize todas as contas registradas.
- ❌ **Saída:** Encerre a operação do sistema.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+** 🐍
  - `Funções` personalizadas para cada operação
  - Parâmetros e Argumentos por posição e nomeados (keywords) -> ` /, *`
  - Controle de fluxo com `while` e condicionais `if-elif-else`
  - Manipulação de `listas` e `dicionários`
  - Interação via `input()` e `print()`
  - Conversão de Tipo de dados -> `Type casting` 


## 🎯 Objetivo

Este projeto tem o objetivo de praticar conceitos fundamentais de programação Python como funções, loops, condicionais, e manipulação de dados, seguindo boas práticas de organização de código. Desenvolvido como parte do **exercício prático** do Bootcamp NTT DATA - Engenharia de Dados com Python da DIO.

## 🛠️ Como Executar

1. Certifique-se de ter o **Python 3.12+** instalado em sua máquina.

2. Clone o repositório:
    ```bash
    git clone https://github.com/josealexandre87/otimizando-controle-bancario-python.git
    ```

3. Acesse a pasta do projeto:
    ```bash
    cd otimizando-controle-bancario-python
    ```

4. Execute o script:
    ```bash
    python sistema_bancario_com_python_otimizado.py
    ```

## 🎉 Exemplo de Execução

```bash
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Cadastrar Novo Cliente
[cc] Criar Conta Corrente
[lc] Lista de Contas
[q] Sair

=> nc
Informe o CPF (somente número): 12345678910
Informe o nome completo: Edward Eric
Informe a data de nascimento (dd-mm-aaaa): 03-10-1867
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ...
=== Cliente criado com sucesso! ===

=> d
Informe o valor do depósito: 100
Depósito: R$ 100.00

=> e
================ EXTRATO ================
Depósito: R$ 100.00
Saldo: R$ 100.00
=========================================
```
