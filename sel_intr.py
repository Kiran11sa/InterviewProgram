import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.Keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


username= "kirankodigela@gmail.com"
password = "8498046025"
@pytest.fixture(scope="function")
def setup():
    driver= webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.get("https://www.youtube.com/")
    time.sleep(5)
    try:
        login_buttn= driver.find_element(By.XPATH,'(//div[@class="yt-spec-touch-feedback-shape__fill"])[4]')
        login_buttn.click()
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//input[@aria-label="Email or phone"]')))
        username_text= driver.find_element(By.XPATH,'//input[@aria-label="Email or phone"]').send_keys(username)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Next"]')))
        next_buttn= driver.find_element(By.XPATH,'//span[text()="Next"]').click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '// input[ @ type = "password"]')))
        driver.find_element(By.XPATH,'// input[ @ type = "password"]').send_keys(password)
        driver.find_element(By.XPATH,'//span[text()="Next"]')
        time.sleep(20)
    except Exception as e:
        print(f"Exception as : {e}")

    # // span[text() = "Next"]

    # // input[ @ type = "password"]


