# Dicas da Biblioteca Pandas

##############################################################################
## Instalar a biblioteca Pandas
python -m pip install pandas
ou
python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip pandas

##############################################################################
## Importar a biblioteca Pandas
import pandas as pd


##############################################################################
## Criar dataframes
# veja 3 formas de criar um mesmo dataframe do zero com dados inciais
dados = [[1,2,3],[4,5,6],[7,8,9]]
df1 = pd.DataFrame(dados, columns=['a', 'b', 'c'])
print(df1)
print()


dados = {'a': [1,4,7], 'b':[2,5,8], 'c': [3,6,9]}
df2 = pd.DataFrame(dados)
print(df2)
print()


dados = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}, {'a': 7, 'b': 8, 'c': 9}]
df3 = pd.DataFrame(dados)
print(df3)
print()


##############################################################################
# criar dataframe vazio, sem a coluna indice de linhas
df = pd.DataFrame(index= None)

# criar dataframe a partir do excel xls (requisito: pip install xlrd)
df = pd.read_excel("C:\\Temp\\planilha.xls", engine="xlrd", sheet_name=0 )

# criar dataframe a partir do excel xlsx
df = pd.read_excel("C:\\Temp\\planilha.xlsx")

# criar dataframe a partir do excel xlsx, selecionando a guia da planilha, e limitando num_linhas que vai ler
df = pd.read_excel("C:\\Temp\\planilha.xlsx", sheet_name=0, nrows=10)
df = pd.read_excel("C:\\Temp\\planilha.xlsx", sheet_name='Plan1', nrows=10)

# criar dataframe, ignorando as 10 primeiras linhas (skiprows), usando converters para preencher com zeros a esquerda a coluna CPF e CNPJ
df3 = pd.read_excel("C:\\Temp\\planilha.xlsx", sheet_name=0, skiprows=range(0, 10), converters={'CNPJ da Instituição': '{:0>14}'.format, 'CPF': '{:0>11}'.format})


# criar dataframe a partir de arquivo CSV, defina qual o separador('' ou ',' ou ';')
df = pd.read_csv("C:\\Temp\\file.csv", sep=';')


##############################################################################  
## Colunas do DataFrame
# Obter lista de nomes das colunas
colunas = df3_dados_iniciais.columns.values.tolist() 

# reordenar colunas  pelo nome da coluna, ou filtrar apenas as colunas desejadas
df = df[["Nr.Contrato do Convênio", "Vl.Descontado", "Cód.Verba", "Data", "CPF", "Matrícula", "Nome"]]

# deletar colunas
#drop one column by name
df.drop('column_name', axis=1, inplace=True)

#drop multiple columns by name
df.drop(['column_name1', 'column_name2'], axis=1, inplace=True)

#drop one column by index
df.drop(df.columns[[0]], axis=1, inplace=True)

#drop multiple columns by index
df.drop(df.columns[[0,2,5]], axis=1, inplace=True)


# selecionar parcialmente 2 colunas
novo_df = df[['nome_coluna3','nome_coluna5']])

# adicionar nova coluna  'nova1' no final das colunas existentes, e com valor '0'
df['nova1'] = '0'
  
# adicionar nova coluna 'nova2' na posicao coluna 15, com valor padrão '0' em todas a linhas
df.insert(loc=15, column='nova2', value='0')

# renomear o titulo da coluna: exemplo de nome 'data lançamento' para novo nome 'data_lanc'
df.rename(columns={'data lançamento': 'data_lanc'}, inplace=True)
  
# converte toda a coluna para um tipo de dados específico, exemplos abaixo
df['SALDO'] = df['SALDO'].astype(int)  
df['DESCRICAO'] = df['DESCRICAO'].astype(str)
df['DATA_VCTO'] = df['DATA_VCTO'].astype('datetime64[ns]')
  

##############################################################################
## Convert posição do DataFrame para String
# criar string, ou lista de string
cpf_cnpj = df.iloc[0,:].to_string(header=False, index=False)
    
arr = df.iloc[0,:].apply(str).values
cpf_cnpj = arr[0]


##############################################################################
## Pesquisa por referencia, condição
# exemplo: pesquisa se o valor da coluna [ID] == 2012, se encontrar me retorne valor da coluna [cpf] na mesma linha do ID 2012
variavel_cpf = df.query('id==2012')['cpf'].values[0]

# trocando valor em linhas da coluna, baseado em condição, se na coluna data tiver 'qualquer coisa + 2021', troca o valor por um novo_valor
df['Data'] = df.Data.str.replace(r'(.*2021)', 'novo_valor')
# novo metodo replace(to_replace...)
df['tel_associado'].replace(to_replace=r"^(0+)", value="", inplace=True, regex=True)

# localiza no dataframe na coluna data, os campos cuja 6ª posicao até o fim é = 2021
# se envontrar, troca o valor da coluna CPF por um novo_valor ( cpf + ok )
df.loc[df.Data.str[6:]=='2021','CPF']= df.CPF + ' ok'

# exemplo se localizar linhas com valor 'apple' na coluna_a, substituir o valor da coluna_b na mesma linha (neste caso novo valor='0')
df.loc[df['coluna_a'] == 'apple', 'coluna_b'].replace(r'0', 'novo_valor',inplace=True, regex=True)

# outro exemplo de localizar e substituir (neste exemplo substitui o ponto por vazio, em seguida substitui a virgula por ponto)
df['valor] = df['valor].apply(lambda x: float(x.replace(".","").replace(",",".")))

# add valor em campo do DF, baseado na condicao do tamanho do valor de uma celula do DF
df.loc[df.tel_associado.str.len() > 9, 'DDD'] = df.tel_associado.str[:2]
print(df['DDD'])

# exemplo de SOMASE, soma coluna baseado em condição, obs. a condição pode ser em outra coluna ou na mesma
v1 = df[['VALOR']].sum(axis=1).where(df['CODIGO_LANCAMENTO'] == 'DEBITO', 0)
total_deb = sum(v1)

# exemplo where em dataframe, montando df2 em que possui apenas a coluna valor, cujo filtramos a coluna id do DF anterior
id_campo = '1535'
df1 = df_atributos[['valor']].where(df_atributos['id'] == id_campo, 0)
filtro = df1['valor'] != 0
df2 = df1[filtro]
 


##############################################################################
## Substring, Update valor da coluna

# exemplo: atualizar a coluna 'CPF' - adicionar a pontuação ( ponto e traço )
df['CPF'] = df['CPF'].astype(str)
df['CPF'] = df['CPF'].str[:3] + '.' + df['CPF'].str[3:6] + '.' + df['CPF'].str[6:9] + '-' + df['CPF'].str[9:11]
 


##############################################################################
## Filtros (Manter)
Filtrando o que deseja manter do DataFrame
# dias_sem_transacionar maior que 365 ou dias_sem_transacionar é null(NaN)
df["dias_sem_transacionar"] = df["dias_sem_transacionar"].astype('float')
df = df.query('(dias_sem_transacionar > 365) or (dias_sem_transacionar != dias_sem_transacionar)')
# ou
df = df.query('(dias_sem_transacionar > 365) or (dias_sem_transacionar.isnull())', engine='python')

# filtar, manter apenas linhas em que a coluna email, contenha 'qualquer_nome@sicredi.com.br', remover demais linhas do DF
df = df.query('email.str.contains("@sicredi.com.br")', engine='python') # retona o valor da coluna
# nao contains
df = df[~df["produto"].str.contains("POUP")]
new_df = df[~df["col"].str.contains(word)]
new_df = df[df["col"].str.contains(word) == False]
new_df = !(df["col"].str.contains(word))
df = df.email.str.contains('.*@sicredi.com.br') # retorna verdadeiro ou falso

# exemplos de condição para selecionar as linhas que deseja manter no DataFrame
df2 = df.query('coluna_name_a > 50 and coluna_name_b > 80')
df3 = df.query('coluna_name_a == "jan" or coluna_name_b == "2022"')

# filtrar as linhas cujo valor da coluna 'ATRASO' esteja entre 90 e 1800 dias
df_filtro = df['ATRASO'].between(90, 1800)  
df2 = df[df_filtro]
   
 
############################################################################## 
## Filtros (Remover)
Filtrando o que deseja remover do DataFrame
# remove as linhas do dataframe, cuja coluna CPF, conter valor duplicado, implace(em tempo real) - mantém ao menos 1 item entre os duplicados
df.drop_duplicates(subset=['CPF'], inplace=True)  

# remove as linhas do dataframe, cuja coluna CPF, conter valor duplicado, implace(em tempo real) - não mantém nenhum item dos apontados como duplicado
data.drop_duplicates(subset=['CPF'], keep=False, inplace=True)

# remove as linhas do dataframe, cuja coluna CPF, conter valor vazio ou NaN
df.dropna(subset=['CPF'], inplace=True)

# remover as linhas em que a coluna [CPF] tem o valor vazio
filtro = df['CPF_CNPJ'] != ""
df2 = df[filtro]
    
############################################################################## 
## Incrementar, empilhar linhas de dados em DataFrame
Exemplo1: Juntar 2 DataFrames Existentes
Exemplo2: Cria df DataFrame temporário de uma linha dentro de um LOOP, e vai incrementando um novo df2

novo_df = pd.concat([df1, df2])

# Add linhas no dataframe destino
colunas = [
    'CODIGO',
    'SALDO',
    'CPF_CNPJ'
]
             for linha, valor in df.iterrows():
                CODIGO = str(valor['CODIGO'])
                SALDO = str(valor['SALDO'])
                CPF_CNPJ = str(valor['CPF_CNPJ'])
                
                df1 = pd.DataFrame([{
                    'CODIGO': CODIGO,
                    'SALDO': SALDO,
                    'CPF_CNPJ': CPF_CNPJ}], columns=colunas, index= None)
                df2 = pd.concat([df1, df2])
print(df2)
 
  

 
##############################################################################  
## Comparar 2 DataFrames
# comparar DataFrame 'a' com DataFrame 'b' se encontar uma linha repetida em ambos, 
# remover do DF 'a', por fim, guardar o que restar no DF 'a' no novo_df

novo_df = (pd.merge(a,b, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)) 

# manter a linha no df, se o valor na coluna conta_corrente do df, esta igual ao valor conta_corrente no df_cartao_debito
df = df[df['conta_corrente'].isin(df_cartao_debito['conta_corrente'])] 



##############################################################################
## Agrupar DataFrame
# neste exemplo abaixo vou agrupar o DF pela coluna [CPF]
# ou seja os valores duplicados da coluna [CPF], serão indices de grupos
# o que ocorre com os dados das demais colunas ao agrupar?
# existem parametros para usar com o groupby, neste caso vou usar 2
# Nas colunas [CPF] e [NOME], uso o comando 'first' que vai manter o primeiro valor encontrado 
# Nas colunas [DEBITO] e [CREDITO], uso o comando 'sum' que vai somar os valores do que foi agrupado de cada CPF 
# df.groupby(['name', 'month'], as_index = False).agg({'text': ' '.join})

df2 = df.groupby(['CPF'],as_index=False).agg({
        'CPF': 'first', 'NOME': 'first', 'DEBITO': 'sum', 'CREDITO': 'sum'
        }) 
 


##############################################################################
## Exportar salvar saída do DataFrame
# Exportar DF para Excel
df.to_excel("C:\\Temp\\relatorio.xlsx", index=False)


# Exportar DF para Excel, salvar em guias/abas diferentes no mesmo arquivo 
writer = pd.ExcelWriter(f'c:\\temp\\relatorio.xlsx', engine = 'xlsxwriter')

df_plan1.to_excel(writer, index=False, sheet_name='Plan1')
workbook  = writer.book
worksheet = writer.sheets['Plan1']

df_plan2.to_excel(writer, index=False, sheet_name='Plan2')
workbook  = writer.book
worksheet = writer.sheets['Plan2']

df_plan3.to_excel(writer, index=False, sheet_name='Plan3')
workbook  = writer.book
worksheet = writer.sheets['Plan3']

writer.save()


# Exportar DF para CSV
df.to_csv("C:\\Temp\\relatorio.csv", sep=';', index=None)
 
 
##############################################################################
##############################################################################
## Consultar MySQL e Salvar em DataFrame
# requisitos
# pip install mysql-connector-python
# pip install SQLAlchemy
# pip install pandas

import pandas as pd
import os

##############################################################################
# autenticando a conexao
def conect_sql_alchemy():
    from sqlalchemy import create_engine
    server = 'IP ou Host aqui'
    user_planning = 'usuario com acesso ao BD'
    pwd_planning = os.getenv('senha_credencial_var_ambiente')
    db = 'planning'
    engine = create_engine(f'mysql+mysqlconnector://{user_planning}:{pwd_planning}@{server}/{db}', pool_recycle=3600)
    return engine
    
##############################################################################
# realizando a consulta, e convertendo em DataFame
def select_movimentacao(num_conta):
    engine = conect_sql_alchemy()
    sql = f"SELECT * FROM movimentacao_financeira WHERE num_conta = '{num_conta}' AND dat_operacao >= '2021-03-01 00:00:00' " 
    df = pd.read_sql(sql, con=engine)
    return df

df = select_movimentacao('12345-6')
print(df)

##############################################################################
## Insert SQL para DB 
def input_in_tabela_planning(df):
    from sqlalchemy import create_engine
    server = 'IP ou Host aqui'
    user_planning = 'usuario com acesso ao BD'
    pwd_planning = os.getenv('senha_credencial_var_ambiente')
    db = 'fluid'
    engine = create_engine(f'mysql+mysqlconnector://{user_planning}:{pwd_planning}@{server}/{db}', pool_recycle=3600)
    df.to_sql('nome_da_tabela', engine, if_exists='append', index = False)
    # df.to_sql('nome_da_tabela', engine, if_exists='replace', index = False)
    print('Input realizado com sucesso no BD')


