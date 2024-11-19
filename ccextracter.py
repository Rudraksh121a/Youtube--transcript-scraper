from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def ccextract(url:str):
    content=[]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    more=driver.find_element(By.ID,'expand')
    more.click()
    time.sleep(2)
    cc_button=driver.find_element(By.XPATH,"//button[@aria-label='Show transcript']")
    cc_button.click()
    time.sleep(3)
    page=driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    formatted_strings = soup.find_all('yt-formatted-string', class_='segment-text style-scope ytd-transcript-segment-renderer')
    driver.quit()
    if formatted_strings:
        for string in formatted_strings:
            # print(string.text.strip())
            content.append(string.text.strip())
        return content

