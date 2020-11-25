
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from time import  sleep
driver = webdriver.Firefox()

tempo_de_espera = 0.1
conteudo = []

# Navigate to url

tagBE = 'div.g:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(2) > span:nth-child(1)'

driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action

driver.find_element(By.NAME, "q").send_keys("BRASITALIA CAFÉS" + Keys.ENTER)
t = 1
while True:
    try:
        driver.find_element_by_css_selector(tagBE).is_enabled()
        like = driver.find_element_by_css_selector(tagBE)
        break
    except NoSuchElementException:
        arquivo = open(f'Python/Log_Erros/erros-{date.today()}', 'w')
        conteudo.append(f"Elemento não encontrato, Tentativa: {t} \n")
        t += 1
        sleep(tempo_de_espera)
        if t > 4:
            break
if t > 4:
    conteudo.append(f"Tempo esgotado! Não foi possível encontrar a tag CSS_COLECTOR [{tagBE}] no tempo estimado! (Tempo configurado de espera {tempo_de_espera} segundo)")
    arquivo.writelines(conteudo)
    arquivo.close()
    #print(f"Tempo esgotado! Não foi possível encontrar a tag CSS_COLECTOR [{tagBE}] no tempo estimado!")

    driver.quit()
else:
    like.click()
    arquivo.writelines("Sem erros")








#https://www.selenium.dev/documentation/en/webdriver/keyboard/