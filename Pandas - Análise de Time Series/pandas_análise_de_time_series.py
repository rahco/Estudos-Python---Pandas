# Alucar - Analisando as vendas

import pandas as pd

pd.read_csv('alucar.csv').head()

alucar = pd.read_csv('alucar.csv')

alucar.head()

print('Quantidade de linhas e colunas: ', alucar.shape)

# na varificação da quantidade de dados nulos, utilizamos a estrutura .sum().sum() para que o resultado traga a soma dos dados nulos de todas as colunas do df
print('Quantidade de dados nulos: ', alucar.isna().sum().sum())

# comando .dtypes para verificação dos tipos dos dados do df
alucar.dtypes

# convertendo o formato das datas de object/str para datetime
alucar['mes'] = pd.to_datetime(alucar['mes'])

alucar.dtypes

# Commented out IPython magic to ensure Python compatibility.
!pip install seaborn==0.9.0
import pandas as pd
import seaborn as sns
# %matplotlib inline
from matplotlib import pyplot as plt

# função para verificar a versão do seaborn instalada
print(sns.__version__)

# comando .lineplot para inserir um gráfico em linha no sns
sns.lineplot(x='mes', y='vendas', data=alucar)

# definindo a paleta de cores
sns.set_palette('Accent')
# ativando linhas de grade
sns.set_style('darkgrid')
# código gráfico atribuido a uma variável para remover o id do gráfico
ax = sns.lineplot(x='mes', y='vendas', data=alucar)
# aumentando a visualização do gráfico
ax.figure.set_size_inches(12,6)
# inserindo título e jogando o mesmo para esquerda com o parâmetro loc
ax.set_title('Vendas Alucar de 2017 e 2018', loc='left', fontsize=18)
# alterando o label do eixo x
ax.set_xlabel('Tempo', fontsize=14)
# alterando o label do eixo y
ax.set_ylabel('Vendas (R$)', fontsize=14)
# comando para remover configurações que são exibinas na head do gráfico
ax = ax

alucar.head()

# com a função .diff() do pd podemos criar uma coluna nova no df com a diferença entre os registros de um df linha a linha
alucar['aumento'] = alucar['vendas'].diff()
alucar.head()

# plotando gráfico da coluna aumento
sns.set_palette('Accent')
sns.set_style('darkgrid')
ax = sns.lineplot(x='mes', y='aumento', data=alucar)
ax.figure.set_size_inches(12,6)
ax.set_title('Aumento das vendas da Alucar de 2017 e 2018', loc='left', fontsize=18)
ax.set_xlabel('Tempo', fontsize=14)
ax.set_ylabel('Aumento', fontsize=14)
ax = ax

# criando uma função para plotar gráficos apenas definindo os parâmetros definidos na função
def plotar(titulo, labelx, labely, x, y, dataset):
  sns.set_palette('Accent')
  sns.set_style('darkgrid')
  ax = sns.lineplot(x=x, y=y, data=dataset)
  ax.figure.set_size_inches(12,6)
  ax.set_title(titulo, loc='left', fontsize=18)
  ax.set_xlabel(labelx, fontsize=14)
  ax.set_ylabel(labely, fontsize=14)
  ax = ax

# testando a função para plotagem do gráfico com as configurações pré-definidas na função
plotar('Aumento das vendas da Alucar de 2017 e 2018', 'Tempo', 'Aumento', 'mes', 'aumento', alucar)

alucar['aceleracao'] = alucar['aumento'].diff()
alucar.head()

plotar('Aceleração das vendas da Alucar de 2017 e 2018', 'Tempo', 'Aceleração', 'mes', 'aceleracao', alucar)

# criando uma área de plotagem com o plt sendo as medidas o comprimentoxaltura
plt.figure(figsize=(16,12))
# definindo a distribuição das imagens
ax = plt.subplot(3,1,1)
# criando o título da área de plotagem
ax.set_title('Análise de vendas da Alucar de 2017 e 2018', fontsize=18, loc='left')
# definindo o gráfico da primera posição
sns.lineplot(x='mes', y='vendas', data=alucar)
# definindo o gráfico do meio
plt.subplot(3,1,2)
sns.lineplot(x='mes', y='aumento', data=alucar)
# definindo o gráfico abaixo na imagem
plt.subplot(3,1,3)
sns.lineplot(x='mes', y='aceleracao', data=alucar)
ax = ax

# criando uma função para gerar a área de plotagem com os gráficos baseado em parâmetros
def plot_comparacao(x, y1, y2, y3, dataset, titulo):
  plt.figure(figsize=(16,12))
  ax = plt.subplot(3,1,1)
  ax.set_title(titulo, fontsize=18, loc='left')
  sns.lineplot(x=x, y=y1, data=dataset)
  plt.subplot(3,1,2)
  sns.lineplot(x=x, y=y2, data=dataset)
  plt.subplot(3,1,3)
  sns.lineplot(x=x, y=y3, data=dataset)
  ax = ax

# testando a função de geração da área com os gráficos
plot_comparacao('mes', 'vendas', 'aumento', 'aceleracao', alucar, 'Análise das vendas da Alucar de 2017 e 2018')

# importando a biblioteca para gerar gráficos de autocorrelação entre dados
from pandas.plotting import autocorrelation_plot

ax = plt.figure(figsize=(12,6))
# os parâmetros x e y servem para posicionar o título do gráfico
ax.suptitle('Correlação das Vendas', fontsize=18, x=0.26, y=0.95) 
autocorrelation_plot(alucar['vendas'])
ax=ax

ax = plt.figure(figsize=(12,6))
# os parâmetros x e y servem para posicionar o título do gráfico
ax.suptitle('Correlação do aumento', fontsize=18, x=0.26, y=0.95) 
# para o gráfico tivemos que utilizar a propriedade [1:] para pular o primeiro dado nulo que tornavana o lag do gráfico de aucorrelação sempre 0
autocorrelation_plot(alucar['aumento'][1:])
ax=ax

ax = plt.figure(figsize=(12,6))
# os parâmetros x e y servem para posicionar o título do gráfico
ax.suptitle('Correlação da aceleração', fontsize=18, x=0.26, y=0.95) 
# para o gráfico tivemos que utilizar a propriedade [1:] para pular o primeiro dado nulo que tornavana o lag do gráfico de aucorrelação sempre 0
autocorrelation_plot(alucar['aceleracao'][2:])
ax=ax

"""# Alucar - Analisando assinantes da newsletter"""

assinantes = pd.read_csv('newsletter_alucar.csv')
assinantes.head()

assinantes.dtypes

# verificando os dados
print('Quantidade de linhas e colunas', assinantes.shape)
print('Quantidade de dados nulos', assinantes.isna().sum().sum())

assinantes['mes'] = pd.to_datetime(assinantes['mes'])
assinantes.dtypes

assinantes['aumento']= assinantes ['assinantes'].diff()
assinantes['aceleracao']= assinantes ['aumento'].diff()

assinantes.head()

# utilizando a função plot_comparacao criada para análise dos dados de assinantes
plot_comparacao('mes', 'assinantes', 'aumento', 'aceleracao', assinantes, 'Análise de assinantes da newsletter')

"""# Chocolura - Analisando as vendas"""

chocolura = pd. read_csv('chocolura.csv')
chocolura.head()

chocolura.dtypes

chocolura['mes'] = pd.to_datetime(chocolura['mes'])
chocolura.dtypes

print ('Quantidade de linhas:', chocolura.shape)
print ('Quantidade de dados nulos:', chocolura.isna().sum().sum())

chocolura['aumento']= chocolura ['vendas'].diff()
chocolura['aceleracao']= chocolura ['aumento'].diff()
chocolura.head()

plot_comparacao('mes', 'vendas', 'aumento', 'aceleracao', chocolura, 'Análise de vendas da Chocolura de 2017 a 2018')

"""# Chocolura - Vendas diárias (Outubro e Novembro"""

vendas_por_dia = pd. read_csv('vendas_por_dia.csv')
vendas_por_dia.head()

print ('Quantidade de linhas:',vendas_por_dia.shape)
print ('Quantidade de dados nulos:', vendas_por_dia.isna().sum().sum())

vendas_por_dia.dtypes

vendas_por_dia['dia'] = pd.to_datetime(vendas_por_dia['dia'])

vendas_por_dia.dtypes

vendas_por_dia['aumento']= vendas_por_dia['vendas'].diff()
vendas_por_dia['aceleracao']= vendas_por_dia ['aumento'].diff()
vendas_por_dia.head()

plot_comparacao('dia', 'vendas', 'aumento', 'aceleracao', vendas_por_dia, 'Análise de vendas de Outubro e Novembro - Chocolura')

"""# Analizando a sazonalidade"""

# com o comando .dt.day_name() podemos obter o dia da semana de uma datetime
vendas_por_dia['dia_da_semana'] = vendas_por_dia ['dia'].dt.day_name()
vendas_por_dia.head(7)

vendas_por_dia['dia_da_semana'].unique()

dias_traduzidos = {'Monday': 'Segunda', 'Tuesday' : 'Terca', 'Wednesday':'Quarta', 'Thursday':'Quinta', 'Friday':'Sexta', 'Saturday':'Sabado', 'Sunday':'Domingo'}

vendas_por_dia['dia_da_semana'] = vendas_por_dia['dia_da_semana'].map(dias_traduzidos)
vendas_por_dia.head(14)

"""# Agrupando os dias"""

# verificando as metas por dia da semana
vendas_agrupadas = vendas_por_dia.groupby('dia_da_semana')['vendas', 'aumento', 'aceleracao'].mean().round()

vendas_agrupadas

"""**Correlação das vendas diárias**"""

ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação das vendas diárias', fontsize=18, x=0.3, y=0.95)
autocorrelation_plot(vendas_por_dia['vendas'])
ax = ax

ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação do aumento das vendas diárias', fontsize=18, x=0.3, y=0.95)
autocorrelation_plot(vendas_por_dia['aumento'][1:])
ax = ax

ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação da aceleração das vendas diárias', fontsize=18, x=0.3, y=0.95)
autocorrelation_plot(vendas_por_dia['aceleracao'][2:])
ax = ax

"""# Cafelura - Análise de vendas"""

cafelura = pd.read_csv('cafelura.csv')
cafelura.head()

cafelura.dtypes

cafelura['mes']= pd.to_datetime(cafelura['mes'])

cafelura.dtypes

print('Quantidade de linhas e colunas:', cafelura.shape)
print('Quantidade de dados nulos:', cafelura.isna().sum().sum())

plotar('Vendas da Cafelura de 2017 e 2018', 'Tempo', 'Vendas', 'mes', 'vendas', cafelura)

# dataset cotendo a quantidade de dias de fds por mês existente
quantidade_de_dias_de_fds = pd.read_csv('dias_final_de_semana.csv')

quantidade_de_dias_de_fds.head()

# array contendo os valores de dias de fds
quantidade_de_dias_de_fds['quantidade_de_dias'].values

# normalizando as vendas baseando na distribuição por dias de final de semana no mês
cafelura['vendas_normalizadas']= cafelura['vendas']/quantidade_de_dias_de_fds['quantidade_de_dias'].values
cafelura.head

# plotando gráfico com as vendas normalizadas
plotar('Vendas normalizadas da Cafelura de 2017 a 2018', 'Tempo', 'Vendas normalizadas', 'mes', 'vendas_normalizadas', cafelura)

# comparativo entre as visões
plt.figure(figsize=(16,12))
ax=plt.subplot(2,1,1)
ax.set_title('Vendas Cafelura 2017 e 2018', fontsize=18)
sns.lineplot(x='mes', y='vendas', data=cafelura)
ax=plt.subplot(2,1,2)
ax.set_title('Vendas normalizadas Cafelura 2017 e 2018', fontsize=18)
sns.lineplot(x='mes', y='vendas_normalizadas', data=cafelura)
ax=ax

"""# Statsmodels"""

from statsmodels.tsa.seasonal import seasonal_decompose

# verificando com a função statsmodels os dados de relevância em uma list
resultado = seasonal_decompose(chocolura['vendas'],  freq=3)
ax = resultado.plot()

# atribuindo os resultados uma variável para criação de um df com os dados
observacao = resultado.observed
tendencia = resultado.trend
sazonalidade = resultado.seasonal
ruido = resultado.resid

# adicionando os dados a um dicionário e posteriormente a um df
data = ({
       'observacao':observacao,
       'tendencia':tendencia, 
       'sazonalidade':sazonalidade,
       'ruido':ruido
})
resultado = pd.DataFrame(data)
resultado.head()

# plotando resultados do df
plot_comparacao(resultado.index, 'observacao', 'tendencia', 'sazonalidade', resultado, 'Exemplo de Statsmodels')

# plotando resultados do df
plot_comparacao(resultado.index, 'observacao', 'tendencia', 'ruido', resultado, 'Exemplo de Statsmodels')

"""# Alucel - Análise de vendas"""

alucel = pd.read_csv('alucel.csv')
alucel.head()

alucel['dia'] = pd.to_datetime(alucel['dia'])
alucel.dtypes

print('Quantidade de linhas e colunas:', alucel.shape)
print('Quantidade de dados nulos:', alucel.isna().sum().sum())

alucel ['aumento'] = alucel ['vendas'].diff()
alucel ['aceleracao'] = alucel ['aumento'].diff()
alucel.head()

plot_comparacao('dia', 'vendas', 'aumento', 'aceleracao', alucel, 'Análise de vendas da Alucel de Outubro e Novembro de 2018')

"""**Média móvel**"""

# o comando .rolling com o parâmetro de frequência a ser inserido, gera uma média móvel entre pontos
# a média móvel é muito útil para normalizar dados que possuem uma forte variável em curta frequência, para determinal a tendência de uma variável
alucel['media_movel'] = alucel['vendas'].rolling(7).mean()
alucel.head(8)

plotar('Análise de vendas com média móvel de 7 dias', 'Tempo', 'Média Móvel', 'dia', 'media_movel', alucel)

alucel['media_movel_21'] = alucel['vendas'].rolling(21).mean()

plotar('Análise de vendas com média móvel de 21 dias', 'Tempo', 'Média Móvel', 'dia', 'media_movel_21', alucel)

plot_comparacao('dia', 'vendas', 'media_movel', 'media_movel_21', alucel, 'Comparando as médias móveis')

