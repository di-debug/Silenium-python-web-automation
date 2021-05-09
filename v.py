# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# selecting Firefox as the browser
# in order to select Chrome
# webdriver.Chrome() will be used
path = "/home/ddust/Documents/chromedriver"
driver = webdriver.Chrome(path)

# URL of the website
url = "https://www.youtube.com/"

# opening link in the browser
driver.get(url)

search = driver.find_element_by_name("search_query")
search.send_keys("hacktech")
search.send_keys(Keys.RETURN)