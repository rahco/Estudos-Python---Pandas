#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise II

# ## Tipos de Imóveis

import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep = ';')

dados.head(10)

# comando para filtrar uma coluna
dados['Tipo']

# outra forma de fazer o filtra de um campo é utilizando o comando .nome, porém este comando somente 
# vai funcionar se não houver espaços no nome
dados.Tipo

tipo_de_imovel = dados['Tipo']

type(tipo_de_imovel)

# comando .drop_duplicates para remover duplicatas em uma series. O parâmetro inplace=True é importante para a mudança ocorra no ds
tipo_de_imovel.drop_duplicates(inplace=True)

tipo_de_imovel

# ## Organizando a Visualização

tipo_de_imovel = pd.DataFrame(tipo_de_imovel)

tipo_de_imovel

tipo_de_imovel.index

tipo_de_imovel.shape[0]

range(tipo_de_imovel.shape[0])

for i in range(tipo_de_imovel.shape[0]):
    print(i)

# comando para substituir o idex por um range ordenado
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])

tipo_de_imovel.index

tipo_de_imovel

# comando para atribuir um nome a coluna index
tipo_de_imovel.columns.name = 'Id'

tipo_de_imovel

