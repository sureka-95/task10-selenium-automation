# import selenium webdriver module
from selenium import webdriver
# imports the By class, which helps to locate elements on a web page
from selenium.webdriver.common.by import By
#import python built in time module
import time

# Set up the driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#  for Login process
# using the find_element function in By class to find specific html id
# send_keys used to type the text in the current field
# finally click() is used to click login button
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# time.sleep() used to pause the execution
# Wait for the inventory page to load
time.sleep(3)

# Fetch title and current URL after login
# store it in the below variable
page_title = driver.title
current_url = driver.current_url

# Extract product names and prices using  By class
products = driver.find_elements(By.CLASS_NAME, "inventory_item")

# opens (or creates) a file named Webpage_task_11.txt in write mode
# encoding="utf-8" ensures it handles special characters
# f is a file object — like a pen you're using to write into the file
# with statement ensures the file is automatically closed after you're done writing
# Save to file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as f:
    f.write(f"Page Title: {page_title}\n")
    f.write(f"Current URL: {current_url}\n\n")
    f.write("Products:\n")
    f.write("----------\n")

    # \n gives line break
    # create loop  until get product name
    for item in products:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        f.write(f"{name} - {price}\n")

# Closes all browser windows and ends the session
driver.quit()

# display output as
print("Saved title, URL, and product info to Webpage_task_11.txt")
