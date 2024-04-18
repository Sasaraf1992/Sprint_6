from qa_python.Sprint_6.locators.order_page_locators import ScooterOrderPage


class YandexScooterOrder:

    def __init__(self,driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*ScooterOrderPage.ORDER_NAME_INPUT).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*ScooterOrderPage.ORDER_SURNAME_INPUT).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ScooterOrderPage.ORDER_ADDRESS_INPUT).send_keys(address)

    def set_phone_number(self, number):
        self.driver.find_element(*ScooterOrderPage.ORDER_NUMBER_INPUT).send_keys(number)

    def click_metro(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_METRO_STATION_BUTTON).click()

    def set_metro_cherkizovo(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_METRO_STATION_CHERKIZOVO).click()

    def set_metro_sokolniky(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_METRO_STATION_SOKOLNIKI).click()

    def click_next_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_NEXT_BUTTON).click()

    def click_date_field(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_WHEN_SCOOTER_COME_FIELD).click()

    def set_date_twenty_five(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_WHEN_SCOOTER_COME_DATE_1).click()

    def set_date_thirty(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_WHEN_SCOOTER_COME_DATE_2).click()

    def click_rental_period(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_RENTAL_PERIOD_BUTTON).click()

    def set_rental_date_three_days(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_RENTAL_PERIOD_DROP_DOWN_DAYS_1).click()

    def set_rental_date_one_day(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_RENTAL_PERIOD_DROP_DOWN_DAYS_2).click()

    def set_scooter_color_black(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_COLOR_BLACK_CHECKBOX).click()

    def set_scooter_color_gray(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_COLOR_GREY_CHECKBOX).click()

    def click_order_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_ORDER_BUTTON).click()

    def click_confirmation_уes_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_YES_BUTTON).click()

    def check_successful_order_header(self):
        return self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_SUCCESSFUL_HEADER).is_displayed()

    def click_cookie_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_COOKIE_CONFIRM_BUTTON).click()