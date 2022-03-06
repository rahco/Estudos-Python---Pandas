#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise I

# ## Importando a Base de Dados

import pandas as pd

# importando
pd.read_csv('dados/aluguel.csv', sep=';')

dados = pd.read_csv('dados/aluguel.csv', sep=';')

dados

type(dados)

dados.info()

dados.head(10)

# ## Informações gerais sobre a Base de Dados

dados.dtypes

# Transformando a saída em um DF para melhorar a visualização dos dados
pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])

tipo_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])

# comando para dar um tífulo a coluna inxex
tipo_de_dados.columns.name = 'Variáveis'

tipo_de_dados

dados.shape

dados.shape[0]

dados.shape[1]

print('A base de dados apresenta {} registros (imóveis) e {} variáveis'.format(dados.shape[0],dados.shape[1]))

# ## Exercício - Informações de um DataFrame

import pandas as pd
data = [['Fulano', 12, 7.0, True],
        ['Sicrano', 15, 3.5, False], 
        ['Beltrano', 18, 9.3, True]]
dt = pd.DataFrame(data, 
        columns = ['Aluno', 'Idade', 'Nota', 'Aprovado'])
dt

tipo_de_ds = pd.DataFrame(dt.dtypes, columns = ['Tipos de Dados'])
tipo_de_ds.columns.name = 'Variáveis'
tipo_de_ds

