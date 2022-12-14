# Exemplos MYSQL com Python e também com Pnadas e SQLALCHEMY

## Exemplos MySQL - CRUD
# requisitos
# pip install mysql-connector-python
# pip install pandas
# Configure driver denodo odbc no windows

import mysql.connector
from datetime import datetime, timedelta
import time
import os
import socket

##################################################################################
def conect_mysql():
    pwd_bd = os.getenv('senha_var_ambiente')
    conexao = mysql.connector.connect(host='IP_ou_HOSTNAME', database='grafana', user='rpa', password=pwd_bd)
    return conexao
    
##################################################################################    
def consultar_fila(str_cod_status):
    try:
        connection = conect_mysql()
        cursor = connection.cursor()
        sql_select_query = f"SELECT * FROM Fila_Rpa WHERE Cod_Status = '{str_cod_status}' AND Nome_VM = 'VM_RPA_001' ORDER BY Prioridade, Data_Agenda"
        cursor.execute(sql_select_query)
        rows = cursor.fetchall()
        total_linhas = cursor.rowcount
        print("Total number of rows in table: ", total_linhas)

        if total_linhas == 0:
            arr_rpa = ['', '', '', '','', '', '']
            print(datetime.now().strftime('%d/%m/%Y %H:%M'),'A fila retornou vazia')
            time.sleep(2)
            return arr_rpa, total_linhas
        else:
            # Pega a primeira linha baseado order by prioridade, data_agenda
            id_rpa = str(rows[0][0])
            cod_rpa = str(rows[0][1])
            cod_setor = str(rows[0][2])
            cod_status = str(rows[0][3])
            nome_vm = str(rows[0][4])
            prioridade = str(rows[0][5])
            data_agenda = str(rows[0][6])
            arr_rpa = [id_rpa, cod_rpa, cod_setor, cod_status, nome_vm, prioridade, data_agenda]
            print(f"|Cod_Rpa: {cod_rpa} |Status: {cod_status} |VM: {nome_vm} |Prioridade: {prioridade} |Data: {data_agenda} \n")
            return arr_rpa, total_linhas
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        try:
            connection.close()
            cursor.close()
        except:
            pass
            
            
            
##################################################################################            
def update_fila(str_cod_rpa, str_cod_status, str_prioridade):
    try:
        connection = conect_mysql()
        cursor = connection.cursor()
        sql_select_query = f"SELECT * FROM Fila_Rpa WHERE Cod_Rpa = '{str_cod_rpa}' AND Cod_Status = '{str_cod_status}'"
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)
        # Update single record now
        sql_update_query = f"UPDATE Fila_Rpa SET Cod_Status = '{str_cod_status}' , Prioridade = '{str_prioridade}' WHERE Cod_Rpa = '{str_cod_rpa}'"
        cursor.execute(sql_update_query)
        connection.commit()
        print("Record Updated successfully ")
    except mysql.connector.Error as error:
        print("Failed to update table record: {}".format(error))
    finally:
        try:
            connection.close()
            cursor.close()
        except:
            pass
            
            
##################################################################################            
def insert_historico(data_inicio, cod_rpa, cod_setor, qtd_atividades, cod_status, msg_log):
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        data_fim = datetime.now()
        # Convert para segundos
        d1_ts = time.mktime(data_inicio.timetuple())
        d2_ts = time.mktime(data_fim.timetuple())
        # Convert para minutos
        tempo_min = ((d2_ts - d1_ts) / 60) 
        data_dif = int(tempo_min)
        # convert para o formato do banco de dados
        dta_inicio = data_inicio.strftime("%Y-%m-%d %H:%M:%S")
        dta_fim = data_fim.strftime("%Y-%m-%d %H:%M:%S")
        dta_tempo = str(data_dif)

        # define o tempo minimo de 1 minuto
        if dta_tempo == '0':
            dta_tempo = '1'
            
        connection = conect_mysql()
        cursor = connection.cursor()
        sql = "INSERT INTO Historico_Rpa(Cod_Rpa, Cod_Setor, Data_Inicio, Data_Fim, Nome_VM, IP_VM, Cod_Status, Log_Message) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(cod_rpa, cod_setor, dta_inicio, dta_fim, hostname, ip, cod_status, msg_log))
        connection.commit()
        # print("Insert successfully ")
    except mysql.connector.Error as error:
        print("Failed to insert fila fluid: {}".format(error))
        pass
    finally:
        try:
            connection.close()
            cursor.close()
        except:
            pass 


##################################################################################
##################################################################################
## Consultar MySQL e Salvar em DataFrame

# requisitos
# pip install mysql-connector-python
# pip install SQLAlchemy
# pip install pandas

import pandas as pd
import os

##################################################################################
# autenticando a conexao no planning
def conect_sql_alchemy():
    from sqlalchemy import create_engine
    server = 'IP ou Host aqui'
    user_planning = 'usuario com acesso ao BD'
    pwd_planning = os.getenv('senha_credencial_var_ambiente')
    db = 'planning'
    engine = create_engine(f'mysql+mysqlconnector://{user_planning}:{pwd_planning}@{server}/{db}', pool_recycle=3600)
    return engine

##################################################################################
# realizando a consulta, e convertendo em DataFame
def select_movimentacao(num_conta):
    engine = conect_sql_alchemy()
    sql = f"SELECT * FROM movimentacao_financeira WHERE num_conta = '{num_conta}' AND dat_operacao >= '2021-03-01 00:00:00' " 
    df = pd.read_sql(sql, con=engine)
    return df

df = select_movimentacao('12345-6')
print(df)


##################################################################################
## Insert SQL para DB 
def input_in_tabela_planning(df):
    from sqlalchemy import create_engine
    server = 'IP ou Host aqui'
    user_planning = 'usuario com acesso ao BD'
    pwd_planning = os.getenv('senha_credencial_var_ambiente')
    db = 'fluid'
    engine = create_engine(f'mysql+mysqlconnector://{user_planning}:{pwd_planning}@{server}/{db}', pool_recycle=3600)
    df.to_sql('nome_da_tabela', engine, if_exists='append', index = False)
    print('Input realizado com sucesso no BD')



##################################################################################
## Consultar SQL Denodo e Salvar em DataFrame
# requisitos
# pip install pyodbc
# pip install pandas
# Configure driver denodo odbc no windows

##################################################################################
def denodo_conex():
    import pandas as pd
    import pyodbc as dbdriver
    from socket import gethostname
    denodoserver_dsn = 'nome_configuracao no driver - exemplo: DenodoODBC'
    denodo_db='nome_db'
    client_hostname = gethostname()
    useragent = '%s-%s' % (dbdriver.__name__,client_hostname)
    conexao = dbdriver.connect( 'DSN=%s;UserAgent=%s' % ( denodoserver_dsn , useragent), database=denodo_db, timeout=3600)
    sql = f"SELECT *  FROM ldw.consorcio_carteira_gestor_atual WHERE (data_contemplacao is null) limit 10"
    df = pd.read_sql(sql, conexao)
    return df

df = denodo_conex()
print(df)  
``` 
