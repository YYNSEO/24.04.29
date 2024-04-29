import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

selector=''

# def js_click_script():
#

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)
target=driver.find_elements(By.CLASS_NAME, 'rank02')
print(len(target))
temp=[]
for i in range(len(target)):
    temp.append(target[i].text)
for i in temp:
    print(i)