from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
from pathlib import Path
os.system('cls')

def Scrapy():
    url = "https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.ID,'cphBody_btnFurtoVeiculo').click()
    id = ''
    for ano in range(3):
        # PERCORRE OS ANOS
        id = f'cphBody_lkAno2{str(ano)}'
        driver.find_element(By.ID,id).click()
        # PERCORRE OS MESES
        for mês in range(1,13):
            id = f'cphBody_lkMes{str(mês)}'
            driver.find_element(By.ID,id).click()
            time.sleep(10)
        # EFETUA EXPORTAÇÃO
            driver.find_element(By.ID,'cphBody_ExportarBOLink').click()
            time.sleep(60)
        time.sleep(10)
    driver.quit()

def Tratar():
    for ano in range(3):
        pasta = f"ArquivosAno202{str(ano)}"
        name = f'DadosBO_202{str(ano)}*.xls'
        os.chdir(downloads_path)
        os.system(f'md {pasta}')
        os.system(f'move {name} {pasta}')
        os.chdir(pasta)          
        os.system(f'copy *.xls 202{str(ano)}.csv')    

downloads_path = str(Path.home() / "Downloads")

Scrapy()
Tratar()
