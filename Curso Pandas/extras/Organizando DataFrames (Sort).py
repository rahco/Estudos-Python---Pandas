#!/usr/bin/env python
# coding: utf-8

import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data

list('321')

df = pd.DataFrame(data, list('321'), list('ZYX'))
df

# comando .sort_index organiza o df através do index
df.sort_index(inplace = True)

df

# comando .sort_index junto ao axis = 1 organiza o df tanto para as linhas como para as colunas
df.sort_index(inplace = True, axis = 1)

df

# comando .sort_values organiza o DF a partir de uma coluna ou grupo de colunas
df.sort_values(by = 'X', inplace = True)
df

# comando .sort_values com axis = 1 organiza o DF a partir de uma linha ou grupo de linhas
df.sort_values(by = '3', axis = 1, inplace = True)
df

# comando .sort_values organiza o DF a partir de uma coluna ou grupo de colunas
df.sort_values(by = ['X','Y'], inplace = True)
df

