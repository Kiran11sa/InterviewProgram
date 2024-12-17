
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Define login credentials
username = "kirankodigela@gmail.com"
password = "8498046025"

# Fixture for setting up the driver in incognito mode
@pytest.fixture(scope="function")
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Enable incognito mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.get("https://www.youtube.com/")
    time.sleep(5)
    try:
        # Locate and click the login button
        login_buttn = driver.find_element(By.XPATH, '(//div[@class="yt-spec-touch-feedback-shape__fill"])[4]')
        login_buttn.click()

        # Enter the username
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Email or phone"]')))
        driver.find_element(By.XPATH, '//input[@aria-label="Email or phone"]').send_keys(username)

        # Click 'Next' button
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Next"]')))
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        time.sleep(5)

        # Enter the password
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)

        # Click 'Next' button after entering password
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        time.sleep(20)

    except Exception as e:
        print(f"Exception as : {e}")
