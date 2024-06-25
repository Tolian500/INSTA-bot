from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
# Keeps the browser open after the script finishes executing
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Retrieve Instagram account credentials from environment variables
Insta_account_name = os.environ["NAME"]
Insta_account_password = os.environ["PASSWORD"]

def load_page(url):
    # Load the specified URL in the browser
    driver.get(url)

def accept_cookies():
    # Click the button to accept cookies
    driver.find_element(By.CSS_SELECTOR, value='button[class="_a9-- _ap36 _a9_0"]').click()

def get_follower_list():
    # Click the login button
    driver.find_element(By.CSS_SELECTOR, value='button[class=" _acan _acao _acat _aj1- _ap30"').click()
    time.sleep(1)

    # Enter the username
    name_input = driver.find_element(By.CSS_SELECTOR, value='input[name="username"]')
    name_input.send_keys(Insta_account_name)
    time.sleep(1)

    # Enter the password and press Enter to login
    pass_input = driver.find_element(By.CSS_SELECTOR, value='input[name="password"]')
    pass_input.send_keys(Insta_account_password, Keys.ENTER)
    time.sleep(4)

    # Accept the save login info prompt
    driver.find_element(By.CSS_SELECTOR, value='button[class=" _acan _acap _acas _aj1- _ap31"]').click()
    time.sleep(4)

    # Navigate to the followers list
    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(2)

    # Find all buttons for actions on the followers list (e.g., Follow buttons)
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap31')
    return buttons

# Load the specified Instagram page
load_page("https://www.instagram.com/tuszol/")
time.sleep(4)

# Accept cookies if prompted
accept_cookies()
time.sleep(2)

# Iterate over the follower list buttons and click each one
for button in get_follower_list():
    button.click()
    time.sleep(1.1)
