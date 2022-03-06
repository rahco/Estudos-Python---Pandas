#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise V

# ## Tratamento de Dados Faltantes

import pandas as pd

dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')

dados.head(10)

# comando .isnull() gera um df bool indicando se o dados é null
dados.isnull()

# comando .isnull() gera um df bool indicando se o dados não é null
dados.notnull()

# .info gera um conjunto de informações sobre o df que apoia a verificação de quais colunas possuem dados null
dados.info()

# utilizando .isnull para filtrar campos nulos de uma determinada coluna
dados[dados['Valor'].isnull()]

# com o comando .dropna e definindo a coluna referência excluímos em definitivo dados do df que são null
A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace = True)
B = dados.shape[0]
A - B

dados[dados['Valor'].isnull()]

# ## Tratamento de Dados Faltantes (continuação)

dados[dados['Condominio'].isnull()].shape[0]

selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())

# no comando de substituição do df para filtragem utilizamos um ~ na frente da seleção que altera os filtros tipo bool
A = dados.shape[0]
dados = dados[~selecao]
B = dados.shape[0]
A - B

dados[dados['Condominio'].isnull()].shape[0]

# para preencher os valor null com .fillna pode ser utilizado um dicionário, definindo um valor a cada variável
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})

dados[dados['Condominio'].isnull()].shape[0]

dados[dados['IPTU'].isnull()].shape[0]

dados.info()

dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)

