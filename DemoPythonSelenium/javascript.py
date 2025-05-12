import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def click(element):
    try:
        time.sleep(3)
        driver.execute_script("arguments[0].click()",element)
        print("Alert clicked successfully")
        time.sleep(3)
    except Exception as e:
        print(f"Click function got failed : {e}")

def flash(element):
    for i in range(1, 30):
        driver.execute_script("arguments[0].scrollIntoView();", element) 
        driver.execute_script("arguments[0].style.background='red'",element)
        time.sleep(.2)
        default_color=element.value_of_css_property('color')
        # print(default_color)
        driver.execute_script("arguments[0].style.background='"+default_color+"'",element)

        
def accept_alert():
    try:
        driver.switch_to.alert.accept()
        print("Alert acccepted")
    except Exception as e:
        print("alert is not accepted")

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

# driver.execute_script("alert('welcome')")
# time.sleep(3)
# driver.switch_to.alert.accept()
# time.sleep(3)

alert=driver.find_element(By.ID,"alert1")

# button=driver.find_element(By.ID,"alert1")
# driver.execute_script("arguments[0].click()",button)

flash(alert)
click(alert)
accept_alert()