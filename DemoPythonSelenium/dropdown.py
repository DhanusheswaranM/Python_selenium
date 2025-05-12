import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

car=driver.find_element(By.ID,"multiselect1")

carSelect=Select(car)

carOption=carSelect.options
for c in carOption:
    print(c.text)

# carSelect.select_by_visible_text("Volvo")
# carSelect.select_by_visible_text("Audi")
driver.execute_script("arguments[0].value='volvox'",car)

print("-------------------Selected options-------------------")
carOption=carSelect.options
for c in carOption:
    if c.is_selected():
        print(c.text)


