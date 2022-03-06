#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# comando para visualizar os dados de um arquivo json no pandas
json = open('dados/aluguel.json')
print(json.read())

# comando completo importando e transformando um arquivo json em df
df_json = pd.read_json('dados/aluguel.json')
df_json

# comando para visualizar os dados de um arquivo txt no pandas
txt = open('dados/aluguel.txt')
print(txt.read())

# comando completo importando e transformando um arquivo txt em df
df_txt = pd.read_table('dados/aluguel.txt')
df_txt

# comando completo importando e transformando um arquivo xlsx(excel) em df
df_xlsx = pd.read_excel('dados/aluguel.xlsx')
df_xlsx

# comando completo importando e transformando um arquivo html em df
df_html = pd.read_html('dados/dados_html_1.html')
df_html[0]

# comando completo importando e transformando um arquivo html utilizando o endereço da internet em df
df_html = pd.read_html('file:///D:/Pessoal/Raphael/Cursos/TI/Forma%C3%A7%C3%A3o%20-%20Python%20para%20Data%20Science/Curso%2004%20-%20Python%20Pandas%20-%20Tratando%20e%20analisando%20dados/Arquivos%20de%20apoio/Aula%2002/extras/dados/dados_html_1.html')
df_html[0]

# quando a página web possui mais de uma tabela é necessário importar o item e selecionar a tabela desejada na visualização
df_html = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')

len(df_html)

df_html[0]

df_html[1]

df_html[2]

