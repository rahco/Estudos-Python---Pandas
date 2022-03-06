#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VII

# ## Criando Agrupamentos

import pandas as pd

dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')

dados.head(10)

# comando .mean para verificar a média de uma variávei
dados['Valor'].mean()

bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]

dados['Bairro'].drop_duplicates()

# o comando .groupby serve para agrupar os dados de um df baseado em alguma variável
grupo_bairro = dados.groupby('Bairro')

type(grupo_bairro)

# como resultado ao .groupby temos um dicionário sendo a chave a variável selecionada e o retorno os index onde se tem a info
grupo_bairro.groups

for bairro, data in grupo_bairro:
    print('{} -> {}'.format(bairro, data.Valor.mean()))

grupo_bairro['Valor'].mean()

grupo_bairro[['Valor', 'Condominio']].mean().round(2)

# # Estatísticas Descritivas

# o comando .describe retorna de forma direta alguns indicadores descritivos sobre a variável informada
grupo_bairro['Valor'].describe().round(2)

# outra forma de se obter indicadores descritivos é com o comando .aggregate definindo os indicadores a serem apurados
grupo_bairro['Valor'].aggregate(['min', 'max']).rename(columns = {'min' : 'Mínimo', 'max' : 'Máximo'})

# comando para import do matplotlib para gerar gráficos no console
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20, 10))

fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})

fig = grupo_bairro['Valor'].max().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})

