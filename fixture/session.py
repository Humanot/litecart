class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, adminname, password):
        driver = self.app.driver
        self.app.navigation.open_admin_page()

        # admin name
        admin_name = driver.find_element_by_name("username")
        admin_name.clear()
        admin_name.send_keys(adminname)

        # password
        admin_pass = driver.find_element_by_name("password")
        admin_pass.clear()
        admin_pass.send_keys(password)
        driver.find_element_by_name("login").click()