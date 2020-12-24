from selenium.webdriver import Firefox, DesiredCapabilities
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper

class Application:
    def __init__(self):
        # capabilities
        caps = DesiredCapabilities.FIREFOX
        caps['binary'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        self.driver = Firefox(capabilities=caps)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.driver.quit()
