# Billy-Blaze

Web Scraper escrito em python utilizando selenium web driver. Tem como objetivo automatizar a coleta dos resultados do jogo Double, gravando no mysql para posterior análise.

Ele foi feito para coletar dados que estão no DOM da página, em breve criarei um novo projeto com um jeito mais elegante de coletar tal informação.

## Requisitos

 - Mysql ou mariadb instalado com o seu usuário e senha em mãos;
 - python3;
 - Navegador Chrome;

## Tutorial de Instação

 1. Acessar o banco de dados com o gerenciador de sua preferência;
 2. Rodar o script sql [`..db/script_cria.sql`] para criar o banco de dados e suas tabelas;
 3. Instalar os módulos necessários no projeto via shell:
		pip install selenium
		pip install python-dotenv
		pip install mysql-connector
		pip install webdriver_manager
4. Criar o arquivo [`.env`] com seus respectivos valores:
		  
	```js
	URL_LOGIN=https://blaze.com/pt/?modal=auth&tab=login
	URL_DOUBLE=https://blaze.com/pt/games/double
	LOGIN=//Email de acesso ao sistema da blaze
	SENHA=//Senha de acesso
	DB_HOST=localhost
	DB_PORT=3306
	DB_USER=//usuario do banco de dados
	DB_PASS=//senha do banco de dados
	DB_DATABASE=billy_blaze
	CHROME_PATH=//usr//bin//google-chrome-stable **path do executavel do chrome**
	```

# Execução

		python3 fogo.py
Ao executar, ele vai abrir o chrome, navegar até o site da blaze, preencher o login e irá aguardar o usuário resolver o captcha. Ao resolver o captcha o mesmo irá coletar os resultados de forma automática.

# Consultas

Consultas úteis estão no arquivo [`..db/querys/uteis.sql`] 

## Ezemplos:

### Quantidade de branco por hora separado por dia:
![1](https://user-images.githubusercontent.com/102566506/196878477-619aa358-9ec4-41fd-be3a-02c1ff34c7f9.png)

### Quantidade de branco por hora e consolidado pelos dias da semana:
![2](https://user-images.githubusercontent.com/102566506/196878559-7a6d281e-1100-44b9-8ce5-842885964ca1.png)

### Diferença de tempo entre os brancos:
![3](https://user-images.githubusercontent.com/102566506/196878603-34f2e751-b296-426e-8a99-7d7fb7df018a.png)
