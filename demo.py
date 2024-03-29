import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 使用Firefox浏览器
driver = webdriver.Firefox()

# 打开百度网站
driver.get('https://www.baidu.com')
driver.find_element(By.NAME, "wd").send_keys("你好")
time.sleep(3)
driver.quit()
