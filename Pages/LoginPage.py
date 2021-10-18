class LoginPage():

        def __init__(self , driver):
            self.driver = driver

            self.username_textbox_name = "email"
            self.password_textbox_name= "passwd"
            self.Login_button_id = "SubmitLogin"

        def enter_username(self , username):
            self.driver.find_element_by_name(self.username_textbox_name).clear()
            self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

        def enter_password(self , Password):
            self.driver.find_element_by_name(self.password_textbox_name).clear()
            self.driver.find_element_by_name(self.password_textbox_name).send_keys(Password)

        def click_submit(self):
            self.driver.find_element_by_id(self.Login_button_id).click()



