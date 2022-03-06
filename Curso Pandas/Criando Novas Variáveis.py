#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VI

# ## Criano Novas Variáveis

import pandas as pd

dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')

dados.head(10)

# criando uma nova variáveis no df chamada valor bruto
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']

dados.head(10)

# criando a variável valor/metro quadrado. O comando .round é utilizado para arrendar o valor calculado
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)

dados.head(10)

# criando a variável valor bruto / metro quadrado
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)

dados

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')

dados

# ## Excluindo Variáveis

# df criado a partir do df dados para ilustrar métodos de excluir variáveis de um df
dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])

dados_aux.head(10)

# 1º formato: passando o campo variável com o comando del
del dados_aux['Valor Bruto']

dados_aux.head(10)

# 2º formato: utilizando o comando .pop
dados_aux.pop('Valor Bruto m2')

dados_aux

# 3º formato: utilizando o comando .drop e especificando as colunas ou linhas a serem removidas
dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)

dados

dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)

