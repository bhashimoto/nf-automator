import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def config_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    return driver, wait

    
def element_exists(driver, by, value):
    try:
        element = driver.find_element(by, value)
    except NoSuchElementException:
        return None
    return element


def convert_block_to_date(block):
    text = block.split('Emissão: ')[1]
    text = text.split(' ')[0]
    date_parts = text.split('/')
    date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
    return date

def download_data(url: str, driver, wait):
    print("accessing URL")
    driver.get(url)
    wait.until(EC.visibility_of_element_located((By.ID, 'tabResult')))
    retrieved_data = {'items':[]}

    print("retrieving data")
    raw_date = driver.find_element(By.XPATH, '//*[@id="infos"]/div[1]/div/ul/li').text
    date = convert_block_to_date(raw_date)
    
    curr_row = 1
    keep_running = True
    
    while keep_running:
        element = element_exists(driver, By.ID, f"Item + {curr_row}")
        if element is None:
            keep_running = False
        else:
            item_name = element.find_element(By.CLASS_NAME, 'txtTit').text
            valor_total_item = element.find_element(By.CLASS_NAME, 'valor').text
            
            retrieved_data['items'].append({'date': date, 'name': item_name, 'value': float(valor_total_item.replace(',', '.'))})

            curr_row += 1
    driver.close()
    return retrieved_data


def retrieve_data(url):
    driver, wait = config_driver()
    print(f"Downloading data from {url}")
    items = download_data(url, driver, wait)
    print(f"retrieved data: {items}")
    return items

