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
import pyodbc
import pandas as pd
import urllib

base_path = tmp_global_obj["basepath"]

cur_path = base_path + 'modules' + os.sep + 'SQLServer_' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32:
    if cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
else:
    if cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)

from sqlalchemy import create_engine

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
                                                                                                                                    "PWD=" + password + "; Trusted_Connection=yes")
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
            "engine": None,
        }
        sesion = session

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
                    spVariables += "@" + value["name"] + " = " + value["value"] + ", "

            if spVariables != "":
                spVariables = spVariables[:-2]
        
        query = ""
        
        spVariables = spVariables.replace("\"", "'")
        query = f"DECLARE @return_value int EXEC @return_value = dbo.{spToExecute} {spVariables} SELECT 'Return Value' = @return_value"

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
    print(traceback.print_exc())
    PrintException()
    raise e