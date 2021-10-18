class ProductsPage():

    def __init__(self , driver):
        self.driver = driver

        self.button_women_xpath = "//a[contains(text(),'Women') and @title='Women']"
        self.button_Dresses_xpath = "//a[contains(text(),'Dresses') and @class='subcategory-name']"
        self.button_SummerDresses_xpath = "//a[contains(text(),'Summer Dresses') and @class='subcategory-name']"


    def click_women(self):
        self.driver.find_element_by_xpath(self.button_women_xpath).click()

    def click_Dresses(self):
        self.driver.find_element_by_xpath(self.button_Dresses_xpath).click()

    def click_SummerDresses(self):
        self.driver.find_element_by_xpath(self.button_SummerDresses_xpath).click()

