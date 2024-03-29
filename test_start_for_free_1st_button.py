# Test case 1: login with valid credentials using 1st "Start for free" button
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testStartForFreeButton1():
    driver = webdriver.Chrome()
    driver.get("https://wealthx.ai/")
    driver.maximize_window()
    start_for_free_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='investContainer']//div//a[@class='btn primary'][normalize-space()='Start for free']")))
    start_for_free_button1.click()
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
