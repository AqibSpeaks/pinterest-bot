from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import PINTEREST_USERNAME, PINTEREST_PASSWORD, BOARD_URL, WEBSITE_URL

def post_to_pinterest(image_path, title, description):
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
    driver.get("https://www.pinterest.com/login/")
    
    # Login
    time.sleep(3)
    driver.find_element(By.NAME, "id").send_keys(PINTEREST_USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PINTEREST_PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    time.sleep(5)
    
    # Navigate to board pin builder
    driver.get(f"{BOARD_URL}pin-builder/")
    time.sleep(5)
    
    # Upload image
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)
    time.sleep(2)
    
    # Add title and description
    driver.find_element(By.NAME, "title").send_keys(title)
    driver.find_element(By.NAME, "description").send_keys(description)
    driver.find_element(By.NAME, "link").send_keys(WEBSITE_URL)
    
    # Publish pin
    driver.find_element(By.XPATH, "//button[contains(text(),'Publish')]").click()
    time.sleep(3)
    driver.quit()
