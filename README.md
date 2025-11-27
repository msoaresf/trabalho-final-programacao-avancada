# trabalho-final-programacao-avancada

Sistema de Controle de Estoque e Vendas: Maria Eduarda Soares e Leticia Azambuja

Este projeto implementa um sistema completo de gestão de estoque e registro de vendas, com foco na persistência de dados (usando pickle) e na análise estatística de vendas utilizando a biblioteca NumPy.

O sistema é executado através de um menu interativo, permitindo ao usuário realizar operações de controle de estoque e registro de vendas.

## Funcionalidades Principais

O sistema é iniciado através do arquivo "Programa_principal.py" e apresenta um menu principal com duas áreas: Estoque e Vendas.

### Menu Principal

* 1 - Gerenciamento de Estoque
* 2 - Sistema de Vendas 
* 0 - Sair 

### 1. Gerenciamento de Estoque

* 1 - Cadastrar produto 
* 2 - Listar produtos cadastrados 
* 3 - Editar produto 
* 4 - Excluir produto 
* 5 - Gerar relatório 
* 0 - Voltar ao menu principal 

### 2. Sistema de Vendas


* 1 - Realizar Venda (inclui listagem de produtos) 
* 2 - Listar Vendas (Histórico) 
* 3 - Análise das vendas (NumPy) 
* 0 - Voltar ao menu principal 

## Análise de Dados com NumPy

A opção 3 - Análise das vendas executa a função analise() no sistemaVendas.py, que utiliza o NumPy para fazer uma analise geral dos lucros, como:

* Lucro Total Geral(`np.sum`).
* Média de Lucro por Item Vendido** (`np.mean`).
* Produto com Maior Lucro e Produto com Maior Quantidade Vendida (usando `np.max` e lógica de extração).
* Categoria Mais Lucrativa (usando `np.argmax`).

## Estrutura de Arquivos

O projeto é composto pelos seguintes arquivos Python:

| Arquivo | Descrição |
| :--- | :--- |
| `Programa_principal.py` | **Ponto de entrada do sistema.** Contém o menu principal. |
| `sistemaVendas.py` | Contém a classe `SistemaDeVendas`, responsável por gerenciar o carrinho, finalizar vendas e realizar a **Análise de Vendas (NumPy)**. Contém tambem a classe `Historico`, que define a estrutura de dados de cada venda registrada.|
| `Arquivar.py` | Contém a classe `ControleEstoque`, responsável por todas as operações de CRUD (Criar, Ler, Atualizar, Deletar) do estoque e persistência de dados (`estoque.pkl`). |
| `Produtos.py` | Contém a classe `Produto`, que define a estrutura de dados de cada item do estoque. |

## Requisitos

Para executar o projeto, você precisa ter o Python instalado e as bibliotecas "numpy" e "colorama".

```bash
pip install numpy
```
```bash
pip install colorama
```
OU 
```bash
pip install -r requirements.txt
```

## Como Executar

1.  Certifique-se de que todos os arquivos Python ("Programa_principal.py", "sistemaVendas.py", "Arquivar.py", "Produtos.py", "compras.py") estejam no mesmo diretório.
2.  Execute o arquivo principal:

```bash
python Programa_principal.py
```

3.  O menu interativo será exibido, e você poderá navegar entre as opções de Estoque e Vendas.

---
*Trabalho final de programação avançada, desenvolvid para fins de estudo e aplicação de conceitos de POO e Análise de Dados com NumPy.*
