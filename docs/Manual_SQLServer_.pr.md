



# SQLServer
  
Conecte-se ao SQL Server e gerencie todos os seus bancos de dados, execute consultas personalizadas, importe e exporte dados, crie e execute procedimentos armazenados.  

*Read this in other languages: [English](Manual_SQLServer_.md), [Português](Manual_SQLServer_.pr.md), [Español](Manual_SQLServer_.es.md)*
  
![banner](imgs/Banner_SQLServer_.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conexão com SQLServer
  
Conectar ao banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão|Conn1|
|Server|Nome do servidor|DESKTOP-T2319IB\SQLEXPRESS|
|Driver|Nome do driver|{ODBC Driver 17 for SQL Server}|
|Nome do BD|Nome do banco de dados|test|
|Usuário do BD|Usuário do banco de dados|usertest|
|Senha do BD|Senha do usuário do banco de dados|passtest|
|Atribuir a variável|Variável onde o resultado da conexão será armazenado|Variable|

### Consulta SQLServer
  
Faça uma consulta a um banco de dados do SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Consulta SQL|Consulta que será executada no banco de dados|select * from test|
|Sessão|Nome da sessão de conexão|Conn1|
|Assign to var|Nome da variável à qual o resultado da consulta será atribuído|Variable|

### Inserir SQLServer
  
Inserir dados em um banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Insert Query|Insert to execute, without including the values|insert into test (id, name)|
|Valores|Valores a inserir na tabela, cada valor deve estar entre aspas simples e separados por vírgulas|('15', 'Rocketbot')|
|Sessão|Nome da sessão a ser usada|Conn1|
|Assign to var|Atribuir o resultado a uma variável|Variable|

### Exportar dados
  
Exportar dados de um banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão a ser usada|Conn1|
|Consulta SQL|Consulta SQL para executar|select * from test|
|Caminho de arquivo|Caminho do arquivo para exportar|Caminho|
|Caminho do arquivo base|Arquivo base. É útil caso você queira exportar com um formato ou cabeçalhos específicos|Caminho|
|Nome da folha|Nome da folha onde será exportado|Folha1|
|Celula|Célula onde será exportado|Celula|

### Importar dados
  
Importar dados para um banco de dados SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão de conexão|Conn1|
|Nome da folha|Nome da planilha para importar|Folha1|
|Esquema da tabela|Esquema da tabela SQL para importar. Por padrão, dbo.|dbo|
|Nome da tabela a importar|Nome da tabela SQL onde os dados serão importados. Se não existir, será criado.|Tabela|
|Caminho do arquivo base|Caminho do arquivo base para importar|Caminho|
|Tamanho do batch|As linhas serão gravadas em lotes desse tamanho por vez. Por padrão, todas as linhas serão gravadas de uma só vez.|2000|
|Método|||

### Baixar Arquivo
  
Baixar Arquivo de um Banco de Dados SQL Server
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão a ser usada|Conn1|
|Consulta SQL|Consulta SQL para executar|EXEC up_Archivos_Select @IdArchivoTipo = 56, @IdPropietario = 1718029|
|Caminho onde o arquivo será salvo|Caminho onde o arquivo será salvo|C:/Users/Downloads/|
|Coluna que armazena o nome do arquivo|Nome da coluna que armazena o nome do arquivo|Documento|
|Coluna que armazena o conteúdo do arquivo|Nome da coluna que armazena o conteúdo do arquivo|Arquivo|

### Crie um SP com variáveis
  
Crie um Store Procedure com variáveis
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão|Conn1|
|Nome de SP|Nome de SP|TestDB_GetAll|
|Variáveis de SP|Variáveis de SP (separadas por vírgula)|@LastName nvarchar(50), @FirstName nvarchar(50)|
|Query|Query do SP (o que está contido entre BEGIN e END)|SELECT * FROM dbo.Table WHERE LastName = @LastName AND FirstName = @FirstName|

### Obter SPs
  
Obtenha os Store Procedures disponíveis
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão|Conn1|
|Assign to var|Assign the result to a variable|Variable|

### SP para executar
  
Para ver os SPs, você deve se conectar ao DB sem fechar a conexão até selecionar o Store Procedure
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione o SP|Para ver os SPs, você deve se conectar ao DB sem fechar a conexão até selecionar o Store Procedure||
|Sessão|Nome da sessão|Conn1|
|Sessão|Nome da sessão|dbo|
|Assign to var|Var where the result will be stored|Variable|

### Excluir um SP
  
Exclua o Store Procedure indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão|Conn1|
|Nome de SP|Nome do Store Procedure|TestDB_GetAll|

### Desligar conexão
  
Desligar a conexão com SQLServer
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
