from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
# driver.implicitly_wait(5)

# firstName = driver.find_element(By.XPATH,value="//div[@class='container']/input[1]")
# firstName.send_keys("Dhanush")

# lastName = driver.find_element(locate_with(By.TAG_NAME,"input").below(firstName))
# lastName.send_keys("Main")

# city = driver.find_element(By.XPATH,"//div[@class='container']/input[4]")

# gender = driver.find_element(locate_with(By.TAG_NAME,"input").above(city))

# city.send_keys("Salem")
# gender.send_keys("Male")

# country=driver.find_element(locate_with(By.TAG_NAME,"input").near(city))
# country.send_keys("India")

# securityQues = driver.find_element(locate_with(By.TAG_NAME,"input").below(country))
# securityQues.send_keys("Date of Birth")

# securityAns = driver.find_element(locate_with(By.TAG_NAME,"input").below(securityQues))
# securityAns.send_keys("24/12/2003")

# personalDetails=driver.find_element(locate_with(By.TAG_NAME,"input").below(securityAns))
# personalDetails.send_keys("146/3,vivekanandhar street, bharathi nagar, salem-10")

# confirmbtn=driver.find_element(By.XPATH,"//div[@class='container']/input[9]")
# # time.sleep(3)
# # confirmbtn.click()

# button3=driver.find_element(By.XPATH,"//div[@class='container']/div/button")
# # button3.click()
# print("button3")

# button2=driver.find_element(locate_with(By.TAG_NAME,("input")).to_left_of(button3))
# # button2.click()
# print("button2")

# button1=driver.find_element(locate_with(By.TAG_NAME,"input").to_left_of(button2))
# button1.click()
# print("button1")

# driver.implicitly_wait(10)
# box1=driver.find_element(By.XPATH,value="//button[@id='btn1']")
# box2=driver.find_element(By.XPATH,value="//button[@id='btn2']")
# box1.click()
# field1=driver.find_element(By.XPATH,value="//button[@id='btn2']//following-sibling::h3//child::input")
# field1.send_keys("Smartcliff")
# box2.click()
# field2=driver.find_element(By.XPATH,value="//button[@id='btn']//following-sibling::h3//child::input[2]")
# field2.send_keys("Solutions")


# box1=driver.find_element(By.XPATH,value="//button[@id='btn1']")
# box2=driver.find_element(By.XPATH,value="//button[@id='btn2']")
# box1.click()
# wait=WebDriverWait(driver,15)
# field1=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@id='btn2']//following-sibling::h3//child::input")))
# # field1=driver.find_element(By.XPATH,value="//button[@id='btn2']//following-sibling::h3//child::input")
# field1.send_keys("Smartcliff")
# box2.click()
# field2=wait.until(expected_conditions.presence_of_element_located((By.ID,"txt2")))
# # field2=driver.find_element(By.XPATH,value="//button[@id='btn']//following-sibling::h3//child::input[2]")
# field2.send_keys("Solutions")

box1=driver.find_element(By.XPATH,value="//button[@id='btn1']")
box2=driver.find_element(By.XPATH,value="//button[@id='btn2']")
box1.click()
# wait=WebDriverWait(driver,timeout=15)
wait = WebDriverWait(driver, timeout=10, poll_frequency=.2, ignored_exceptions=[NoSuchElementException])
field1=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@id='btn2']//following-sibling::h3//child::input")))
# field1=driver.find_element(By.XPATH,value="//button[@id='btn2']//following-sibling::h3//child::input")
field1.send_keys("Smartcliff")
box2.click()
field2=wait.until(expected_conditions.presence_of_element_located((By.ID,"txt2")))
# field2=driver.find_element(By.XPATH,value="//button[@id='btn']//following-sibling::h3//child::input[2]")
field2.send_keys("Solutions")
