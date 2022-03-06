#!/usr/bin/env python
# coding: utf-8

import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados.head(10)

# Objetivo extra é contar no df através de uma faixa de classe de valores da quantidade de quartos
# 1 e 2 quartos
# 3 e 4 quartos
# 5 e 6 quartos
# 7 e XXX quartos
# primeiro passo é criar uma list com os valores de limites máximos de cada classe
# importante ter o valor 0 adicional como um limite nesta list
# sendo 4 classes deve ter uma adicional com o valor 0 conforme ilustrado abaixo
classes = [0, 2, 4, 6, 100]

# com o comando .cut criamos uma series com o rótulo de cada classe por index
# para o comando funcionar precisamos especificar a coluna a ser agrupada e a array de classes criada
quartos = pd.cut(dados.Quartos, classes)

quartos

# para obter a contagem de valores agrupados pela series criada com .cut utilizamos o comando .value_counts
pd.value_counts(quartos)

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais' ]

quartos = pd.cut(dados.Quartos, classes, labels = labels)

# para melhorar a visualização é possível utilizar o parâmetro labels definindo um nome para cada curva
pd.value_counts(quartos)

# o parâmetro include_lowest serve para incluir qualquer valor menor que esteja fora da curva 1 na primeira curva
quartos = pd.cut(dados.Quartos, classes, labels = labels, include_lowest = True)

pd.value_counts(quartos)

