from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
prefs = {
        "download.default_directory": r"C:\Users\oliver.rospendowski\Desktop\Estudo\EstudoPython\output"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

teste = driver.get("http://127.0.0.1:5500/index.html")
time.sleep(5)

teste = driver.find_element(By.CLASS_NAME, "first-month-value").text

print(teste)
