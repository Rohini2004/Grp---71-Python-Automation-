# Assignment 3: CSS Selector Challenge
# Question:
# Locate web elements using CSS Selectors, including selectors with
# wildcards for elements having varying or dynamic attribute values.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/")

dynamic_elements = driver.find_elements(By.CSS_SELECTOR, "[id^='selenium-']")

print("Total elements found with ID starting with 'selenium-':", len(dynamic_elements))

for i, el in enumerate(dynamic_elements, start=1):
    print(f"{i}. ID: {el.get_attribute('id')} | Text: {el.text.strip()}")

input("Press Enter to close the browser...")
driver.quit()