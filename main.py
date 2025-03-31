from selenium  import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime as dt
from time import sleep
import pandas as pd


def get_dates():
  

    driver = webdriver.Chrome(
        service = Service(ChromeDriverManager().install())
        )

    driver.get("https://economia.uol.com.br/cotacoes/bolsas/")

    companys = ['PETR3.SA', 'CIEL3.SA', 'TASA4.SA']
    values = list()
    date_time = list()

    for company in companys:
        input_search = driver.find_element(By.ID, 'filled-normal')
        input_search.send_keys(company)
        sleep(2)
        input_search.send_keys(Keys.ENTER)
        sleep(1)
        span_value = driver.find_element(By.XPATH, '//span[@class = "chart-info-val ng-binding"]')
        cotacion = span_value.text

        values.append(cotacion)
        date_time.append(dt.now().strftime('%d/%m/%Y %H:%M:%S'))
        
        
    date = {
        'companys': companys,
        'value' : values,
        'date_time': date_time,
    }
    print(companys)
    return date


def create_excel(date, file_name):   

    df_companys = pd.DataFrame(date)
    #Caminho para transformar dados: 1: data frame, 2: pandas, 3: csv
    df_companys.to_excel(file_name, index=False)

dates = get_dates()
create_excel(dates, './empresas_ações.xlsx')




