import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")

# place_List = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td[3]")

# for place in place_List:
#     print(place.text)

# row=len(driver.find_elements(By.XPATH,"//table[@id='table1']//tr"))
# col=len(driver.find_elements(By.XPATH,"//table[@id='table1']//th"))
# print("Number of row :",row)
# print("Number of column :",col)

# for r in range(1, row+1) :
#     for c in range(1, col+1) :
#         if r==1:
#              head=driver.find_element(By.XPATH,"//table[@id='table1']/thead/tr["+str(r)+"]/th["+str(c)+"]")
#              print(head.text,end=" ")
#         else:
#             data=driver.find_element(By.XPATH,"//table[@id='table1']//tr["+str(r-1)+"]/td["+str(c)+"]")
#             print(data.text,end=" ")
#     print()
# # for r in range(1, row+1) :
# #     for c in range(1, col+1) :
# #         if r==1:
# #              head=driver.find_element(By.XPATH,"//table[@id='table1']//tr["+str(r)+"]//th["+str(c)+"]")
# #              print(head.text,end=" ")
# #         else:
# #             data=driver.find_element(By.XPATH,"//table[@id='table1']//tr["+str(r-1)+"]//td["+str(c)+"]")
# #             print(data.text,end=" ")
# #     print()

driver.get("https://thinking-tester-contact-list.herokuapp.com/")
email=driver.find_element(By.ID,"email")
email.send_keys("test@2412gmail.com")

password=driver.find_element(By.ID,"password")
password.send_keys("test@2412")

submit=driver.find_element(By.ID,"submit")
submit.click()

# driver.get("https://thinking-tester-contact-list.herokuapp.com/")
# email=driver.find_element(By.ID,"email")
# email.send_keys("test@2412gmail.com")

# password=driver.find_element(By.ID,"password")
# password.send_keys("test@2412")

# submit=driver.find_element(By.ID,"submit")
# submit.click()

# row=len(driver.find_elements(By.XPATH,"//table[@id='myTable']//tr"))
# col=len(driver.find_elements(By.XPATH,"//table[@id='myTable']//th"))
# print("Number of row :",row)
# print("Number of column :",col)

# for i in range(2,row+1):
#     data = driver.find_element(By.XPATH,"//table[@id='myTable']/tr["+str(i)+"]/td[2]")
#     print(data.text)
time.sleep(3)
contact_name=driver.find_elements(By.XPATH, "//table[@id='myTable']/tr/td[2]")
count=len(contact_name)
for name in contact_name:
    print(name.text)

expected_name ="Danny S"
i=1
time.sleep(3)
for name in contact_name:
    if name.text == expected_name:
        rowDate=driver.find_element(By.XPATH,"//table[@id='myTable']//tr["+str(i)+"]")
        actname=rowDate.find_elements(By.TAG_NAME,"td")
        for names in actname:
            print(names.text)
    i+=1