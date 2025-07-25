from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = Options()
# Commented out headless to debug visually
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://www.99acres.com/search/property/buy/bhubaneswar?city=182&preference=S&area_unit=1&res_com=R"
property_data = []

for page in range(1, 4):
    url = f"{base_url}&page={page}"
    driver.get(url)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "srpTuple__card")]'))
        )
    except:
        print(f"No listings found on page {page}")
        continue

    listings = driver.find_elements(By.XPATH, '//div[contains(@class, "srpTuple__card")]')
    print(f"Found {len(listings)} listings on page {page}")

    for listing in listings:
        try:
            name = listing.find_element(By.CLASS_NAME, "srpTuple__propertyName").text
        except:
            name = ""
        try:
            price = listing.find_element(By.CLASS_NAME, "srpTuple__spacer10").text
        except:
            price = ""
        try:
            area = listing.find_element(By.CLASS_NAME, "srpTuple__area").text
        except:
            area = ""
        try:
            address = listing.find_element(By.CLASS_NAME, "srpTuple__propertyLocation").text
        except:
            address = ""
        try:
            desc = listing.find_element(By.CLASS_NAME, "srpTuple__propertyBrief").text
        except:
            desc = ""

        property_data.append({
            "property_name": name,
            "price": price,
            "areaWithType": area,
            "address": address,
            "description": desc
        })

    print(f"Page {page} done")

driver.quit()

df = pd.DataFrame(property_data)
df.to_csv("bhubaneswar_99acres_properties.csv", index=False)
