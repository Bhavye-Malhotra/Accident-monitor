from selenium import webdriver
from selenium.webdriver.common.keys import Keys

lat="28.6818237"
lon="77.1562096"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://maps.google.com")

elem = driver.find_elements_by_id('searchbox')
elem.send_keys("hospital near " + lat + lon )
elem.send_keys(Keys.RETURN)

#driver.close()