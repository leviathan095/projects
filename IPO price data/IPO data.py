from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.keys import Keys

pd.set_option('display.max_columns', None)

url = "https://halkarz.com"

options = Options()
b = webdriver.Chrome()

b.get(url)

while True:
    time.sleep(2)
    try:

        button = b.find_element(By.XPATH,'// *[ @ id = "getin"] / div / div / div[2] / div[1] / div')
        b.execute_script("arguments[0].click();", button)

    except NoSuchElementException:
        break
sirket_kodu = [name.text for name in b.find_elements(By.CLASS_NAME, 'il-bist-kod')]
sirket_adi = [name.text for name in b.find_elements(By.CLASS_NAME, 'il-halka-arz-sirket')]
arz_tarihi = [name.text for name in b.find_elements(By.CLASS_NAME, 'il-halka-arz-tarihi')]
elems = b.find_elements(By.CSS_SELECTOR,"h3.il-halka-arz-sirket [href]")
all_links = [elem.get_attribute('href') for elem in elems]



sirket_kodu = [ np.nan if item == '' else item for item in sirket_kodu]
sirket_adi = [ np.nan if item == '' else item for item in sirket_adi]
arz_tarihi = [ np.nan if item == '' else item for item in arz_tarihi]

sirket_kodu= sirket_kodu[:5]
sirket_adi= sirket_adi[:5]
arz_tarihi = arz_tarihi[:5]
all_links = all_links[:5]


prices = []
current_prices = []
for link in all_links:
     url = link

     b.get(url)

     price = [name.text for name in b.find_elements(By.CLASS_NAME, 'f700')]
     prices.append(price)

prices_first = [item for sublist in prices for item in sublist]
for kod in sirket_kodu:
    url2 = 'https://fintables.com'

    b.get(url2)
    e = b.find_element(By.XPATH , '/ html / body / div[1] / main / div / main / div[3] / div[1] / div[2] / div[2] / div[2] / div[1] / div[1] / input')
    e.send_keys(kod)
    e.send_keys(Keys.ENTER)
    time.sleep(2)
    curr_price = [name.text for name in b.find_elements(By.XPATH, '//*[@id="sidebar"]/div/div/div[1]/div[1]/div/div[2]/div[1]/span')]
    current_prices.append(curr_price)
current_price = [item for sublist in current_prices for item in sublist]
price_first = []
for item in prices_first:
    price_first.append(item.replace('TL', ''))


df=pd.DataFrame({"Company Name": sirket_adi, "Company Code" : sirket_kodu, "Date" : arz_tarihi, "Prices": prices_first, "Current Prices":current_prices})
df = df.dropna()
df.to_csv('products.csv', index=False, encoding='utf-8')

