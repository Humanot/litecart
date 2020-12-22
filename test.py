def test_login(app):
    driver = app
    driver.get("http://localhost/litecart/admin")
    admin_name = driver.find_element_by_name("username")
    admin_name.clear()
    admin_name.send_keys("admin")

    admin_pass = driver.find_element_by_name("password")
    admin_pass.clear()
    admin_pass.send_keys("secret")


    driver.find_element_by_name("login").click()
