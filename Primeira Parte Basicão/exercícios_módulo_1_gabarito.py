# -*- coding: utf-8 -*-
"""Exercícios Módulo 1 - Gabarito.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o_LaxQjtbqq5pXFqzjCFIgi0hPEHwF_h

# Exercícios do Módulo 1 - Operações, Variáveis e Input

### Parte 1 - Operações e Variáveis
Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 150<br>
Quantidade de Vendas de Pepsi = 130<br>
Preço Unitário da Coca = 1,50 <br>
Preço Unitário da Pepsi = 1,50 <br>
Custo da Loja: 2.500,00

Use o bloco abaixo para criar todas as variáveis que precisar.
"""

qtde_coca = 150
qtde_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo = 2500

"""1. Qual foi o faturamento de Pepsi da Loja?"""

print(qtde_pepsi * preco_pepsi)

"""2. Qual foi o faturamento de Coca da Loja?"""

print(qtde_coca * preco_coca)

"""3. Qual foi o Lucro da loja?"""

faturamento = qtde_coca * preco_coca + qtde_pepsi * preco_pepsi
lucro = faturamento - custo
print(lucro)

"""4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual"""

print(lucro / faturamento)

"""### Parte 2 - Inputs e Strings

A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
Ex: <br>
Coca -> Código: BEB1300543<br>
Pepsi -> Código: BEB1300545<br>
Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
Vodka Smirnoff -> Código: BAC17675002<br>

Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
"""

codigo = input("Qual é o código da bebida? (Insira tudo em letra maiúscula):")
print("BAC" in codigo)