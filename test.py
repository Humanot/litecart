from selenium.webdriver import Chrome, Firefox, Opera, FirefoxOptions, DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

#through options
#options = FirefoxOptions()
#options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe" #standart version
#driver = Firefox(options=options)

#just parameter
#driver = Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe") #standart version

#binary
# binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe") #standart version
# driver = Firefox(firefox_binary=binary) #standart version

#capabilities
caps = DesiredCapabilities.FIREFOX
caps['binary'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
driver = Firefox(capabilities=caps)
print(caps)

driver.get("http://localhost/litecart/admin")
admin_name = driver.find_element_by_name("username")
admin_name.clear()
admin_name.send_keys("admin")

admin_pass = driver.find_element_by_name("password")
admin_pass.clear()
admin_pass.send_keys("secret")


driver.find_element_by_name("login").click()
time.sleep(50)
driver.quit()