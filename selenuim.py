import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import numpy as np

selector=''

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)
target=driver.find_elements(By.CLASS_NAME, 'rank02')
#print(len(target))
#print(target[14])
temp=[]
counter = {}
for i in range(len(target)):
    if ',' in target[i].text:
        x = target[i].text.split(',')
        #print(i)
        temp.append(x[0])
        temp.append(x[1])
    else:
        temp.append(target[i].text)
#print(temp)
# for i in temp:
#     print(i)
for value in temp:
    try:
        counter[value] +=1
    except:
        counter[value] = 1
    #print(counter[value], "------------")
#print(counter)


plt.rcParams['font.family'] ='Malgun Gothic'
y=np.arange(len(counter.values()))
name = list(counter.keys())
count = list(counter.values())
plt.barh(y,count)
plt.yticks(y,name)
plt.show()



#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import matplotlib.pyplot as plt
# import numpy as np
# selector=""
# plt.rcParams['font.family'] ='Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] =False
#
# singer={}
# driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.melon.com/chart/index.htm")
# time.sleep(3)
# target=driver.find_elements(By.CLASS_NAME,"rank02")
#
#
# for i in range(len(target)):
#     sing=target[i].text
#     if len(sing.split(','))>1:
#         for i in sing.split(','):
#             if i not in singer:
#                 singer[i]=1
#             else:
#                 a = singer[i]
#                 b=a+1
#                 singer[sing]=b
#     else:
#         if sing not in singer:
#             singer[sing] = 1
#         else:
#             a=singer[sing]
#             b=a+1
#             singer[sing]=b
#
# # x=np.arange(len(singer.keys()))
# # plt.bar(x,list(singer.values()),color="red")
# # plt.xticks(x,list(singer.keys()))
# # plt.show()
# #
# ratio = list(singer.values())
# labels=list(singer.keys())
# plt.pie(ratio,labels=labels,autopct='%.1f%%') #explode 칸강조
# plt.show()