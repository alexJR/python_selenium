
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from time import  sleep
driver = webdriver.Firefox()

tempo_de_espera = 0
conteudo = []

# Navigate to url
print(datetime.today())
nome = '//*[@id="nome"]'
cpf = '#CPF'
email = '#exampleInputEmail1'
senha = '#exampleInputPassword1'
flag = '#exampleCheck1'


enviar = '.btn'

driver.get("https://django1-ajr.herokuapp.com/seguradoras")

# Enter "webdriver" text and perform "ENTER" keyboard action


with open('Python/dados', 'r', encoding='utf-8') as f:
    results = [[str(entry) for entry in line.split(';')] for line in f.readlines()]

for x, v in enumerate(results):
    sleep(tempo_de_espera)
    driver.find_element_by_xpath(nome).send_keys(results[x][0])
    sleep(tempo_de_espera)
    driver.find_element_by_css_selector(cpf).send_keys(results[x][1])
    sleep(tempo_de_espera)
    driver.find_element_by_css_selector(email).send_keys(results[x][2])
    sleep(tempo_de_espera)
    driver.find_element_by_css_selector(senha).send_keys("**********")
    sleep(tempo_de_espera)
    driver.find_element_by_css_selector(flag).click()
    sleep(tempo_de_espera)
    driver.find_element_by_css_selector(enviar).click()
    sleep(0.1)
    driver.get("https://django1-ajr.herokuapp.com/seguradoras")

print("FINALIZADO")
driver.quit()
print(datetime.today())









#https://www.selenium.dev/documentation/en/webdriver/keyboard/