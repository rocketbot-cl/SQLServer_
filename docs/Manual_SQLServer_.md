



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
|Session||Conn1|
|Server||DESKTOP-T2319IB\SQLEXPRESS|
|BD Name||test|
|User BD||usertest|
|Pass BD||passtest|

### Query SQLServer
  
Make a query to a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|SQL Query||select * from test|
|Session||Conn1|
|Assign to var||Variable|

### Export data
  
Export data from a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
|SQL Query||select * from test|
|File path||Path|
|Base file path||Path|
|Sheet name||Sheet1|
|Cell||Cell|

### Import data
  
Import data to a SQLServer database
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
|Sheet name||Sheet1|
|Name of the table to import||Table|
|Base file path||Path|

### Create a SP with variables
  
Create the Store Procedure with variables
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
|SP's name||TestDB_GetAll|
|SP's variables||@LastName nvarchar(50), @FirstName nvarchar(50)|
|Query||SELECT * FROM dbo.Table WHERE LastName = @LastName AND FirstName = @FirstName|

### Get SPs
  
Get the available Store Procedures
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
|Assign to var||Variable|

### SP to execute
  
To see the SPs you must connect to the DB and do not close the conection until you selected the Store Procedure
|Parameters|Description|example|
| --- | --- | --- |
|Select the SP|||
|Session||Conn1|
|Assign to var||Variable|

### Delete a SP
  
Delete the indicated Store Procedure
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
|SP's name||TestDB_GetAll|

### Close connection
  
Close the connection to SQLServer
|Parameters|Description|example|
| --- | --- | --- |
|Session||Conn1|
