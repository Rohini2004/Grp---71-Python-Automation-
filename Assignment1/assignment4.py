from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open the HTML webpage
driver.get("file:///C:/Users/Rohini/Desktop/assignment4.html")

# Locate the Login button inside the login-section div
button = driver.find_element(
    By.CSS_SELECTOR,
    "#login-section > button"
)

# Click the button
button.click()

# Display message
print("Login button was successfully located and clicked.")

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()