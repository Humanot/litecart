class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_admin_page(self):
        self.app.driver.get("http://localhost/litecart/admin")
