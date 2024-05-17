import time
from selenium.webdriver.common.by import By
import time
import re
import string
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# setup chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # ensure GUI is off
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1200')
driver = webdriver.Chrome(options=chrome_options)
while True:
  driver.get("https://trustpositif.kominfo.go.id/check")
  title = driver.title
  print(title)
  time.sleep(1)
  WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="press-to-modal"]'))).click()
  time.sleep(1)
  WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-data"]'))).click()
  time.sleep(0.3)
  input_user = input("Masukkan beberapa elemen (pisahkan dengan spasi atau koma): ")
  input_list = input_user.split()
  for asd in input_user:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-data"]'))).send_keys(asd)
  time.sleep(0.3)
  WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="text-footer"]'))).click()
  time.sleep(1)
  asdasd = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="daftar-block"]')))
  print(asdasd.text)
  driver.quit()
  time.sleep(60)
