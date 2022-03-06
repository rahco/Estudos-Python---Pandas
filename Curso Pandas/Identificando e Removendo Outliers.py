#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VIII

# ## Identificando e Removendo Outliers

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))

dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')

# o comando .boxplot exibe um gráfico para verificação se o conjunto de dados possuem uma distorção significativa
dados.boxplot(['Valor'])

dados[dados['Valor'] >= 500000]

valor = dados['Valor']

# Com duplo click sobre a imagem é possível ver o código HTML de inserção da mesma

# <img src="Box-Plot.png" width=70%>

# baseado no conceito do comando box-plot, dividimos as informações em quartios para seleção dos dados mais coerentes a análise
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

# com a seleção dos valores definidos no box-plot temos a seleção final no bd
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]

dados_new.boxplot(['Valor'])

# com o comando .hist podemos fazer um comparativo para verificar o resultado da ação do filtro
dados.hist(['Valor'])
dados_new.hist(['Valor'])

print(Q1)
print(Q3)
print(IIQ)
print(limite_inferior)
print(limite_superior)

# ## Identificando e Removendo Outliers (por tipo)

# o comando .boxplot pode ser utilizado com o parâmetro by para visualizar os dados agrupados
dados.boxplot(['Valor'], by = ['Tipo'])

# com o comando .groupby criamos uma series agrupada por uma variável e selecionando o campo 
grupo_tipo = dados.groupby('Tipo')['Valor']

type(grupo_tipo)

# com os comandos acima criamos uma series com o tipo sendo a chave e os valores em index em um dicionário
grupo_tipo.groups

# ao criarmos os quartios temos uma series com os resultados por agrupamento
Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

Q1

Q3

IIQ

limite_inferior

limite_superior

limite_superior['Casa']

# para filtramos os dados considerando o agrupamento fazemos um laço for iterando a filtragem e gerando um novo df
# no laço criamos duas variávels eh bool para filtragem dos dados por agrupamento
# unificamos a seleção dos bool em uma variável selecao
# criamos um df da seleção específica ao grupo analisado
# finalizamos o for concatenando os df filtrados
dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

dados_new.boxplot(['Valor'], by = ['Tipo'])

dados_new.to_csv('dados/aluguel_residencial_sem_outliers.csv', sep = ';', index = False)

