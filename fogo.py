import os
import mysql.connector
from dotenv import load_dotenv, find_dotenv
from mysql.connector import errorcode
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

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

#print(env_url_login, env_login, env_senha, env_db_host, env_db_port, env_db_user, env_db_pass, env_db_database)

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

''' 
---Exemplo de query do banco de dados---
query = "select id, char_name from double_colors"
cursor_colors = conn.cursor()

cursor_colors.execute(query)

myresult = cursor_colors.fetchall()

for x in myresult:
  print(x)

---EXEMPLO DE INSERT---
cursor_insert_teste = conn.cursor()

sql_insert_teste = "INSERT INTO teste VALUES (now())"

cursor_insert_teste.execute(sql_insert_teste)

conn.commit()

print("aaaa")

res_color = 1
res_number = 10
black_loot = 1000.11
red_loot = 1111.11
white_loot = 2222.22

try:
    cursor_insert = conn.cursor()
    #sql_insert_double = "INSERT INTO double_data VALUES (null, %s, %s, %f, %f, %f, now())"
    sql_insert_double = "INSERT INTO double_data VALUES (null, {}, {}, {}, {}, {}, now())".format(res_color, res_number, black_loot, red_loot, white_loot)
    print(sql_insert_double)
    val = (int(res_color), int(res_number), float(black_loot), float(red_loot), float(white_loot))
    cursor_insert.execute(sql_insert_double)
    conn.commit()
except mysql.connector.Error as error:
    print(cursor_insert)
    print("Failed to insert into MySQL table {}".format(error))





os._exit(0)
'''

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")


#browser  = webdriver.Chrome(ChromeDriverManager().install(), executable_path=env_chrome_path, chrome_options=chrome_options)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


#para aguardar resolver captcha
wait_0 = WebDriverWait(browser, timeout=1200, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

#verificar banner verde superior
wait_1 = WebDriverWait(browser, timeout=20, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException])

#load
wait_load = WebDriverWait(browser, timeout=6, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException])

#wait_logical
wait_logical = WebDriverWait(browser, timeout=1200, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException])

#wait_res
wait_res = WebDriverWait(browser, timeout=1.5, poll_frequency=0.5, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException])
"""
def waitLoginCaptcha(browser):
    cond_wait = 0
    while cond_wait < 1:
        if browser.find_element(By.CSS_SELECTOR,"#header > div.right > div > div.routes > div > div.icons > div:nth-child(2) > div"):
            return True


def verifyMaintenance(browser):
    cond_wait = 0
    cont_maintenance = 0
    while cond_wait < 1:
        if browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.game-controller-container > div.maintenance-overlay"):
            print("Manutenção") 
            if cont_maintenance > 0:
                cursor_insert_maintenance = conn.cursor()
                sql_insert_maintenance = "INSERT INTO double VALUES (4, 0, 0, 0, now())"

                cursor_insert_maintenance.execute(sql_insert_maintenance)

                conn.commit()

                cont_maintenance += 1
        if not browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.game-controller-container > div.maintenance-overlay"):
            return True
            
def waitNextSpin(browser):
    cond_wait = 0

    while cond_wait < 1:
        
        verify_maintenance = WebDriverWait(browser, timeout=30).until(verifyMaintenance)
        prog_bar = browser.find_element(By.CSS_SELECTOR,"#roulette-timer > div.progress-bar").value_of_css_property('display')
        if prog_bar == 'flex':
            return True

def waitTime(browser):
    cond_wait = 0
    
    while cond_wait < 1:
        time_left = browser.find_element(By.CSS_SELECTOR,"#roulette-timer > div.progress-bar > div.time-left > span").text
        tl = time_left.split(':')
        
        if int(tl[0]) <= 1:
            red_val = time_left = browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.col-wrapper > div > div.col-md-4.col-xs-12.margin-xs.left > div > div.body.show > div.total > div.counter > span").text
            print("red ", red_val)

            white_val = time_left = browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.col-wrapper > div > div.col-md-4.col-xs-12.margin-xs.mid > div > div.body.show > div.total > div.counter > span").text
            print("whitet ", white_val)

            black_val = time_left = browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.col-wrapper > div > div.col-md-4.col-xs-12.right > div > div.body.show > div.total > div.counter > span").text
            print("black ", black_val)
            return True

"""
browser.get(env_url_login)



input_login_username = browser.find_element("name", "username")
input_login_username.send_keys(env_login)

input_login_password = browser.find_element("name", "password")
input_login_password.send_keys(env_senha)


input_login_submit = browser.find_element(By.CLASS_NAME,"submit")
input_login_submit.click()


print("Resolva o Captcha e realize o login!.") 
login_captcha = wait_0.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header > div.right > div > div.routes > div > div.icons > div:nth-child(2) > div")))

print("Logou!!!, aguardando renderizar a pagina.")

#browser.implicitly_wait(10)
try:
    load_1 = wait_load.until(EC.presence_of_element_located((By.ID, "naonaonao")))
except TimeoutException:
    print("Timeout 1\n")
    pass

print("Buscando barra superior, se existir clicar no X para fechar")
barra_superior = wait_1.until(EC.presence_of_element_located((By.ID, "banner")))

print("Barra Fecharda, aguardando o site renderizar novamente.")
if barra_superior:
    print("Barra encontrada, fechando...")
    icon_close = wait_1.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner > i")))    
    if icon_close:
        icon_close.click()
        #browser.implicitly_wait(10)
        try:
            load_2 = wait_load.until(EC.presence_of_element_located((By.ID, "naonaonao")))
        except TimeoutException:
            print("Timeout 2\n")
            pass
        
"""
if browser.find_element(By.CSS_SELECTOR,"#banner"):
    banner_a = browser.find_element(By.CSS_SELECTOR,"#banner > i")
    banner_a.click()

"""
print("Abrindo double, aguarde")
browser.get(env_url_double)
#browser.implicitly_wait(10)
try:
    load_3 = wait_load.until(EC.presence_of_element_located((By.ID, "naonaonao")))
except TimeoutException:    
    print("Timeout 3\n")
    pass

flag_loop = 0
flag_bar_timer = 0

red_loot = "0"
white_loot = "0"
black_loot = "0"

while flag_loop < 1:
    #Next Spin

    try:
        if flag_bar_timer == 0:
            wait_next_bar_time = wait_logical.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#roulette-timer > div.progress-bar")))
            if wait_next_bar_time:
                flag_bar_timer = 1
                res_color = 0
                res_number = 0

                #res = browser.find_element(By.CSS_SELECTOR,"#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div")

                #red 2
                #if browser.find_element(By.CSS_SELECTOR, "#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div.red > div"):
                red_red = False
                try:
                    red_red = wait_res.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div.red > div")))
                    if red_red:
                        res_color = 2
                        #res_number = res_red.find_element(By.CLASS_NAME, 'number').text
                        #res_numbar = browser.find_element(By.CSS_SELECTOR, "#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div.red > div").text
                        res_number = red_red.text
                        #print("Red", res_number)
                except TimeoutException:
                    pass
                #white 3
                white_res = False
                try:
                    white_res = wait_res.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div.white")))
                    if white_res:
                        res_color = 3
                        res_number = 0
                        #print("white", res_number)
                except TimeoutException:
                    pass
                
                #black 1
                black_res = False
                try:
                    black_res = wait_res.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div.black > div")))
                    if black_res:
                        res_color = 1
                        #res_number = res_red.find_element(By.CLASS_NAME, 'number').text
                        #res_number = browser.find_element(By.CSS_SELECTOR, "#roulette-recent > div > div.entries.main > div:nth-child(1) > div > div.black > div").text
                        res_number = black_res.text
                        #print("black", res_number)
                except TimeoutException:
                    pass

                #print("flag_bar_timer 1")
                '''
                print("Color", res_color)
                print("Number", res_number)
                print("Red Loot", red_loot)
                print("White Loot", white_loot)
                print("Black Loot", black_loot)
                print("\n\n")
                '''
                if red_loot != "0":
                    """
                    id
                    fk_int_id_color
                    number_spin
                    dec_black
                    dec_red
                    dec_white
                    dt_spin
                    """
                    
                    #print("aaaaaaaaa", float(black_loot))
                    #sql_insert_double = """INSERT INTO double_data VALUES (null, %s, %s, %f, %f, %f, now())"""
                    if black_loot == "NaN":
                        black_loot = -1
                    if red_loot == "NaN":
                        red_loot = -1
                    if white_loot == "NaN":
                        white_loot = -1

                    try:    
                        cursor_insert = conn.cursor()
                        sql_insert_double = "INSERT INTO double_data VALUES (null, {}, {}, {}, {}, {}, now())".format(res_color, res_number, black_loot, red_loot, white_loot)
                        #val = (int(res_color), int(res_number), float(black_loot), float(red_loot), float(white_loot))

                       
                        cursor_insert.execute(sql_insert_double)

                        conn.commit()
                    except mysql.connector.Error as error:
                        print("Erro", sql_insert_double)
                        pass
        elif flag_bar_timer == 1:
            wait_next_bar_time_hide = wait_logical.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"#roulette-timer > div.progress-bar")))
            if wait_next_bar_time_hide:
                flag_bar_timer = 0

                red_loot = browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.col-wrapper > div > div.col-md-4.col-xs-12.margin-xs.left > div > div.body.show > div.total > div.counter > span").text    
                red_loot = red_loot.replace("R$ ", "")
                # print("Red2", red_loot)
                white_loot = browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.col-wrapper > div > div.col-md-4.col-xs-12.margin-xs.mid > div > div.body.show > div.total > div.counter > span").text    
                white_loot = white_loot.replace("R$ ", "")
                #print("White", white_loot)
                black_loot = browser.find_element(By.CSS_SELECTOR,"#roulette > div > div.col-wrapper > div > div.col-md-4.col-xs-12.right > div > div.body.show > div.total > div.counter > span").text    
                black_loot = black_loot.replace("R$ ", "")
                #print("Black", black_loot)

                #print("flag_bar_timer 0")
    except TimeoutException:
        wait_next_bar_time = False
        wait_next_bar_time_hide = False
        flag_bar_timer = 0
        pass


#wait_new = WebDriverWait(browser, timeout=30).until(waitNextSpin)
#wait_time = WebDriverWait(browser, timeout=30).until(waitTime)


input("Aguardando ordens")
#submit