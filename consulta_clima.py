from selenium import webdriver
from selenium.webdriver.common.by import By


def consultar_clima(local:str)->str:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    class_clima = '//*[@id="wob_tm"]'
    class_tempo = '//*[@id="wob_tci"]'
    local_formatado = 'clima+' + local.replace(' ', '+')
    driver.get(f"https://www.google.com/search?q={local_formatado}")
    clima = driver.find_element(By.XPATH, class_clima)
    tempo = driver.find_element(By.XPATH, class_tempo)
    clima_formatado = str(clima.text) + " °C"
    tempo_formatado = tempo.get_attribute("alt")
    retorno = clima_formatado + " - " + tempo_formatado
    driver.quit()
    return retorno
