import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

"""
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("window-size=1200,1100")
options.add_argument("disable-gpu")
"""
options = None

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

def element_exists(by, value):
    try:
        element = driver.find_element(by, value)
    except NoSuchElementException:
        return None
    return element


def download_data(url: str):
    print("accessing URL")
    driver.get(url)
    wait.until(EC.visibility_of_element_located((By.ID, 'tabResult')))
    retrieved_data = {'items':[]}

    print("retrieving data")
    raw_date = driver.find_element(By.XPATH, '//*[@id="infos"]/div[4]/div/ul/li').text[:8]
    date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"

    
    curr_row = 1
    keep_running = True
    
    while keep_running:
        element = element_exists(By.ID, f"Item + {curr_row}")
        if element is None:
            keep_running = False
        else:
            item_name = element.find_element(By.CLASS_NAME, 'txtTit').text
            valor_total_item = element.find_element(By.CLASS_NAME, 'valor').text
            
            retrieved_data['items'].append({'date': date, 'name': item_name, 'value': float(valor_total_item.replace(',', '.'))})

            curr_row += 1
    return retrieved_data


def main():
    args = sys.argv[1:]
    url = args[0]
    print(f"Downloading data from {url}")
    items = download_data(url)
    print(f"retrieved data: {items}")


main()
