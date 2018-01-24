from tests.pages.base_pages.base_page import BasePage


class CalculatorPage(BasePage):

    ID = "com.maroyakasoft.dentak:id/button_"
    MULT = "com.maroyakasoft.dentak:id/button_kakeru"
    SUB = "com.maroyakasoft.dentak:id/button_minos"
    DIV = "com.maroyakasoft.dentak:id/button_waru"
    SUM = "com.maroyakasoft.dentak:id/button_plus"
    EQUAL = "com.maroyakasoft.dentak:id/button_ikoru"
    RESULT = "com.maroyakasoft.dentak:id/display"
    FORMULA = "com.maroyakasoft.dentak:id/textView_formula"
    DISPLAY = "com.maroyakasoft.dentak:id/display"
    CLEAR = "com.maroyakasoft.dentak:id/button_clear"
    PERCENT = "com.maroyakasoft.dentak:id/button_percent"


    def click_number(self, numero):
        self.driver.find_element_by_id(self.ID + numero).click()

    def click_mult(self):
        self.driver.find_element_by_id(self.MULT).click()

    def click_sum(self):
        self.driver.find_element_by_id(self.SUM).click()

    def click_sub(self):
        self.driver.find_element_by_id(self.SUB).click()

    def click_div(self):
        self.driver.find_element_by_id(self.DIV).click()

    def click_equal(self):
        self.driver.find_element_by_id(self.EQUAL).click()

    def click_clear(self):
        self.driver.find_element_by_id(self.CLEAR).click()
    
    def click_percent(self):
        self.driver.find_element_by_id(self.PERCENT).click()
