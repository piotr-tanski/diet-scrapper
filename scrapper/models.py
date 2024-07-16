from django.db import models
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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
    meals = defaultdict(list)
    for diet in ['comfort', 'vege', 'fit', 'fodmap', 'no-lactose-&-low-gluten', 'diabetic', 'hypo-hashimoto']:
        print(f"Getting {diet} from maczfit")
        driver = _get_chrome_driver()
        driver.get(f'https://www.maczfit.pl/programy-maczfit?diet={diet}&active=0')
        try:
            element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu__meals')))
            for e in driver.find_elements(By.CLASS_NAME, 'menu__meals'):
                name = e.find_element(By.CLASS_NAME, 'meal__name').text
                desc = e.find_element(By.CLASS_NAME, 'meal__description').text
                if name and desc:
                    meals[name].append(desc)
        except TimeoutException:
            print(f"Couldn't get {diet} from maczfit!")
            pass
    return meals


def _get_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    return webdriver.Chrome(options=chrome_options)