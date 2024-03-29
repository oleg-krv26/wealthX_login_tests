# Test case 5: login with valid credentials using "Sign Up" for free button
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testSignUpButton():
    driver = webdriver.Chrome()
    driver.get("https://wealthx.ai/")
    driver.maximize_window()
    sign_up_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn secondary']")))
    sign_up_button.click()
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
