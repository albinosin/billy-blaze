import os
import mysql.connector
from dotenv import load_dotenv, find_dotenv
from mysql.connector import errorcode

load_dotenv(find_dotenv())

env_url_login   = os.environ.get("URL_LOGIN")
env_url_double  = os.environ.get("URL_DOUBLE")
env_login       = os.environ.get("LOGIN")
env_senha       = os.environ.get("SENHA")
env_db_host     = os.environ.get("DB_HOST")
env_db_port     = os.environ.get("DB_PORT")
env_db_user     = os.environ.get("DB_USER")
env_db_pass     = os.environ.get("DB_PASS")
env_db_database = os.environ.get("DB_DATABASE")
env_chrome_path = os.environ.get("CHROME_PATH")

try:
    conn = mysql.connector.connect(
        host=env_db_host,
        user=env_db_user,
        password=env_db_pass,
        database=env_db_database
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Conectado com sucesso!\n")
    #conn.close()


#query = "select fk_int_id_color, dt_spin from double_data where fk_int_id_color > 0 and dt_spin between '2022-10-09 19:36:14' and '2022-10-09 19:42:45' order by dt_spin;"
query = "select fk_int_id_color, dt_spin from double_data where fk_int_id_color > 0 order by dt_spin;"
cursor_colors = conn.cursor()

cursor_colors.execute(query)

myresult = cursor_colors.fetchall()

cor_anterior = 0
dt_anterior = '0000-00-00 00:00:00'
contador = 1
controlador = 0

for x in myresult:
    if x[0] == cor_anterior:
        contador += 1
    else:        
        if controlador > 0:
            #print(cor_anterior, contador)
            try:    
                cursor_insert = conn.cursor()
                sql_insert_double = "INSERT INTO double_sequence VALUES (null, {}, {}, '{}')".format(cor_anterior, contador, dt_anterior)
                #val = (int(res_color), int(res_number), float(black_loot), float(red_loot), float(white_loot))

                
                cursor_insert.execute(sql_insert_double)

                conn.commit()
            except mysql.connector.Error as error:
                print("Erro", sql_insert_double)
                pass

        cor_anterior = x[0]
        dt_anterior = x[1]
        contador = 1
        controlador = 1

try:    
    cursor_insert = conn.cursor()
    sql_insert_double = "INSERT INTO double_sequence VALUES (null, {}, {}, '{}')".format(cor_anterior, contador, dt_anterior)
    #val = (int(res_color), int(res_number), float(black_loot), float(red_loot), float(white_loot))

    
    cursor_insert.execute(sql_insert_double)

    conn.commit()
except mysql.connector.Error as error:
    print("Erro", sql_insert_double)
    pass
  #print(x[1])