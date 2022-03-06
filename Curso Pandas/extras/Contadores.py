#!/usr/bin/env python
# coding: utf-8

import pandas as pd

s = pd.Series(list('asdadeadesdasesda'))
s

# com o comando .unique podemos ver os valores únicos contidos em uma series
s.unique()

# com o comando .value_counts temos uma contagem de quantas vezes um item está repedito em uma series
s.value_counts()

dados = pd.read_csv('dados/aluguel.csv', sep = ';')

dados.head(10)

# com o comando .unique indicado a coluna a ser verificada temos os valores únicos na series
dados.Tipo.unique()

# com o comando .value_counts e setagem da series a ser verificada temos o resultado do contador
dados.Tipo.value_counts()

# ## Exercício - Contadores

m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

# Montar um df com os resultados dos lançamentos por moeda
eventos = {'m1': list(m1), 
            'm2': list(m2), 
            'm3': list(m3), 
            'm4': list(m4), 
            'm5': list(m5)}
moedas = pd.DataFrame(eventos)
df = pd.DataFrame(data = ['Cara', 'Coroa'], 
                    index = ['c', 'C'], 
                    columns = ['Faces'])
for item in moedas:
    df = pd.concat([df, moedas[item].value_counts()], 
                    axis = 1)
df

