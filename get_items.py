# get_items.py

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

opts  = Options()

driver = Chrome(options=opts)   # set driver environment to Chrome browser

driver.get('https://www.bladehq.com/item--CIVIVI-Elementum-Liner-Lock-Knife--114183')

#find the add to cart buttom and click
element = driver.find_element_by_name("submit").click()

print("Program Complete.")