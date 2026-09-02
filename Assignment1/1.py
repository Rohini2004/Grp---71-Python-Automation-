from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")

search_box = driver.find_element(By.ID, "id-search-field")
print("ID:", search_box.tag_name)

search_box_name = driver.find_element(By.NAME, "q")
print("NAME:", search_box_name.tag_name)

search_button = driver.find_element(By.CLASS_NAME, "search-button")
print("CLASS_NAME:", search_button.tag_name)

heading = driver.find_element(By.TAG_NAME, "h1")
print("TAG_NAME:", heading.tag_name)

link = driver.find_element(By.LINK_TEXT, "Downloads")
print("LINK_TEXT:", link.text)

time.sleep(20)
driver.quit()