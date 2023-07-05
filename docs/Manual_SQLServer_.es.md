



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
|Tamaño del lote|Las filas se escribirán en lotes de este tamaño a la vez. Por defecto, todas las filas se escribirán a la vez.|2000|
|Metodo|||

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
