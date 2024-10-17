from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "langSelectButton")))

languageSelect = driver.find_element(By.CLASS_NAME, "langSelectButton")
languageSelect.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))

clickCookie = driver.find_element(By.ID, "bigCookie")
while True:
  clickCookie.click()
  cookieCount = int(driver.find_element(By.ID, "cookies").text.split(' ')[0])
  for i in range(4):
    upgrades = driver.find_element(By.ID, "product" + str(i))
    price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(',', '')
    if price:  # Check if price is not empty
      if cookieCount >= int(price):
        upgrades.click()
        break
