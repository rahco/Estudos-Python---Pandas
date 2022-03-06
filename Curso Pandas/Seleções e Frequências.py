#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise IV

# ## Seleções e Frequências

import pandas as pd

dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')

dados.head(10)

# Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]
n1

# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
n2

# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
# Ou seja 60 <= Area <= 100
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
n3

# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
n4

print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila' -> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))

# # Exercícios extras

import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])


alunos

selecao = alunos['Aprovado'] == True
aprovados = alunos[selecao]
aprovados

selecao = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')
aprovados = alunos[selecao]
aprovados

selecao = (alunos.Idade >= 40) | ((alunos.Idade > 10) & (alunos.Idade < 20))
grupos_idade = alunos[selecao]
grupos_idade

alunos

# Crie um DataFrame somente com os alunos reprovados e mantenha neste 
# DataFrame apenas as colunas Nome, Sexo e Idade, nesta ordem.
selecao = alunos['Aprovado'] == False
reprovados = alunos[['Nome', 'Sexo', 'Idade']][selecao]
reprovados

# Crie uma visualização com os três alunos mais novos
alunos.sort_values(by = ['Idade'], inplace = True)
alunos.iloc[:3]

