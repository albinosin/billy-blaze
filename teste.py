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


chrome_options = Options()
"""
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
"""
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--remote-debugging-port=9222')

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


flag_loop = 0
while flag_loop < 1:
    flag_loop = 0