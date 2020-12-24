from selenium.webdriver import Firefox, DesiredCapabilities
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        # capabilities
        caps = DesiredCapabilities.FIREFOX
        caps['binary'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        self.driver = Firefox(capabilities=caps)
        self.session = SessionHelper(self)

    def open_admin_page(self):
        self.driver.get("http://localhost/litecart/admin")

    def destroy(self):
        self.driver.quit()
