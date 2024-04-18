from order_page_locators import ScooterOrderPage
import allure

class YandexScooterOrder:

    def __init__(self,driver):
        self.driver = driver

    @allure.step('Ввод имени в поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(*ScooterOrderPage.ORDER_NAME_INPUT).send_keys(name)

    @allure.step('Ввод фамилии в поле "Фамилия"')
    def set_surname(self, surname):
        self.driver.find_element(*ScooterOrderPage.ORDER_SURNAME_INPUT).send_keys(surname)

    @allure.step('Ввод адреса в поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*ScooterOrderPage.ORDER_ADDRESS_INPUT).send_keys(address)

    @allure.step('Ввод телефона в поле "Телефон"')
    def set_phone_number(self, number):
        self.driver.find_element(*ScooterOrderPage.ORDER_NUMBER_INPUT).send_keys(number)

    @allure.step('Клик в поле "Метро"')
    def click_metro(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_METRO_STATION_BUTTON).click()

    @allure.step('Выбор метро "Сокольники" из выпадающего списка')
    def set_metro_sokolniky(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_METRO_STATION_SOKOLNIKI).click()

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_NEXT_BUTTON).click()

    @allure.step('Клик в поле "Дата"')
    def click_date_field(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_WHEN_SCOOTER_COME_FIELD).click()
    @allure.step('Выбор даты')
    def set_date_twenty_five(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_WHEN_SCOOTER_COME_DATE_1).click()

    @allure.step('Клик на кнопку "Срок аренды"')
    def click_rental_period(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_RENTAL_PERIOD_BUTTON).click()

    @allure.step('Выбор срока аренды')
    def set_rental_date_three_days(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_RENTAL_PERIOD_DROP_DOWN_DAY).click()

    @allure.step('Выбор цвета самоката')
    def set_scooter_color_gray(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_COLOR_GREY_CHECKBOX).click()

    @allure.step('Клик на кнопку "Заказать" под формой заказа')
    def click_order_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_ORDER_BUTTON).click()

    @allure.step('Клик на кнопку "Да"')
    def click_confirmation_уes_button(self):
        self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_YES_BUTTON).click()

    @allure.step('Проверка отображения всплывающего окна "Заказ оформлен')
    def check_successful_order_header(self):
        return self.driver.find_element(*ScooterOrderPage.ORDER_SCOOTER_SUCCESSFUL_HEADER).is_displayed()