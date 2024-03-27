# Test case 1: login with with valid credentials using 1st "Start for free" button
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Navigate to the website
driver.get("https://wealthx.ai/")
# Maximize the browser window (optional)
driver.maximize_window()
# Wait for the button to be clickable
start_for_free_button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='investContainer']//div//a[@class='btn primary'][normalize-space()='Start for free']")))
# Click on the "Start for free" button
start_for_free_button1.click()
# Wait for the username input field to be visible
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your username']")))
# Input username
username_input.send_keys("oleg")
# Locate the password input field
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
# Input password
password_input.send_keys("Test123!")
# Locate and click the "Sign In" button
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
sign_in_button.click()
time.sleep(10)

# Close the browser window
# driver.quit()

# Close the browser
# driver.quit()


