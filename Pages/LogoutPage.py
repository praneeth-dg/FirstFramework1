class LogoutPage():

    def __init__(self, driver):
        self.driver = driver

        self.logout_button_xpath = "//a[contains(@class,'logout')]"

    def click_submit(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

