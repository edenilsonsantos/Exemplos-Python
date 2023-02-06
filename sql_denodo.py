def api2_consulta_denodo(banco_dados, tabela, colunas, filtro=''):
    ### Requisitos: Instalar as biliotecas abaixo no terminal do vscode ou pycharm
    ## python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip pandas
    ## python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip sqlalchemy
    ## python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip mysql-connector-python
    ## python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip psycopg2
    ## python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip --upgrade denodo-sqlalchemy

    import os
    import pandas as pd
    from sqlalchemy import create_engine
    server = 'virtualizador.hostname.net'
    user_denodo = 'rpa_sede_denodo'
    pwd_denodo = os.getenv('passwd_denodo')


    conexao = create_engine(f'denodo://{user_denodo}:{pwd_denodo}@{server}:9996/{banco_dados}')
    sql = f"SELECT {colunas} FROM {tabela} where {filtro}"
    df = pd.read_sql_query(sql, conexao)
    print(df)




api2_consulta_denodo('ldw', 'colaboradores_por_cargo', 'codigo_centro_custo', f"cod_ldap eq 'miriam_anaa'")



