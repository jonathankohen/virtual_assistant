# import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from gtts import gTTS


browser = webdriver.Chrome(ChromeDriverManager(version="91.0.4472.19").install())

query = "beavers"

browser.get("https://en.wikipedia.org")
time.sleep(2)

wiki = browser.find_element_by_xpath('//*[@id="searchInput"]')
wiki.send_keys(query)

search_btn = browser.find_element_by_xpath('//*[@id="searchButton"]')
search_btn.click()

# tts = gTTS("hello")
# tts.save("hello.mp3")

# //*[@id="mw-content-text"]/div[1]/p[2]