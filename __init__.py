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
import os
import sys
import traceback
import pandas as pd
import datetime

base_path = tmp_global_obj["basepath"]

cur_path = base_path + 'modules' + os.sep + 'SQLServer_' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
if sys.maxsize > 32 and cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)

# Globals declared here
global mod_sqlserver_sessions
# Default declared here
SESSION_DEFAULT = "default"
global sesion
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
def connect_sql(driver, server, database, username=None, password=None, session=SESSION_DEFAULT):
    import urllib
    from sqlalchemy import create_engine
    import pyodbc
    
    connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database
    if username and password is not None:
        connection_string += ';UID=' + username + ';PWD=' + password
        params = urllib.parse.quote_plus("DRIVER=" + driver + ";"
                                                                "SERVER=" + server + ";"
                                                                                    "DATABASE=" + database + ";"
                                                                                                            "UID=" + username + ";"
                                                                                                                                "PWD=" + password + ";")
    else:
        connection_string += ";Trusted_Connection=yes"
        params = urllib.parse.quote_plus("DRIVER=" + driver + ";"
                                                                "SERVER=" + server + ";"
                                                                                    "DATABASE=" + database + ";"
                                                                                                            "Trusted_Connection=yes")  
    conn = pyodbc.connect(connection_string, autocommit=True)
    cursor = conn.cursor()

    mod_sqlserver_sessions[session] = {
        "connection": conn,
        "cursor": cursor,
        "engine": None,
    }
    sesion = session
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    mod_sqlserver_sessions[session]["engine"] = engine

try:
    if module == "connectionBD":

        server = GetParams('server')
        database = GetParams('database')
        username = GetParams('user')
        password = GetParams('password')
        session = GetParams('session')
        # driver = GetParams('driver') if GetParams('driver') else '{SQL Server}'
        var_ = GetParams('var')
        temp_server = server.lower()
        
        try:
            try:
                connect_sql("{SQL Server}", server, database, username, password, session)
            except Exception as e:
                print("Error with SQL Server: ", e)
                print("Trying ODBC Driver 17 for SQL Server")
                connect_sql("{ODBC Driver 17 for SQL Server}", server, database, username, password, session)
            if var_:
                SetVar(var_, True)
        except Exception as e:
            if var_:
                SetVar(var_, False)
            PrintException()
            raise e
        
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

        if (query.lower().startswith('select') and 'into' not in query.lower()) or query.lower().startswith('execute') or query.lower().startswith('exec'):
            data = []

            try:
                columns = [column[0] for column in cursor.description]

                for row in cursor:
                    ob_ = {}
                    t = 0
                    for r in row:
                        ob_[columns[t]] = str(r) + ""
                        t = t + 1
                    data.append(ob_)
            except TypeError:
                # Added to avoid errors when the query executes an Insert SP, which it would no go through the elif...
                data = cursor.rowcount, 'registros afectados' 
        elif query.lower().startswith('insert'):
            data = cursor.rowcount, 'registro insertado'

        else:
            conn.commit()
            data = cursor.rowcount, 'registros afectados'
        conn.commit()
        SetVar(var_, data)

    if module == 'InsertDB':
        session = GetParams('session')
        query = GetParams('query')
        values = GetParams('values')
        var_ = GetParams('var')
        try:
            values = values.replace("('", '("').replace("')", '")').replace("', '", '", "').replace("','", '","')
            values_ = eval(values)

            if not session:
                session = SESSION_DEFAULT

            if type(values_) == str:
                values = (values_,)
            else:
                values = values_


            query_values = "?," * len(values)
            query_values = query_values[:-1]

            query = query + " VALUES (" + query_values + ")"

            cursor = mod_sqlserver_sessions[session]["cursor"]
            conn = mod_sqlserver_sessions[session]["connection"]
            cursor.execute(query, values)

            conn.commit()
            data = cursor.rowcount, 'registros afectados'
            SetVar(var_, data)
        
        except Exception as e:
            SetVar(var_, False)
            raise e

    # if (module == "createSp"):

    #     session = GetParams('session')
    #     spQuery = GetParams("spQuery")
    #     spQuery = spQuery.replace("\n", " ")
    #     spName = GetParams("spName")
    #     query = f"CREATE PROCEDURE dbo.sp{spName} AS BEGIN {spQuery} END"

    #     if not session:
    #         session = SESSION_DEFAULT

    #     cursor = mod_sqlserver_sessions[session]["cursor"]
    #     conn = mod_sqlserver_sessions[session]["connection"]
    #     conn.execute(query)
    #     conn.commit()

    if (module == "createSp"):

        session = GetParams('session')
        spQuery = GetParams("spQuery")
        spQuery = spQuery.replace("\n", " ")
        spName = GetParams("spName")
        spVariables = GetParams("spVariables")

        query = f"CREATE PROCEDURE dbo.{spName} {spVariables} AS BEGIN {spQuery} END"

        if not session:
            session = SESSION_DEFAULT

        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]
        conn.execute(query)
        conn.commit()

    if (module == "deleteSp"):

        session = GetParams('session')
        spName = GetParams("spName")
        query = f"DROP PROCEDURE dbo.{spName}"

        if not session:
            session = SESSION_DEFAULT

        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]
        conn.execute(query)
        conn.commit()

    if (module == "getHtmlSps"):

        session = sesion

        query = "SELECT name FROM dbo.sysobjects WHERE TYPE = 'P' AND CATEGORY = 0"
        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]
        cursor.execute(query)
        SpsGot = []

        for i in cursor:
            SpsGot.append(i[0])
        
        SetVar("SQLServer__fake_var", {
            "spsGot" : SpsGot,
        })
        

    if (module == "getSelectSps"):
        
        session = GetParams('session')
        spIframe = GetParams("iframe")
        tableWithVariables = ""
        try:
            tableWithVariables = eval(spIframe)["table"]
        except:
            pass
        spToExecute = eval(spIframe)["spGot"]

        spVariables = ""

        if tableWithVariables:
            for value in tableWithVariables:
                if not value["name"] == "":

                    if value["type"] == "date":
                        if not isinstance(value["value"], datetime.datetime):
                            try:
                                value["value"] = value.strftime('%Y-%m-%d %H:%M:%S')
                            except:
                                pass
                    spVariables += "@" + value["name"] + " = " + value.get('value', ) + ", "

            if spVariables != "":
                spVariables = spVariables[:-2]
        
        query = ""
        
        spVariables = spVariables.replace("\"", "'")
        query = f"DECLARE @return_value int EXEC @return_value = dbo.{spToExecute} {spVariables} SELECT 'Return Value' = @return_value"
        query = replaceByVar(obj_['vars']['robot'],query)
        print("*****\n\n'", query, "\n\n************")
        # print(query)

        if not session:
            session = SESSION_DEFAULT

        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]
        cursor.execute(query)
        
        resultData = []
        try:
            for i in cursor:
                resultData.append(i)
        except Exception as e:
            print(e)

        conn.commit()
        
        whereToStoreData = GetParams('whereToStoreData')
        SetVar(whereToStoreData, resultData)

    if (module == "getSps"):

        session = GetParams('session')
        query = "SELECT name FROM dbo.sysobjects WHERE TYPE = 'P' AND CATEGORY = 0"

        if not session:
            session = SESSION_DEFAULT

        cursor = mod_sqlserver_sessions[session]["cursor"]
        conn = mod_sqlserver_sessions[session]["connection"]
        cursor.execute(query)
        resultData = []

        for i in cursor:
            resultData.append(i[0])

        whereToStoreData = GetParams('whereToStoreData')
        SetVar(whereToStoreData, resultData)

    if module == 'ExportData':
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
            app = xw.App(visible=False)
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
            app.kill()

    if module == 'importData':

        path_file = GetParams('path_file')
        hoja = GetParams('hoja')
        schema = GetParams('schema') if GetParams('schema') else 'dbo'
        tabla = GetParams('tabla')
        chunk = GetParams('chunk')
        method = GetParams('method')
        session = GetParams('session')

        if not session:
            session = SESSION_DEFAULT

        if chunk:
            chunk = int(chunk)
        else:
            chunk = None
        
        if not method or method == "None":
            method = None
        
        engine = mod_sqlserver_sessions[session]["engine"]

        if hoja:
            df = pd.read_excel(path_file, sheet_name=hoja, engine='openpyxl')
        else:
            df = pd.read_excel(path_file, engine='openpyxl')

        df.to_sql(tabla, con=engine, schema=schema, if_exists='append', index=False, chunksize=chunk, method=method)

    if module == "close":
        session = GetParams('session')
        if not session:
            session = SESSION_DEFAULT

        conn = mod_sqlserver_sessions[session]["connection"]
        conn.close()
        mod_sqlserver_sessions[session] = {}


except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e