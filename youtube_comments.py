from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_youtube_comments(video_url, max_comments=100):
    """Scrapes YouTube comments using Selenium"""

    # Set up Chrome WebDriver
    options = webdriver.ChromeOptions()
    # Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(video_url)

    time.sleep(1)  # Allow page to load

    # Scroll down to load comments
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(10):  # Scroll multiple times
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    # Extract comments
    comment_elements = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    comments = [comment.text for comment in comment_elements[:max_comments]]

    driver.quit()
    return comments
