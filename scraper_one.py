from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
try:
    #Type desired search phrase
    alex = input("Please enter search phrase: ")

    #Accept the google cookies first
    driver.get("https://google.de")
    driver.find_element(By.ID,"L2AGLb").click()
    time.sleep(5)

    #Search for the given phrase
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(alex)
    search_box.submit()
    time.sleep(5)

    #Extract title and link using CSS selector
    results = driver.find_elements_by_css_selector('div.g')

    link = results[0].find_element_by_tag_name("a")
    href = link.get_attribute("href")
    driver.get(href)

    # Getting current URL source code
    get_title = driver.title
    # Printing the title of this URL
    print(get_title)
    print(href)

except (NoSuchElementException, TimeoutError) as e:
    print(f"An error occurred: {e}")
finally:
    #Close Browser
    driver.quit()
