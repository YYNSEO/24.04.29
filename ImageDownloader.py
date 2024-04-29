import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

search_query = "아이폰"
if not os.path.exists(search_query):
    os.makedirs(search_query)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/imghp")
search_box = driver.find_elements(By.CLASS_NAME,"gLFyf")
search_box[0].send_keys(search_query)
search_box[0].send_keys(Keys.RETURN)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
image_elements = driver.find_elements(By.CLASS_NAME,"cC9Rib")
image_links = []
c=0
for img in image_elements:
    try:
        c+=1
        ActionChains(driver).click(img).perform()
        time.sleep(1)
        actual_images = driver.find_elements(By.CLASS_NAME,'iPVvYb')
        for actual_image in actual_images:
            if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                image_links.append(actual_image.get_attribute('src'))
        if c>50:
            break
    except Exception as e:
        print(e)
for i, image_link in enumerate(image_links):
    try:
        response = requests.get(image_link)
        with open(os.path.join(search_query, f"{search_query}_{i}.jpg"), "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(e)
driver.quit()