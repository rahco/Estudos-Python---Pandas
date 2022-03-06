#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# # Series

data = [1, 2, 3, 4, 5]

s = pd.Series(data)

s

index = ['Linha' + str(i) for i in range(5)]

index

# comando alterando o idex da series por um range com string através de uma lista
s = pd.Series(data = data,index = index)

s

data = {'Linha' + str(i) : i + 1 for i in range(5)}

data

# comando alterando o idex da series por um range com string através de um dicionário
s = pd.Series(data)
s

s1 = s + 2

s1

# fazendo operações com 2 df
s2 = s + s1
s2


# # Data Frame

data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

data

df1 = pd.DataFrame(data = data)

df1

# definindo o nome das linhas
index = ['Linha' + str(i) for i in range(3)]
index

index

df1 = pd.DataFrame(data = data, index = index)
df1

# definindo o nome das colunas
columns = ['Coluna' + str(i) for i in range(3)]
columns

# forma padrão de definir os nomes das linhas e colunas em um df
df1 = pd.DataFrame(data = data, index = index, columns = columns)
df1

data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}
data

# outra forma de definir os nomes das linhas e colunas é através d eum conjunto de pares de dicionários
df2 = pd.DataFrame(data)
df2

data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)]

data

# df criado com tuplas
df3 = pd.DataFrame(data = data, index = index, columns = columns)
df3

df1[df1 > 0] = 'A'
df1

df2[df2 > 0] = 'B'
df2

df3[df3 > 0] = 'C'
df3

# concatenamento de df através de colunas
df4 = pd.concat([df1, df2, df3])
df4

# concatenamento de df através de linhas
df4 = pd.concat([df1, df2, df3], axis = 1)
df4

