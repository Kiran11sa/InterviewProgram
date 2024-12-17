import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants for credentials and URL
YOUTUBE_URL = "https://www.youtube.com/"
USERNAME = "your_username_here"  # Replace with actual username
PASSWORD = "your_password_here"  # Replace with actual password


# Initialize driver setup
@pytest.fixture(scope="function")
def setup():
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # service = Service("/path/to/chromedriver")  # Replace with actual path to chromedriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Global implicit wait
    yield driver
    driver.quit()


# Function to open YouTube and wait for the page to load
def open_youtube(driver):
    driver.get(YOUTUBE_URL)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//tp-yt-paper-button[@aria-label='Sign in']")))


# Function to click login button
def click_login_button(driver):
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[@aria-label='Sign in']"))
    )
    login_button.click()


# Function to handle any alerts
def handle_alert(driver):
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.dismiss()
    except:
        pass  # No alert present


# Function to log in with username and password
def login(driver, username, password):
    username_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierId")))
    username_input.send_keys(username)
    driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

    password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(password)
    driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()


# Function to search for a query
def search_video(driver, query):
    search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


# Function to click the first video result
def click_first_video(driver):
    first_video = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@id='video-title'])[1]")))
    first_video.click()


# Function to click the subscribe button if not already subscribed
def subscribe_channel(driver):
    try:
        subscribe_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Subscribe']")))
        subscribe_button.click()
    except:
        pass  # Already subscribed or button not available


# Main test case using the defined functions
def test_youtube_login_and_search(setup):
    driver = setup

    # Execute each function in order
    open_youtube(driver)
    click_login_button(driver)
    handle_alert(driver)
    login(driver, USERNAME, PASSWORD)
    search_video(driver, "java")
    click_first_video(driver)
    subscribe_channel(driver)

# To run the test, save this script as `test_youtube.py` and use the command:
# pytest test_youtube.py --headed
