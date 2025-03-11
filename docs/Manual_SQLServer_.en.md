



# SQLServer
  
Connect to SQLServer and manage all your databases, execute custom queries, import and export data, create and execute stored procedures.  

*Read this in other languages: [English](Manual_SQLServer_.md), [Português](Manual_SQLServer_.pr.md), [Español](Manual_SQLServer_.es.md)*
  
![banner](imgs/Banner_SQLServer_.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### SQLServer Connection
  
Connect to SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session name|Conn1|
|Server|Server name|DESKTOP-T2319IB\SQLEXPRESS|
|Driver|Driver name|{ODBC Driver 17 for SQL Server}|
|BD Name|Database name|test|
|User BD|Database user|usertest|
|Pass BD|Database user password|passtest|
|Assign to var|Variable where the result of the connection will be stored|Variable|

### Query SQLServer
  
Make a query to a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|SQL Query|Query to execute in the database|select * from test|
|Session|Connection session name|Conn1|
|Assign to var|Name of the variable to which the result of the query will be assigned|Variable|

### Insert SQLServer
  
Insert data in a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|Insert Query|Insert to execute, without including the values|insert into test (id, name)|
|Values|Values to insert in the table, each value must be in single quotes and separated by commas|('15', 'Rocketbot')|
|Session|Name of the session to use|Conn1|
|Assign to var|Assign the result to a variable|Variable|

### Export data
  
Export data from a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session to use|Conn1|
|SQL Query|SQL query to execute|select * from test|
|File path|File path to export|Path|
|Base file path|Base file. It is useful in case you want to export with a specific format or headers|Path|
|Sheet name|Name of the sheet where it will be exported|Sheet1|
|Cell|Cell where it will be exported|Cell|

### Import data
  
Import data to a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|Session|Connection session name|Conn1|
|Sheet name|Name of the spreadsheet to import|Sheet1|
|Table schema|Schema of the SQL table to import. By default, dbo.|dbo|
|Name of the table to import|Name of the SQL table where the data will be imported. If it does not exist, it will be created.|Table|
|Base file path|Base file path to import|Path|
|Batch size|Rows will be written in batches of this size at a time. By default, all rows will be written at once.|2000|
|Method|||

### Download File
  
Download File from a SQL Server Database
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session to use|Conn1|
|SQL Query|SQL query to execute|EXEC up_Archivos_Select @IdArchivoTipo = 56, @IdPropietario = 1718029|
|Path where the file will be saved|Path where the file will be saved|C:/Users/Downloads/|
|Column that stores the file name|Name of the column that stores the file name|Document|
|Column that stores the file content|Name of the column that stores the file content|File|

### Create a SP with variables
  
Create the Store Procedure with variables
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session's name|Conn1|
|SP's name|SP's name|TestDB_GetAll|
|SP's variables|SP's variables (separated by comma)|@LastName nvarchar(50), @FirstName nvarchar(50)|
|Query|SP's query (what it is between BEGIN and END)|SELECT * FROM dbo.Table WHERE LastName = @LastName AND FirstName = @FirstName|

### Get SPs
  
Get the available Store Procedures
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session name|Conn1|
|Assign to var|Assign the result to a variable|Variable|

### SP to execute
  
To see the SPs you must connect to the DB and do not close the conection until you selected the Store Procedure
|Parameters|Description|example|
| --- | --- | --- |
|Select the SP|To see the SPs you must connect to the DB and do not close the conection until you selected the Store Procedure||
|Session|Session name|Conn1|
|Assign to var|Var where the result will be stored|Variable|

### Delete a SP
  
Delete the indicated Store Procedure
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session name|Conn1|
|SP's name|Store Procedure's name|TestDB_GetAll|

### Close connection
  
Close the connection to SQLServer
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
