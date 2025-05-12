from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zoho.com/signup.html")

email=driver.find_element(By.XPATH,"//div[@id='czone-signup']/form/div/div[1]/div/span")

emailText=driver.find_element(locate_with(By.TAG_NAME,"input").below(email))
emailText.send_keys("dhanusheswarankiot281234@gmail.com")

password=driver.find_element(By.XPATH,"//div[@id='czone-signup']/form/div/div[2]/div/span")

passwordText=driver.find_element(locate_with(By.TAG_NAME,"input").below(password))
passwordText.send_keys("Dhanush2412$")

# phoneNoCode=driver.find_element(By.XPATH,"(//div[@class='wrap-elm'])[3]/div/div")

# phoneNumber=driver.find_element(locate_with(By.TAG_NAME,"input").near(phoneNoCode))
phoneNumber=driver.find_element(By.XPATH,"//input[@id='rmobile']")
phoneNumber.send_keys("8807722319")

checkbox=driver.find_element(By.XPATH,"//label[@class='sign_agree']/span")
checkbox.click()
print("Checkbox clicked")


# signIntext=driver.find_element(By.XPATH,"//div[@class='socl-signup']")

# signInbtn=driver.find_element(locate_with(By.TAG_NAME,"input").above(signIntext))
signInbtn=driver.find_element(By.ID,"signupbtn")
signInbtn.click()


captchaField=driver.find_element(By.XPATH,"//div[@class='signupcontainer']/div[5]/input")
captcha=input("Enter the captcha :")
captchaField.send_keys(captcha)

signInbtn.click()

otp=driver.find_element(By.XPATH,"//span[@class='signupotpcontainer']/span[1]/button")

otpField=driver.find_element(locate_with(By.TAG_NAME,"input").above(otp))
otpNo=input("enter the otp :")
otpField.send_keys(otpNo)

verify=driver.find_element(locate_with(By.TAG_NAME,"input").below(otp))
verify.click()
