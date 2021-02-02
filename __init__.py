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
import pyodbc

global cursor
global conn

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

"""
    Obtengo variables
"""
if module == "connectionBD":

    server = GetParams('server')
    database = GetParams('database')
    username = GetParams('user')
    password = GetParams('password')
    result = GetParams('result')

    driver = "{SQL Server}"
    if server.endswith("database.windows.net"):
        driver = '{ODBC Driver 17 for SQL Server}'
    # print(driver)
    try:

        if username and password is not None:

            conn = pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        else:

            conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database)

        cursor = conn.cursor()
        if result:
            SetVar(result, True)

    except Exception as e:
        if result:
            SetVar(result, False)
        PrintException()
        raise e

if module == 'QueryBD':

    query = GetParams('query')
    var_ = GetParams('var')
    data = False

    try:

        cursor.execute(query)
        if query.lower().startswith(('call', 'exec')):
            data = cursor.fetchall()

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

        # elif query.lower().startswith('insert'):
        #     data = cursor.rowcount, 'registro insertado'
        #     #data = True

        else:
            conn.commit()
            data = cursor.rowcount, 'registros afectados'

        conn.commit()
        SetVar(var_, data)

    except Exception as e:
        PrintException()
        raise e

if module == "close":
    conn.close()
    cursor = None