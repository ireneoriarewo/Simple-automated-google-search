from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "FILE PATH"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.get(URL)
driver.maximize_window()
search = driver.find_element(By.NAME, "q")
search.send_keys("History of Cake")

button = driver.find_element(By.TAG_NAME, "button")
search.send_keys(Keys.ENTER)

images = driver.find_element(By.LINK_TEXT, "Images")
images.send_keys(Keys.ENTER)
