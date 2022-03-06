# Criandos os nomes

import pandas as pd

nomes_f = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=20&sexo=f")
nomes_m = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=20&sexo=m")

# com o comando .sample pegamos uma amostra aleatória do dataset que é alterada a cada recarregamento do comando
nomes_f.sample(5)

nomes_m.sample(5)

print('Quantidade de nomes: ' + str(len(nomes_f) + len(nomes_m)))

frames = [nomes_f, nomes_m]

# inserindo os dois bd em uma variável lista e utilizando os comandos .concat e .to_frame podemos criar um novo bd com a concatenação dos dados. Entre [] foi possível definir um único campo a ser concatenado
nomes = pd.concat(frames)['nome'].to_frame()
nomes.sample(5)

"""# Incluindo ID dos alunos"""

import numpy as np
np.random.seed(123)

total_alunos = len(nomes)
total_alunos

# com o comando .random.permutation criamos uma coluna id com números aleatórios entre o intervalor do campo amostral
nomes["id_aluno"] = np.random.permutation(total_alunos) + 1

nomes.sample(3)

dominios = ['@dominiodoemail.com.br', '@servicodoemail.com']
nomes['dominio'] = np.random.choice(dominios, total_alunos)

nomes.sample(5)

nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()

nomes.sample(5)

"""# Criano a tabela cursos"""

!pip3 install html5lib
!pip3 install lxml

import html5lib

url = 'http://tabela-cursos.herokuapp.com/index.html'
cursos = pd.read_html(url)
cursos

type(cursos)

# sendo o resultado da tabela uma lista com um único item, filtrando essa info em uma nova variável transformamos a tabela html em um df
cursos = cursos[0]

type(cursos)

cursos.head()

"""# Alterando index de cursos"""

cursos = cursos.rename(columns = {'Nome do curso' : 'nome_do_curso'})

cursos.head(2)

cursos['id'] = cursos.index + 1

cursos.head()

cursos = cursos.set_index('id')

cursos.head()

"""# Matriculando os alunos nos cursos"""

nomes.sample(5)

nomes['matriculas'] = np.ceil(np.random.exponential(size=total_alunos) * 1.5).astype(int)

nomes.sample(5)

nomes.matriculas.describe()

# o seaborn é um biblioteca focada na visualização de dados baseada no matplotlib
import seaborn as sns

# com o comando .distplot montamos um gráfico do tipo hist
sns.distplot(nomes.matriculas)

nomes.matriculas.value_counts()

nomes.sample(5)

"""# Selecionando cursos"""

nomes.sample(3)

todas_matriculas = []
x = np.random.rand(20)
prob = x / sum(x)

for index, row in nomes.iterrows():
  id = row.id_aluno
  matriculas = row.matriculas
  for i in range(matriculas):
    mat = [id, np.random.choice(cursos.index, p = prob)]
    todas_matriculas.append(mat)

matriculas = pd.DataFrame(todas_matriculas, columns = ['id_aluno', 'id_curso'])

matriculas.head(5)

matriculas.groupby('id_curso').count().join(cursos['nome_do_curso']).rename(columns={'id_aluno':'quantidade_de_alunos'})

nomes.sample(5)

cursos.head()

matriculas.head()

matriculas_por_curso = matriculas.groupby('id_curso').count().join(cursos['nome_do_curso']).rename(columns={'id_aluno':'quantidade_de_alunos'})

matriculas_por_curso.head()



"""# Saídas em diferentes formatos"""

matriculas_por_curso.head()

matriculas_por_curso.to_csv('matriculas_por_curso.csv', index = False)

pd.read_csv('matriculas_por_curso.csv')

# comando .to_json para transformar um bd em formato json
matriculas_json = matriculas_por_curso.to_json()

matriculas_json

# comando .to_html para transformar um df em um arquivo .html
matriculas_html = matriculas_por_curso.to_html()

# copiando o resultado do print da variável utilizada para gerar o arquivo html e colando o código no Notepad++ podemos salver o arquivo em html e abrir a tabela em algum navegados
print(matriculas_html)

"""# Criando o banco sql"""

!pip install sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, inspect # adicionando o método inspect

engine = create_engine('sqlite:///:memory:')
engine
type(engine)

matriculas_por_curso.to_sql('matriculas', engine)

inspector = inspect(engine) # criando um Inspector object
print(inspector.get_table_names()) # Exibindo as tabelas com o inspecto

"""# Buscando no banco sql"""

query = 'select * from matriculas where quantidade_de_alunos < 5'

pd.read_sql(query, engine)

pd.read_sql_table('matriculas', engine, columns=['nome_do_curso', 'quantidade_de_alunos'])

muitas_matriculas = pd.read_sql_table('matriculas', engine, columns=['nome_do_curso', 'quantidade_de_alunos'])

muitas_matriculas

muitas_matriculas.query('quantidade_de_alunos > 6')

muitas_matriculas = muitas_matriculas.query('quantidade_de_alunos > 6')
muitas_matriculas

"""# Nomes dos alunos e alunas da próxima tuma"""

matriculas_por_curso.head(20)

matriculas.head()

id_curso = 10
proxima_turma = matriculas.query("id_curso == {}".format(id_curso))
proxima_turma

nomes.sample(3)

proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))

proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome']

proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome'].to_frame()

nome_curso = cursos.loc[id_curso]
nome_curso

# comando realizado para buscar o nome do curso em um outro df
nome_curso = nome_curso.nome_do_curso
nome_curso

# comando join para juntar dois df em um único df. Com os [] simples ou duplo é possível selecionar as colunas que precisam ser exibidas no novo df resultado do join
proxima_turma = proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome'].to_frame()

proxima_turma

# comando para alterar o nome de uma coluna no df
proxima_turma.rename(columns = {'nome' : 'Alunos do curso de {}'.format(nome_curso)})

proxima_turma = proxima_turma.rename(columns = {'nome' : 'Alunos do curso de {}'.format(nome_curso)})

proxima_turma

"""# Excel"""

proxima_turma.to_excel('proxima_turma.xlsx', index = False)

pd.read_excel('proxima_turma.xlsx')

