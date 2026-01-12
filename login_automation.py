from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Edge(options=options)

driver.get("http://127.0.0.1:8000/login")

time.sleep(2)

driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "password").send_keys("password123")

time.sleep(3)

driver.quit()
