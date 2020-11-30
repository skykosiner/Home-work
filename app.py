from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
driver.get('https://www.satchelone.com/login')

# login
# School
def school():
    school = driver.find_element_by_id('school-selector-search-box')
    school.send_keys("Hasmonean High School")
    school.send_keys(Keys.ENTER)
school()
# Username
def user():
    username = driver.find_element_by_id('identification')
    username.send_keys("yoni@kosiner.co.uk")
user()
# Passwords
def password():
    load_dotenv()
    PASS = os.getenv("PASS")
    password = driver.find_element_by_id('password')
    password.send_keys(PASS)
    password.send_keys(Keys.ENTER)
password()
# Todos

time.sleep(2)
def todo():
    Todos = driver.find_element_by_class_name("row")
    print(Todos.text)
todo()
driver.quit()

# New driver on google classrom insted of stachel one
driver = webdriver.Safari()
driver.get('https://classroom.google.com/a/not-turned-in/all')

email = driver.find_element_by_id('identifierId')
email.send_keys("kosiy001.302@hasmoneanmat.org.uk")
email.send_keys(Keys.ENTER)

time.sleep(2)
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
classroom_password = driver.find_element_by_name('password')
classroom_password.send_keys(PASSWORD)
classroom_password.send_keys(Keys.ENTER)

time.sleep(9)
todos = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[2]')
print(todos.text)

time.sleep(5)
driver.quit()
