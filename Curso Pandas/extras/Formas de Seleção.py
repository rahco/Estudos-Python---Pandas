#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# comando .split() pode ser utilizado para criar listas com str
'l1 l2 l3 l4'.split()

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())

df

df['c1']

type(df['c1'])

# utilizando colchetes duples e separando por vírgulas podemos selecionar mais de uma coluna
df[['c3', 'c1']]

type(df[['c3', 'c1']])

# para selecionar todas as linhas inserimos :
df[:]

# para selecionar a partir de uma linha e todas abaixo utilizamos index_linha:
df[1:]

# para selecionar um intervalo de linhas definimos index_inicial:idex_final+1
df[1:3]

# para selecionar linhas e colunas colocamos os filtros de colchetes em sequência sendo linhas>colunas
df[1:][['c3', 'c1']]

df

# com o comando .loc podemos fazer os mesmo filtros, porém utilizando os rótulos/nomes das linhas
df.loc['l3']

df.loc[['l3', 'l2']]

# com o .loc podemos também puxar valores de dentro de um df defindo sua localização pelo inxex e coluna
df.loc['l1', 'c2']

# com o .iloc utilizamos os índeces tanto das linhas como das colunas para localizar informações o DF
df.iloc[0,1]

# com o .loc podemos tb remontar o df selecionando colunas e linhas específicas
df.loc[['l3','l1'],['c4','c1']]

# o mesmo filtro feito com o .iloc
df.iloc[[2, 0],[3, 0]]

