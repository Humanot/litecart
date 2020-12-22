from selenium.webdriver import Chrome, Firefox, Opera, FirefoxOptions, DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pytest

#through options
#options = FirefoxOptions()
#options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe" #standart version
#driver = Firefox(options=options)

#just parameter
#driver = Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe") #standart version

#binary
# binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe") #standart version
# driver = Firefox(firefox_binary=binary) #standart version

@pytest.fixture()
def app(request):
#capabilities
    caps = DesiredCapabilities.FIREFOX
    caps['binary'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
    driver = Firefox(capabilities=caps)

    def destroy():
        driver.quit()

    request.addfinalizer(destroy)
    return driver