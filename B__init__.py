# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
try:
    import os
    import sys
    import pyodbc
    import pandas as pd
    import urllib

    base_path = tmp_global_obj["basepath"]
    cur_path = base_path + 'modules' + os.sep + 'SQLServer_' + os.sep + 'libs' + os.sep
    if cur_path not in sys.path:
        sys.path.append(cur_path)
    from sqlalchemy import create_engine
except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
    PrintException()
    raise e

# Globals declared here
global mod_sqlserver_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_sqlserver_sessions:
        mod_sqlserver_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_sqlserver_sessions = {SESSION_DEFAULT: {}}
"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

"""
    Obtengo variables
"""
try:
    if module == "connectionBD":

        server = GetParams('server')
        database = GetParams('database')
        username = GetParams('user')
        password = GetParams('password')
        session = GetParams('session')

        if not session:
            session = SESSION_DEFAULT

        driver = "{SQL Server}"
        if server.endswith("database.windows.net"):
            driver = '{ODBC Driver 17 for SQL Server}'

        connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database
        if username and password is not None:
            connection_string += ';UID=' + username + ';PWD=' + password
            params = urllib.parse.quote_plus("DRIVER=" + driver + ";"
                                                                  "SERVER=" + server + ";"
                                                                                       "DATABASE=" + database + ";"
                                                                                                                "UID=" + username + ";"
                                                                                                                                    "PWD=" + password)
        else:
            params = urllib.parse.quote_plus("DRIVER=" + driver + ";"
                                                                  "SERVER=" + server + ";"
                                                                                       "DATABASE=" + database + ";"
                                                                                                                "Trusted_Connection=yes")

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        mod_sqlserver_sessions[session] = {
            "connection": conn,
            "cursor": cursor,
            "engine": None
        }

        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        mod_sqlserver_sessions[session]["engine"] = engine

    if module == 'QueryBD':
        session = GetParams('session')
        query = GetParams('query')
        var_ = GetParams('var')
        data = False

        if not session:
            session = SESSION_DEFAULT

        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]
        cursor.execute(query)

        if query.lower().startswith('select') or query.lower().startswith('execute'):
            data = []

            # print(query)

            columns = [column[0] for column in cursor.description]
            # data.append(columns)

            for row in cursor:
                # print(row)
                ob_ = {}
                t = 0
                for r in row:
                    ob_[columns[t]] = str(r) + ""
                    t = t + 1
                data.append(ob_)
        elif query.lower().startswith('insert'):
            data = cursor.rowcount, 'registro insertado'
            # data = True

        else:
            conn.commit()
            data = cursor.rowcount, 'registros afectados'
        conn.commit()
        SetVar(var_, data)

    if module == 'ExportData':
        from openpyxl import Workbook
        import xlwings as xw

        session = GetParams('session')
        query = GetParams('query')
        path_file = GetParams('path_file')
        cell_name = GetParams('cell_name')
        sheet_name = GetParams('sheet_name')
        path_file_base = GetParams('path_file_base')
        data = False

        if not session:
            session = SESSION_DEFAULT

        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]

        if query.lower().startswith('select'):

            cursor.execute(query)

            data = []

            columns = [column[0] for column in cursor.description]
            data.append(columns)

            for row in cursor:
                ob_ = {}
                t = 0
                registros = list()
                for r in row:
                    registros.append(str(r).strip())

                data.append(registros)

            if path_file_base:
                data.pop(0)
                wb = xw.Book(path_file_base)
                if sheet_name:
                    sht  = wb.sheets[sheet_name]
                else:
                    sht  = wb.sheets[0]
                
                if cell_name:
                    sht.range(cell_name).value = data
                else:
                    sht.range('A2').value = data
                wb.save(path_file)
                wb.close()
            else:
                wb = xw.Book()
                sht = wb.sheets[0]
                sht.range('A1').value = data
                wb.save(path_file)
                wb.close()

    if module == 'importData':

        path_file = GetParams('path_file')
        hoja = GetParams('hoja')
        tabla = GetParams('tabla')
        session = GetParams('session')

        if not session:
            session = SESSION_DEFAULT

        engine = mod_sqlserver_sessions[session]["engine"]

        if hoja:
            df = pd.read_excel(path_file, sheet_name=hoja, engine='openpyxl')
        else:
            df = pd.read_excel(path_file, engine='openpyxl')

        df.to_sql(tabla, con=engine, if_exists='append', index=False)

    if module == "close":
        session = GetParams('session')
        if not session:
            session = SESSION_DEFAULT

        conn = mod_sqlserver_sessions[session]["connection"]
        conn.close()
        mod_sqlserver_sessions[session] = {}


except Exception as e:
    PrintException()
    raise e