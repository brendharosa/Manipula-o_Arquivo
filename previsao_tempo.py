
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

cidade = input("Digite o nome da cidade: ").strip()

options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = None

try:
    driver = webdriver.Chrome(options=options)

    url = "https://wttr.in/" + quote(cidade) + "?format=j1"
    driver.get(url)

    conteudo = driver.find_element(By.TAG_NAME, "body").text
    previsao = json.loads(conteudo)

    temperatura_minima = previsao["weather"][0]["mintempC"]
    temperatura_maxima = previsao["weather"][0]["maxtempC"]

    data_atual = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).strftime("%d/%m/%Y")

    print("===================================")
    print("         PREVISÃO DO TEMPO")
    print("===================================")
    print("Cidade:", cidade)
    print("Data da consulta:", data_atual)
    print("Temperatura mínima:", temperatura_minima, "°C")
    print("Temperatura máxima:", temperatura_maxima, "°C")
    print("===================================")

except Exception as erro:
    print("Erro ao consultar a previsão:", erro)

finally:
    if driver is not None:
        driver.quit()
