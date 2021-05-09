# name="q"
# search_query
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

path = "/home/ddust/Documents/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://google.com")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys(Keys.RETURN)
url = "https://subhajitsaha.com/"
driver.get(url)

button =driver.find_element_by_link_text("Checkout my blog 📝")
button.click()

print(driver.page_source)
time.sleep(10)
driver.quit()




