# <font color=green> PYTHON PARA DATA SCIENCE - PANDAS
---

# <font color=green> 1. INTRODUÇÃO AO PYTHON
---

# 1.1 Introdução

> Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares. 
>
> Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assundo é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado.

# 1.2 Instalação e ambiente de desenvolvimento

### Instalação Local

### https://www.python.org/downloads/
### ou
### https://www.anaconda.com/distribution/

### Google Colaboratory

### https://colab.research.google.com

### Verificando versão
!python -V

"""# 1.3 Trabalhando com dados"""

# comando de import do pacote pandas
import pandas as pd
# comando opcional para aumentar o limite de linhas e colunas exibidas de um dataset
#pd.set_option('display.max_rows', 10)
#pd.set_option('display.max_columns', 1000)

# comando de import de arquivo csv para o ambiente
dataset = pd.read_csv('db.csv', sep = ';')

dataset

# comando de verificação dos tipos de dados
dataset.dtypes

#comando para visualizar um conjunto de estatísticas de alguns campos selecionados do dataset
dataset[['Quilometragem', 'Valor']].describe()

# comando para visualizar algumas informações básicas de um dataset
dataset.info()

"""# <font color=green> 2. TRABALHANDO COM TUPLAS
---

# 2.1 Criando tuplas

Tuplas são sequências (similares as listas) imutáveis que são utilizadas para armazenar coleções de itens, geralmente heterogêneos. Podem ser construídas de várias formas:
```
- Utilizando um par de parênteses: ( )
- Utilizando uma vírgula à direita: x,
- Utilizando um par de parênteses com itens separados por vírgulas: ( x, y, z )
- Utilizando: tuple() ou tuple(iterador)
```
"""

()

1,2,3

nome = 'Passat'
valor = 153000
(nome,valor)

nome_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
nome_carros

type(nome_carros)

"""# 2.2 Seleções em tuplas"""

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

# comando para acessar um item específico dentro de uma tupla
nomes_carros[0]

nomes_carros[1]

# comando para acessar o último item em uma tupla
nomes_carros[-1]

# comando para filtrar itens em uma dupla determinando um intervalo de início e fim
nomes_carros[1:3]

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
nomes_carros

# uma tupla dentro de uma tupla pode ser acessada por inteira pois a mesma é considerada como um item dentro da tupla
nomes_carros[-1]

# para acessar um item de tupla dentro de uma outra tupla, basta adicionar o comando de posição do item desejado após o comando de acesso a tupla
nomes_carros[-1][1]

"""# 2.3 Iterando em tuplas"""

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

# comando para varrer e printar todos os itens de uma tupla
for item in nomes_carros:
  print(item)

"""### Desempacotamento de tuplas"""

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

# listando nomes e igualando a uma tupla é possível atribuir os valores sequências de uma tupla a variávis simultaneamente  
carro_1, carro_2, carro_3, carro_4 = nomes_carros

carro_1

carro_2

carro_3

carro_4

# utilizando o underscore é possível ignorar campos da tupla para criar variáveis apenas com alguns itens da tupla
_, A, _, B = nomes_carros

A

B

# quando a tupla for muito grande e existe a necessidade de aplicar a variável a apenas um item da lista é possível utilizaro *_ para ignorar os demais itens da tupla
_, C, *_ = nomes_carros

C

"""## *zip()*

https://docs.python.org/3.6/library/functions.html#zip
"""

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
carros

valores = [88078.64, 106161.94, 72832.16, 124549.07]
valores

# o comando zip é um iterador que utilizado junto com um comando de agregação pode criar uma lista com conjunto de dados separados em tuplas ou listas, basicamente ele criar uma associação entre os dados
list(zip(carros, valores))
# como no exemplo o comando pegou cada elemento dos conjuntos de dados e criou tuplas agrupadas em uma lista

# comando para printar o empacotamento dos dados feito pelo iterador zip
for item in zip(carros, valores):
  print(item)

# ao se utilizar o zip os valores empacorados podem ser mostrados/printados individualmente (fora da tupla) mas ainda conectados uns aos outros
for carro, valor in zip(carros, valores):
  print(carro, valor)

# utilizando o desempacotamento do zip com o for é possível criar filtro entre as informações que foram combinadas pelo zip utilizando o comando if
for carro, valor in zip(carros, valores):
  if(valor > 100000):
    print(carro)

"""# <font color=green> 3. TRABALHANDO COM DICIONÁRIOS
---

# 3.1 Criando dicionários

Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices (números inteiros) para acessar os valores.

Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento. Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido como chave (*key*) e o segundo como valor (*value*).

```
dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n}
```

https://docs.python.org/3.6/library/stdtypes.html#typesmapping
"""



carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros

valores = [88078.64, 106161.94, 72832.16]
valores

# comando .index ser para buscar o índice de um elemento dentro de uma lista
carros.index('Passat')

# utilizando o comando .index é possível buscara informação relacionado a um elemento em outra lista
valores[carros.index('Passat')]

# com o comando abaixo é possível agrupar os dados relacionando os elementos através de chaves, em uma estrutura chamada dicionário (dict)
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

type(dados)

"""### Criando dicionários com *zip()*"""

list(zip(carros, valores))

# outra forma de criar um dataset relacional agrupando dados em um dicionário (dict) é utilizando o iterador zip que agrupa os elementos em tuplas
dados = dict(zip(carros, valores))
dados

"""# 3.2 Operações com dicionários"""

# com o comando abaixo é possível agrupar os dados relacionando os elementos através de chaves, em uma estrutura chamada dicionário (dict)
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

"""## *dict[ key ]*

Retorna o valor correspondente à chave (*key*) no dicionário.
"""

# comando para buscar o valor relacional de um elemento através de sua chave
dados['Passat']

"""## *key in dict*

Retorna **True** se a chave (*key*) for encontrada no dicionário.
"""

# comando para verificar se uma chave está ou não contida em um dicionário
'Passat' in dados

'Fusca' in dados

'Fusca' not in dados

"""## *len(dict)*

Retorna o número de itens do dicionário.
"""

# retorna quantos pares de valores estão contidos em um dicionário
len(dados)

"""## *dict[ key ] = value*

Inclui um item ao dicionário.
"""

# comando para adicionar um item a um dicionário
dados['DS5'] = 124549.07

dados

"""## *del dict[ key ]*

Remove o item de chave (*key*) do dicionário.
"""

dados

# comando para remover um item de um dicionário
del dados['Passat']
dados

"""## Atividade Extra"""

dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

# 1) Testar se a chave acessorios existe no dicionário de informações do carro Crossfox (Resposta: False)
'acessorios' in dados['Crossfox']

# 2) Testar se a chave acessorios existe no dicionário de informações do carro Passat (Resposta: True)
'acessorios' in dados['Passat']

# 3) Obter o valor do carro Crossfox (Resposta: 25000)
dados['Crossfox']['valor']

# 4) Acessar o último acessório do carro Passat (Resposta: 'ABS')
dados['Passat']['acessorios'][-1]

# respostas
'acessorios' in dados['Crossfox']
'acessorios' in dados['Passat']
dados['Crossfox']['valor']
dados['Passat']['acessorios'][-1]

"""# 3.3 Métodos de dicionários

## *dict.update()*

Atualiza o dicionário.
"""

dados

# comando para fazer a atualização de um dicionário incluindo um novo item
dados.update({'Passat': 106161.94})
dados

# o comando .update pode ser utilizado tanto para adicionar novos itens como para alterar o valor de algum item como feito com o valor do carro Passat
dados.update({'Passat': 106161.95, 'Fusca': 150000})
dados

"""## *dict.copy()*

Cria uma cópia do dicionário.
"""

# com o comando .copy() uma nova cópia independente do dicionário será criada, podendo ter alterações que não serão refletidas na origem
dadosCopy = dados.copy()

dadosCopy

del dadosCopy['Fusca']
dadosCopy

dados

"""## *dict.pop(key[, default ])*

Se a chave for encontrada no dicionário, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como *default* é retornado. Se o valor *default* não for fornecido e a chave não for encontrada no dicionário um erro será gerado.
"""

dadosCopy

# utilizando o comando .pop e designando um item a ser eleminado, o console responde o valor que foi removido do dicionário
dadosCopy.pop('Passat')

dadosCopy

# dadosCopy.pop('Passat') ao tentar utilizar o comando novamente de exclusão de um item já removido no console aparecerá uma mensagem de erro

# para evitar a mensagem de erro após a vírgula no comando .pop é possível escrever uma mensagem de erro sinalizando que o elemento não foi entrado para eviar a mensagem de erro
dadosCopy.pop('Passat', 'Chave não encontrada')

dadosCopy.pop('DS5', 'Chave não encontrada')

dadosCopy

"""## *dict.clear()*

Remove todos os itens do dicionário.
"""

# o comando .clear limpa por completo os dados contidos em um dicionário
dadosCopy.clear()

dadosCopy

"""# 3.4 Iterando em dicionários"""

dados = {'Crossfox': 72832.16, 'DS5': 124549.07, 'Fusca': 150000, 'Jetta Variant': 88078.64, 'Passat': 106161.95}
dados

"""## *dict.keys()*

Retorna uma lista contendo as chaves (*keys*) do dicionário.
"""

dados.keys()

# com o comando .keys é possível ter o retorno uma lista todas as chaves contidas em um dicionário. Essa lista pode ser utilizada com for para demostrar os itens chave ou valores relacionados
for key in dados.keys():
  print(dados[key])

"""## *dict.values()*

Retorna uma lista com todos os valores (*values*) do dicionário.
"""

# como comando .keys o comando .values retorna todas os valores contidos em um dicionário
dados.values()

"""## *dict.items()*

Retorna uma lista contendo uma tupla para cada par chave-valor (*key-value*) do dicionário.
"""

# o comando .items transforma um dicionário em uma lista com os valores relacionados agrupados em tuplas
dados.items()

for item in dados.items():
  print(item)

# o comando items pode ser utilizado junto ao comando for para fazer o desempacotamento de tuplas
for key, value in dados.items():
  print(key, value)

# com o desempacotamento dos dados é possível utilizar comandos como o if para filtragem de dados
for key, value in dados.items():
  if(value > 100000):
    print(key)

"""# Teste"""

dataset = {
    'Crossfox': {'valor': 72000, 'ano': 2005}, 
    'DS5': {'valor': 125000, 'ano': 2015}, 
    'Fusca': {'valor': 150000, 'ano': 1976}, 
    'Jetta': {'valor': 88000, 'ano': 2010}, 
    'Passat': {'valor': 106000, 'ano': 1998}
}

for item in dataset.items():
  if(item[1]['ano'] >= 2000):
    print(item[0])

"""# <font color=green> 4. FUNÇÕES E PACOTES
---
    
Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado.

# 4.1 Built-in function

A linguagem Python possui várias funções integradas que estão sempre acessíveis. Algumas já utilizamos em nosso treinamento: type(), print(), zip(), len(), set() etc.

https://docs.python.org/3.6/library/functions.html
"""

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

# linhas para agrupar os valores de um dicionário em uma lista chamada valores
valores = []
for valor in dados.values():
  valores.append(valor)
valores

# linhas para somar todos os valores de um dicionário em uma variável chamada soma
soma = 0
for valor in dados.values():
  soma += valor
soma

# utilizando o comando list foi possível reproduzir o efeito da linha 83 com apenas uma linha de código
list(dados.values())

# com a built-in function sum foi possível reproduzir o efeito do código 84 em uma única linha de código
sum(dados.values())

# após a vírgula é possível configurar um parâmetro adicional ao comando sum que é um valor que irá ser adicionado inicialmente a soma
sum(dados.values(), 1000000)

# o comando help demonstra um grupo de informações de apoio para o entendimento a uma built-in function
help(print)

# similar ao help o comando exibe informações de ajuda sobre alguma built-in function
print?

"""# 4.2 Definindo funções sem e com parâmetros

### Funções sem parâmetros

#### Formato padrão

```
def <nome>():
    <instruções>
```
"""

# o comando def serve para criar uma função no python. No exemplo abaixo temos uma função de média criada porém com parâmetros fixos
def media():
  valor = (1 + 2 + 3) / 3
  print(valor)

# para printar o resultado de uma função no console, basta inserir o nome da função seguido de ()
media()

"""### Funções com parâmetros

#### Formato padrão

```
def <nome>(<param_1>, <param_2>, ..., <param_n>):
    <instruções>
```
"""

# função criada para gerar a média de 3 números, porém que precisaram de parâmetros a serem especificados na hora de chamar a função
def media(number_1, number_2, number_3):
  valor = (number_1 + number_2 + number_3) / 3
  print(valor)

# ao chamar uma função que tenha parâmetros é necessário informalos sequencialmente dentro das ()
media(1, 2, 3)

# com a função criada é possível utilizar a mesma com qualquer valores definidos em seus parâmetros
media(23, 45, 67)

# uma função pode ser criada utilizando built-in functions como list, sum, len, etc. Abaixo o exemplo de uma função de média cálculada sobre elementos de uma lista
def media(lista):
  valor = sum(lista) / len(lista)
  print(valor)

# função média criada sendo executada com uma lista de dados
media([1, 2, 3, 4, 5, 6, 7, 8, 9])

resultado = media([1, 2, 3, 4, 5, 6, 7, 8, 9])

resultado

# no exemplo da função criada acima, como a função apenas print o resultado, não é possível atribuir seu resultado a uma variável como exemplificado
type(resultado)

"""# Teste"""

data = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    for item in dataset.items():
        result = item[1]['km'] / (ano_atual - item[1]['ano'])
        print(result)

km_media(data, 2019)

"""# 4.3 Definindo funções que retornam valores

### Funções que retornam um valor

#### Formato padrão

```
def <nome>(<param_1>, <param_2>, ..., <param_n>):
    <instruções>
    return <resultado>
```
"""

# com o comando return no final da descrição da função é possível atribuir o resultado de uma função a uma variável
def media(lista):
  valor = sum(lista) / len(lista)
  return valor

media([1, 2, 3, 4, 5, 6, 7, 8])

resultado = media([1, 2, 3, 4, 5, 6, 7, 8])

resultado

"""### Funções que retornam mais de um valor

#### Formato padrão

```
def <nome>(<param_1>, <param_2>, ..., <param_n>):
    <instruções>
    return (<resultado_1>, <resultado_2>, ..., <resultado_n>)
```
"""

# no comando return é possível adicionar mais valores para serem o resultado de uma função, geralmente usualmente tuplas de resultado
def media(lista):
  valor = sum(lista) / len(lista)
  return (valor, len(lista))

media([1, 2, 3, 4, 5, 6, 7, 8, 9])

# os resultados podem ser adicionados a variáveis sequêncialmente, seperando assim os valores das tuplas
resultado, n = media([1, 2, 3, 4, 5, 6, 7, 8, 9])

resultado

n

"""## Teste"""

dst = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        result.update ({ item[0]: media})       
    return result

km_media(dst, 2019)

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({'km_media':media})
        result.update({item[0]:item[1]})
    return result

km_media(dst, 2019)

"""# <font color=green> 5. PANDAS BÁSICO
---

**versão: 0.25.2**
  
Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.


## Estruturas de Dados

### Series

Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de **index**. A forma básica de criação de uma Series é a seguinte:


```
    s = pd.Series(dados, index = index)
```

O argumento *dados* pode ser um dicionário, uma lista, um array Numpy ou uma constante.

### DataFrames

DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.


```
    df = pd.DataFrame(dados, index = index, columns = columns)
```

O argumento *dados* pode ser um dicionário, uma lista, um array Numpy, uma Series e outro DataFrame.

**Documentação:** https://pandas.pydata.org/pandas-docs/version/0.25/

# 5.1 Estruturas de dados
"""

# comando de importação do pandas no colab
import pandas as pd

"""### Criando uma Series a partir de uma lista"""

carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros

# comando para criar uma Series no pandas
pd.Series(carros)

"""### Criando um DataFrame a partir de uma lista de dicionários"""

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(dados)

dataset

# chamando o DataFrame criado e especificando entre colchetes
dataset[['Ano', 'Nome', 'Motor', 'Quilometragem', 'Zero_km', 'Valor']]

"""### Criando um DataFrame a partir de um dicionário"""

dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

# o comando DataFrame pode ser utilizado da mesma forma com dicionários
dataset = pd.DataFrame(dados)

dataset

"""### Criando um DataFrame a partir de uma arquivo externo"""

# com o comando .read_csv é possível carregar de um arquivo extorno um DataFrame. O comando adicional index_col pode ser utilizado para tornar a primeira coluna do DataFrame a index de toda tabela
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)

dataset

"""## Teste"""

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })

    return result

km_media(dados, 2019)

carros = pd.DataFrame(km_media(dados, 2019)).T

carros

"""# 5.2 Seleções com DataFrames"""

# com o comando .head podemos visualizar as 5 primeiras linhas de um dataset criado
dataset.head()

"""### Selecionando colunas"""

# colocando o nome da coluna dentro de um colchetes é possível filtrar apenas uma coluna de um DataFrame. O idex do DF sempre será exibido junto a coluna filtrada
dataset['Valor']

# ao selecionar uma coluna de um DF o tipo é indicado como um Series, ou seja um DF é um conjunto de Series
type(dataset['Valor'])

# selecionando a coluna de um DF com colchetes duplos, se obtem um objeto do tipo DF
dataset[['Valor']]

type(dataset[['Valor']])

"""### Selecionando linhas - [ i : j ] 

<font color=red>**Observação:**</font> A indexação tem origem no zero e nos fatiamentos (*slices*) a linha com índice i é **incluída** e a linha com índice j **não é incluída** no resultado.
"""

# seleção de linhas segue o mesmo formato de seleção de itens em arrays, listas e dicionários
dataset[0:3]

"""### Utilizando .loc para seleções

<font color=red>**Observação:**</font> Seleciona um grupo de linhas e colunas segundo os rótulos ou uma matriz booleana.
"""

# com o comando .loc temos de retorno uma Series com as informações do item filtrado
dataset.loc['Passat']

# para seleção de mais itens pode-se utilizar o colchetes duplo transformando o retorno series em DF
dataset.loc[['Passat', 'DS5']]

# com o comando de colchetes duplos podemos separar por vírgulas fazendo filtro de linhas e colunas dentro do DF
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]

# adicionando : é possível selecionar todas as linhas ou colunas dentro de um filtro
dataset.loc[:, ['Motor', 'Valor']]

"""### Utilizando .iloc para seleções

<font color=red>**Observação:**</font> Seleciona com base nos índices, ou seja, se baseia na posição das informações.
"""

dataset.head()

# com o comando .iloc o filtro do DF é feito pelo índice inicial das linhas 
dataset.iloc[[1]]

# com a seleção multipla de linhas não se faz necessário o uso do colchetes duplos, e especificando o range a ser filtrado o DF é atualizado
dataset.iloc[1:4]

# com o camando abaixo é possível filtrar linhas e colunas, inclusive definindo o posicionamento das colunas filtradas
dataset.iloc[1:4, [0, 5, 2]]

# com colchetes tanto para linhas e colunas é possível especificar o formato total do DF a ser exibido
dataset.iloc[[1, 42, 22], [0, 5, 2]]

# com o : podemos trazer todas as informações de linhas ou colunas dentro do DF
dataset.iloc[:, [0, 5, 2]]

"""## Test - Filtros"""

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])

dataset.head()

dataset.iloc[[1, 3], [0, -1]]

"""# 5.3 Queries com DataFrames"""

dataset.head()

# quanto o rótulo da coluna for simples e sem espações, utilizado o variável do DF .nomedacoluna é possível gerar uma series com as informações da coluna
dataset.Motor

# utilizando o parâmetro de comparação == é possível gerar uma series que avalia se a condição é true/false que pode ser utilizada como filtro
dataset.Motor == 'Motor Diesel'

select = dataset.Motor == 'Motor Diesel'

type(select)

# atribuindo o resultado da comparação == a uma variável e aplicando ela para filtragem no DF é possível gerar um DF com a filtragem dos dados true da comparação
dataset[select]

# utilizando chaves e o & (que representa a condição AND na filtragem) é possível fazer uma filtragem no DF de mais condições. O simbolo & poderia ser substituido por | (que significa OR)
dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]

(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)

"""### Utilizando o método query"""

# utilizando o comando .query é possível filtrar dados no DF de forma similar ao método de comparação, escrevendo todo código de filtragem entre aspas simples. A condição and pode ser alterada para or
dataset.query('Motor == "Motor Diesel" and Zero_km == True')

"""# 5.4 Iterando com DataFrames"""

dataset.head()

for item in dataset:
  print(item)

# utilizando o comando list com .iterrows criamos uma visão do DF com uma lista com os item em tuplas e series
list(dataset.iterrows())

# combinando for | list | .iterrows pode-se fazer iterações no DF como inclusão ou modificação de itens
for index, row in dataset.iterrows():
  if(2019 - row['Ano'] != 0):
    dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
  else:
    dataset.loc[index, 'Km_media'] = 0

dataset

"""# 5.5 Tratamento de dados"""

dataset.head()

dataset.info()

# o comando .isna cria uma series bool indicando True informações nulas no DF. Esse comando pode ser utilizado para filtrar dados com erros no DF
dataset.Quilometragem.isna()

# aplicando o .isna no filtro do DF temos a visão onde apenas os dados apresentam resultados NAN
dataset[dataset.Quilometragem.isna()]

# com o comando .fillna pode-se transformar todo 0 contido no DF em algum valor específico
dataset.fillna(0, inplace = True)

dataset

dataset.query("Zero_km == True")

dataset = pd.read_csv('db.csv', sep = ';')

dataset

# utilizando o comando .dropna e especificando a coluna do DF podemos remover os registros do DF por completo caso seja necessário
dataset.dropna(subset = ['Quilometragem'], inplace = True)

dataset



