#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise III

# ## Imóveis Residenciais

import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep = ';')

dados.head(10)

list(dados['Tipo'].drop_duplicates())

residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']

residencial

dados.head(10)

# com o comando atribuimos a list residencial em uma series bool para utilizar como filtro com o comando .isin
selecao = dados['Tipo'].isin(residencial)
selecao

# ao aplicarmos uma series bool em um df ele automaticamente excluir os itens como False mantendo apenas os True
dados_residencial = dados[selecao]

dados_residencial

list(dados_residencial['Tipo'].drop_duplicates())

dados_residencial.shape[0]

dados.shape[0]

dados_residencial.index = range(dados_residencial.shape[0])

dados_residencial

# ## Exportando a Base de Dados

dados_residencial.to_csv('dados/aluguel_residencial.csv', sep = ';')

dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')

dados_residencial_2

# o comando .to_csv exporta a visão do DF criada para um arquivo de extenção csv.
O parâmetro index=False é adicionado ao comando pa
dados_residencial.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)

dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')
dados_residencial_2

