#!/usr/bin/env python
# coding: utf-8

import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

s

s.fillna(0)

s

# utilizando o method ffill junto a o comando .fillna, é preenchido no lugar de um item null o primeiro valor acima dele notnull
s.fillna(method = 'ffill')

# utilizando o method bfill é preenchido no lugar de um item null o primeiro valor abaixo dele notnull
s.fillna(method = 'bfill')

# modelo para adicionar aos valores null a média dos valores notnull no df
s.fillna(s.mean())

s

# utilizando o parâmetro limit o ffill irá preencher apenas um valor determinado de null por recorrência
s.fillna(method = 'ffill', limit = 1)

s1 = s.fillna(method = 'ffill', limit = 1)
s1

# utilizando a combinação de métodos com variáveis é possível adicionar um valor de cima e um abaixo
s1.fillna(method = 'bfill', limit = 1)

atletas = pd.DataFrame([['Marcos', 9.62], ['Pedro', None], ['João', 9.69], 
                        ['Beto', 9.72], ['Sandro', None], ['Denis', 9.69], 
                        ['Ary', None], ['Carlos', 9.74]], 
                        columns = ['Corredor', 'Melhor Tempo'])
atletas

