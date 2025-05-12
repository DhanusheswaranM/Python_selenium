import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import requests

def verify_link(url):
    try :
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} - {response.reason} - {response.status_code}")
        else:
            print(f"{url} - {response.reason} -  {response.status_code} - is a broken link")
    except Exception as e:
         print(f"{url} - is a broken link")


driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")

# act = ActionChains(driver)
# blogs = driver.find_element(By.ID,"blogsmenu")
# act.move_to_element(blogs).perform()

# option2 = driver.find_element(By.XPATH,"//div[@id='cssmenu']/ul/li[2]/ul/li[2]/a")
# act.click(option2).perform()

# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# act=ActionChains(driver)
# driver.find_element(By.ID,"input-email").send_keys("aarun.83@gmail.com")
# driver.find_element(By.ID,"input-password").send_keys("Arun123")
# act.send_keys(Keys.ENTER).perform()
# time.sleep(3)

driver.get("https://omayo.blogspot.com/")
links=driver.find_elements(By.XPATH,"//div[@id='LinkList1']/div/ul/li/a")

act=ActionChains(driver)

print(len(links))

for link in links:
    # print(link.get_attribute("href"))
    url=link.get_attribute("href")
    if url:
        verify_link(url)

for link in links:
    act.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

