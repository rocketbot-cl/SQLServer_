



# SQLServer
  
Conéctese a SQL Server y administre todas sus bases de datos, ejecute consultas personalizadas, importe y exporte datos, cree y ejecute procedimientos almacenados.  

*Read this in other languages: [English](Manual_SQLServer_.md), [Português](Manual_SQLServer_.pr.md), [Español](Manual_SQLServer_.es.md)*
  
![banner](imgs/Banner_SQLServer_.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conexión a SQLServer
  
Conectarse a la base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión|Conn1|
|Servidor|Nombre del servidor|DESKTOP-T2319IB\SQLEXPRESS|
|Driver|Nombre del driver|{ODBC Driver 17 for SQL Server}|
|Nombre de BD|Nombre de la base de datos|test|
|Usuario de la BD|Usuario de la base de datos|usertest|
|Contraseña de BD|Contraseña del usuario de la base de datos|passtest|
|Asignar a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Consulta SQLServer
  
Hacer una consulta a una base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Consulta SQL|Consulta que se ejecutará en la base de datos|select * from test|
|Sesión|Nombre de la sesión de conexión|Conn1|
|Asignar a variable|Nombre de la variable a la que se asignará el resultado de la consulta|Variable|

### Insertar SQLServer
  
Insertar datos en una base de datos SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Insert Query|Insert a ejecutar, sin incluir los valores|insert into test (id, name)|
|Valores|Valores a insertar en la tabla, cada valor debe estar entre comillas simples y separados por comas|('15', 'Rocketbot')|
|Sesión|Nombre de la sesión a utilizar|Conn1|
|Asignar a variable|Asignar el resultado a una variable|Variable|

### Exportar datos
  
Exportar datos desde una base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión a utilizar|Conn1|
|Consulta SQL|Consulta SQL a ejecutar|select * from test|
|Ruta del archivo|Ruta del archivo a exportar|Ruta|
|Ruta del archivo base|Archivo base. Es de utilidad en caso de que se quiera exportar con un formato o cabeceras específicas|Ruta|
|Nombre de hoja|Nombre de la hoja donde se va a exportar|Hoja1|
|Celda|Celda donde se va a exportar|Celda|

### Importar datos
  
Importar datos a una base de datos SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión de conexión|Conn1|
|Nombre de hoja|Nombre de la hoja de cálculo a importar|Hoja1|
|Schema de la tabla|Esquema de la tabla SQL a importar. Por defecto, dbo.|dbo|
|Nombre de la tabla a importar|Nombre de la tabla SQL donde se importarán los datos. Si no existe, se creará.|Tabla|
|Ruta del archivo base|Ruta del archivo base a importar|Ruta|
|Tamaño del lote|Las filas se escribirán en lotes de este tamaño a la vez. Por defecto, todas las filas se escribirán a la vez.|2000|
|Metodo|||

### Descarga Archivo
  
Descarga Archivos desde una base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión a utilizar|Conn1|
|Consulta SQL|Consulta SQL a ejecutar|EXEC up_Archivos_Select @IdArchivoTipo = 56, @IdPropietario = 1718029|
|Ruta donde se guardara el archivo|Ruta donde se guardara el archivo|C:/Users/Downloads/|
|Columna que almacena el nombre del archivo|Nombre de la columna que almacena el nombre del archivo|Documento|
|Columna que almacena el contenido del archivo|Nombre de la columna que almacena el contenido del archivo|Archivo|

### Crear un SP con variables
  
Crea un Store Procedure con variables
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión|Conn1|
|Nombre del SP|Nombre del SP|TestDB_GetAll|
|Variables del SP|Variables del SP (separadas por coma)|@LastName nvarchar(50), @FirstName nvarchar(50)|
|Query|Query del SP (lo contenido entre BEGIN y END)|SELECT * FROM dbo.Table WHERE LastName = @LastName AND FirstName = @FirstName|

### Obtener SPs
  
Obtén los Store Procedures disponibles
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión|Conn1|
|Asignar a variable|Asignar el resultado a una variable|Variable|

### SP a ejecutar
  
Para ver los SP debes conectarte a la DB sin cerrar la conexion hasta que hayas seleccionado el Store Procedure
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione el SP|Para ver los SP debes conectarte a la DB sin cerrar la conexion hasta que hayas seleccionado el Store Procedure||
|Sesión|Nombre de la sesión|Conn1|
|Esquema|Nombre del esquema|dbo|
|Asignar a variable|Variable donde se guardará el resultado|Variable|

### Borrar un SP
  
Eliminar el Store Procedure indicado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión|Conn1|
|Nombre del SP|Nombre del Store Procedure|TestDB_GetAll|

### Cerrar conexión
  
Cierra la conexión con SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
