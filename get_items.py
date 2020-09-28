# get_items.py

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

opts  = Options()

driver = Chrome(options=opts)   # set driver environment to Chrome browser

driver.get('https://www.bladehq.com/item--CIVIVI-Elementum-Liner-Lock-Knife--114184')

#find the "add to cart button" and click
buy_button = driver.find_element_by_name("submit").click()

#find the checkout as guest button and click it
checkout_as_guest = driver.find_element_by_link_text("Checkout as Guest").click()

# fill out form

name = 'Full Name'
ship_address = '1234 Forever Way'
city = 'Los Angles'
zip = '90210'
phone_num = '5553455'
email = 'bot@boter.com'

#insert full name
driver.find_element_by_id("sfull_name").send_keys(name)
driver.find_element_by_id("saddr1").send_keys(ship_address)
driver.find_element_by_id("scity").send_keys(city)
driver.find_element_by_id("szip").send_keys(zip)

# drop down menu for country
# Phone
# email

# Click Continue Checkout button

print("Program Complete.")