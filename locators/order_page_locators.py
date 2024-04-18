from selenium.webdriver.common.by import By

class ScooterOrderPage:
    ORDER_NAME_INPUT = [By.XPATH, "//*[@placeholder = '* Имя']"]
    ORDER_SURNAME_INPUT = [By.XPATH, "//*[@placeholder = '* Фамилия']"]
    ORDER_ADDRESS_INPUT = [By.XPATH, "//*[@placeholder = '* Адрес: куда привезти заказ']"]
    ORDER_METRO_STATION_BUTTON = [By.XPATH, "//*[@placeholder = '* Станция метро']"]
    ORDER_METRO_STATION_SOKOLNIKI = [By.XPATH, "//button/div[2][(@class = 'Order_Text__2broi') and (text() = 'Сокольники')]"]
    ORDER_NUMBER_INPUT = [By.XPATH, "//*[@placeholder = '* Телефон: на него позвонит курьер']"]
    ORDER_NEXT_BUTTON = [By.XPATH, "//button[text() = 'Далее']"]
    ORDER_WHEN_SCOOTER_COME_FIELD = [By.XPATH, "//*[@placeholder = '* Когда привезти самокат']"]
    ORDER_WHEN_SCOOTER_COME_DATE_1 = [By.XPATH, "//*[@aria-label = 'Choose четверг, 25-е апреля 2024 г.']"]
    ORDER_RENTAL_PERIOD_BUTTON = [By.XPATH, "//div[text() = '* Срок аренды']"]
    ORDER_RENTAL_PERIOD_DROP_DOWN_DAY = [By.XPATH, "//div[text() = 'трое суток']"]
    ORDER_SCOOTER_COLOR_GREY_CHECKBOX = [By.ID, "grey"]
    ORDER_SCOOTER_ORDER_BUTTON = [By.XPATH, "//button[2][text() = 'Заказать']"]
    ORDER_SCOOTER_YES_BUTTON = [By.XPATH,"//button[text() = 'Да']"]
    ORDER_SCOOTER_SUCCESSFUL_HEADER = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
