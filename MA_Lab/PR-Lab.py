import requests
from bs4 import BeautifulSoup
import inspect
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://google.com")

# This will get the initial html - before javascript
html1 = driver.page_source

# This will get the html after on-load javascript
html2 = driver.execute_script("return document.documentElement.innerHTML;")

//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[3]