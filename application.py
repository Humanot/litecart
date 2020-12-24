from selenium.webdriver import Chrome, Firefox, Opera, FirefoxOptions, DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#through options
#options = FirefoxOptions()
#options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe" #standart version
#driver = Firefox(options=options)

#just parameter
#driver = Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe") #standart version

#binary
# binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe") #standart version
# driver = Firefox(firefox_binary=binary) #standart version

class Application:
    def __init__(self):
        # capabilities
        caps = DesiredCapabilities.FIREFOX
        caps['binary'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        self.driver = Firefox(capabilities=caps)

    def destroy(self):
        self.driver.quit()
