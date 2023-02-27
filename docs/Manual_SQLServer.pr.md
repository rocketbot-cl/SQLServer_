# SQLServer
  
Módulo para interagir com SQL Server com consultas e SPs  
  
![banner](imgs/Banner_SQLServer_.jpg)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Conexão com SQLServer
  
Conectar ao banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
|Server||DESKTOP-T2319IB\SQLEXPRESS|
|Nome do BD||test|
|Usuário do BD||usertest|
|Senha do BD||passtest|

### Consulta SQLServer
  
Faça uma consulta a um banco de dados do SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Consulta SQL||select * from test|
|Sessão||Conn1|
|Assign to var||Variable|

### Exportar dados
  
Exportar dados de um banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
|Consulta SQL||select * from test|
|Caminho de arquivo||Caminho|
|Caminho do arquivo base||Caminho|
|Nome da folha||Folha1|
|Celula||Celula|

### Importar dados
  
Importar dados para um banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
|Nome da folha||Folha1|
|Nome da tabela a importar||Tabela|
|Caminho do arquivo base||Caminho|

### Crie um SP com variáveis
  
Crie um Store Procedure com variáveis
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
|Nome de SP||TestDB_GetAll|
|Variáveis de SP||@LastName nvarchar(50), @FirstName nvarchar(50)|
|Query||SELECT * FROM dbo.Table WHERE LastName = @LastName AND FirstName = @FirstName|

### Obter SPs
  
Obtenha os Store Procedures disponíveis
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
|Assign to var||Variable|

### SP para executar
  
Para ver os SPs, você deve se conectar ao DB sem fechar a conexão até selecionar o Store Procedure
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione o SP|||
|Sessão||Conn1|
|Assign to var||Variable|

### Excluir um SP
  
Exclua o Store Procedure indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
|Nome de SP||TestDB_GetAll|

### Desligar conexão
  
Desligar a conexão com SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
