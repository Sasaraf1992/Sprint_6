from qa_python.Sprint_6.locators.main_page_locators import ScooterMainPage


class YandexScooterMainPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_script(self):
        element = self.driver.find_element(*ScooterMainPage.QUESTION_ABOUT_IMPORTANT_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_how_much_button(self):
        self.driver.find_element(*ScooterMainPage.HOW_MUCH_COST_BUTTON).click()

    def get_how_much_text(self):
        return self.driver.find_element(*ScooterMainPage.HOW_MUCH_COST_DROP_DOWN_TEXT).text

    def click_few_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.WANT_FEW_SCOOTER_BUTTON).click()

    def get_few_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.WANT_FEW_SCOOTER_DROP_DOWN_TEXT).text

    def click_how_arenda_time_button(self):
        self.driver.find_element(*ScooterMainPage.HOW_ARENDA_TIME_CALCULATED_BUTTON).click()

    def get_how_arenda_time_text(self):
        return self.driver.find_element(*ScooterMainPage.HOW_ARENDA_TIME_CALCULATED_DROP_DOWN_TEXT).text

    def click_can_order_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.CAN_ORDER_SCOOTER_BUTTON).click()

    def get_can_order_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.CAN_ORDER_SCOOTER_DROP_DOWN_TEXT).text

    def click_can_return_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.CAN_RETURN_SCOOTER_BUTTON).click()

    def get_can_return_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.CAN_RETURN_SCOOTER_DROP_DOWN_TEXT).text

    def click_charger_with_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.CHARGER_WITH_SCOOTER_BUTTON).click()

    def get_charger_with_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.CHARGER_WITH_SCOOTER_DROP_DOWN_TEXT).text

    def click_can_cancel_order_button(self):
        self.driver.find_element(*ScooterMainPage.CAN_CANCELL_ORDER_BUTTON).click()

    def get_can_cancel_order_text(self):
        return self.driver.find_element(*ScooterMainPage.CAN_CANCELL_ORDER_DROP_DOWN_TEXT).text

    def click_leave_za_mkadom_button(self):
        self.driver.find_element(*ScooterMainPage.LEAVE_ZA_MKADOM_BUTTON).click()

    def get_leave_za_mkadom_text(self):
        return self.driver.find_element(*ScooterMainPage.LEAVE_ZA_MKADOM_DROP_DOWN_TEXT).text