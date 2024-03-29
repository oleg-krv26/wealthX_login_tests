# Test case 3: login with valid credentials using 3rd "Start for free" button
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testStartGrowYourWealthButton():
    driver = webdriver.Chrome()
    driver.get("https://wealthx.ai/")
    driver.maximize_window()
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button_start_growing_your_wealth_now = "//a[normalize-space()='Start growing your wealth now!']"
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_start_growing_your_wealth_now)))
    button.click()
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your username']")))
    username_input.send_keys("oleg")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
    password_input.send_keys("Test123!")
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
    sign_in_button.click()
    time.sleep(5)
