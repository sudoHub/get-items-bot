# get_items.py

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

opts  = Options()

driver = Chrome(options=opts)   # set driver environment to Chrome browser

driver.get('https://www.bladehq.com/item--CIVIVI-Elementum-Liner-Lock-Knife--114184')

#find the "add to cart button" and click // Saving to buy_button for element testing
buy_button = driver.find_element_by_name("submit").click()

#find the checkout as guest button and click it
checkout_as_guest = driver.find_element_by_link_text("Checkout as Guest").click()

# fill out form

name = 'Full Name'
ship_address = '1234 Forever Way'
city = 'Los Angles'
zip = '90210'
phone_num = '801-555-3455'
email = 'bot@boter.com'

#insert full name
driver.find_element_by_id("sfull_name").send_keys(name)
driver.find_element_by_id("saddr1").send_keys(ship_address)
driver.find_element_by_id("scity").send_keys(city)
driver.find_element_by_id("szip").send_keys(zip)

# drop down menu for country
driver.find_element_by_xpath("//*[@id='scountry']/option[ text() = 'United States']").click()

# Drop down menu for State
driver.find_element_by_xpath("//*[@id='sstate']/option[text() = 'Utah']").click()

# Phone
driver.find_element_by_xpath("//*[@id='sphone']").send_keys(phone_num)

# email
driver.find_element_by_xpath("//*[@id='email_addr']").send_keys(email)

# Click Continue Checkout button
driver.find_element_by_xpath("//*[@id='checkout_new_addrs_form']/div[2]/div/div/div[2]/button").click()

print("Program Complete.")