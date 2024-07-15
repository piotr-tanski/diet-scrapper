from django.db import models
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
import time


def get_diet(diet):
    result = ""
    start = time.time()

    if diet == "maczfit":
        result = _get_maczfit()

    end = time.time()
    print(f"get_diet({diet}) took {end - start} seconds")
    return result


def _get_maczfit():
    driver = _get_chrome_driver()
    diets = ['comfort', 'vege', 'fit', 'wegan', 'fodmap', 'no-lactose-&-low-gluten', 'diabetic', 'hypo-hashimoto', 'keto']
    meals = defaultdict(list)
    for diet in diets:
        print(f"Getting {diet} from maczfit")
        driver.get(f'https://www.maczfit.pl/programy-maczfit?diet={diet}&active=0')
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu__meals')))
        if not element:
            continue

        for e in driver.find_elements(By.CLASS_NAME, 'menu__meals'):
            name = e.find_element(By.CLASS_NAME, 'meal__name').text
            desc = e.find_element(By.CLASS_NAME, 'meal__description').text
            if name and desc:
                meals[name].append(desc)
    return meals


def _get_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    return webdriver.Chrome(chrome_options=chrome_options)