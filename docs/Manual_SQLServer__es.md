# SQLServer
  
Módulo para interactuar con SQL Server con consultas y SPs  
  
![banner](imgs/Banner_SQLServer_.jpg)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Conexión a SQLServer
  
Conectarse a la base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
|Servidor||DESKTOP-T2319IB\SQLEXPRESS|
|Nombre de BD||test|
|Usuario de la BD||usertest|
|Contraseña de BD||passtest|

### Consulta SQLServer
  
Hacer una consulta a una base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Consulta SQL||select * from test|
|Sesión||Conn1|
|Asignar a variable||Variable|

### Exportar datos
  
Exportar datos desde una base de datos de SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
|Consulta SQL||select * from test|
|Ruta del archivo||Ruta|
|Ruta del archivo base||Ruta|
|Nombre de hoja||Hoja1|
|Celda||Celda|

### Importar datos
  
Importar datos a una base de datos SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
|Nombre de hoja||Hoja1|
|Nombre de la tabla a importar||Tabla|
|Ruta del archivo base||Ruta|

### Crear un SP con variables
  
Crea un Store Procedure con variables
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
|Nombre del SP||TestDB_GetAll|
|Variables del SP||@LastName nvarchar(50), @FirstName nvarchar(50)|
|Query||SELECT * FROM dbo.Table WHERE LastName = @LastName AND FirstName = @FirstName|

### Obtener SPs
  
Obtén los Store Procedures disponibles
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
|Asignar a variable||Variable|

### SP a ejecutar
  
Para ver los SP debes conectarte a la DB sin cerrar la conexion hasta que hayas seleccionado el Store Procedure
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione el SP|||
|Sesión||Conn1|
|Asignar a variable||Variable|

### Borrar un SP
  
Eliminar el Store Procedure indicado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
|Nombre del SP||TestDB_GetAll|

### Cerrar conexión
  
Cierra la conexión con SQLServer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
