import settings
from main_page_locators import ScooterMainPage


class TestYandexScooterQuestionAbout:

    def test_how_much_button_active(self, driver):
        driver.get(settings.URL)
        how_much_button = driver.find_element(*ScooterMainPage.HOW_MUCH_COST_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", how_much_button)
        how_much_button.click()
        how_much_text = driver.find_element(*ScooterMainPage.HOW_MUCH_COST_DROP_DOWN_TEXT).text
        assert how_much_text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_few_scooter_button_active(self, driver):
        driver.get(settings.URL)
        few_scooter_button = driver.find_element(*ScooterMainPage.WANT_FEW_SCOOTER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", few_scooter_button)
        few_scooter_button.click()
        few_scooter_text = driver.find_element(*ScooterMainPage.WANT_FEW_SCOOTER_DROP_DOWN_TEXT).text
        assert few_scooter_text == ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                                    "можете просто сделать несколько заказов — один за другим.")

    def test_how_arenda_time_button_active(self, driver):
        driver.get(settings.URL)
        how_arenda_time_button = driver.find_element(*ScooterMainPage.HOW_ARENDA_TIME_CALCULATED_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", how_arenda_time_button)
        how_arenda_time_button.click()
        how_much_arenda_time_text = driver.find_element(*ScooterMainPage.HOW_ARENDA_TIME_CALCULATED_DROP_DOWN_TEXT).text
        assert how_much_arenda_time_text == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в '
                                             'течение дня. Отсчёт времени аренды начинается с момента, '
                                             'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
                                             '20:30, суточная аренда закончится 9 мая в 20:30.')

    def test_can_order_scooter_button_active(self, driver):
        driver.get(settings.URL)
        can_order_scooter_button = driver.find_element(*ScooterMainPage.CAN_ORDER_SCOOTER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", can_order_scooter_button)
        can_order_scooter_button.click()
        can_order_scooter_text = driver.find_element(*ScooterMainPage.CAN_ORDER_SCOOTER_DROP_DOWN_TEXT).text
        assert can_order_scooter_text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_can_return_scooter_button_active(self, driver):
        driver.get(settings.URL)
        can_return_scooter_button = driver.find_element(*ScooterMainPage.CAN_RETURN_SCOOTER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", can_return_scooter_button)
        can_return_scooter_button.click()
        can_return_scooter_text = driver.find_element(*ScooterMainPage.CAN_RETURN_SCOOTER_DROP_DOWN_TEXT).text
        assert can_return_scooter_text == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку '
                                           'по красивому номеру 1010.')

    def test_charger_with_scooter_button_active(self, driver):
        driver.get(settings.URL)
        charger_with_scooter_button = driver.find_element(*ScooterMainPage.CHARGER_WITH_SCOOTER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", charger_with_scooter_button)
        charger_with_scooter_button.click()
        charger_with_scooter_text = driver.find_element(*ScooterMainPage.CHARGER_WITH_SCOOTER_DROP_DOWN_TEXT).text
        assert charger_with_scooter_text == ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток "
                                             "— даже если будете кататься без передышек и во сне. Зарядка не "
                                             "понадобится.")

    def test_can_cancel_order_button_active(self, driver):
        driver.get(settings.URL)
        can_cancel_order_button = driver.find_element(*ScooterMainPage.CAN_CANCELL_ORDER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", can_cancel_order_button)
        can_cancel_order_button.click()
        can_cancel_order_text = driver.find_element(*ScooterMainPage.CAN_CANCELL_ORDER_DROP_DOWN_TEXT).text
        assert can_cancel_order_text == ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже "
                                         "не попросим. Все же свои.")

    def test_leave_za_mkadom_button_active(self, driver):
        driver.get(settings.URL)
        leave_za_mkadom_button = driver.find_element(*ScooterMainPage.LEAVE_ZA_MKADOM_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", leave_za_mkadom_button)
        leave_za_mkadom_button.click()
        leave_za_mkadom_text = driver.find_element(*ScooterMainPage.LEAVE_ZA_MKADOM_DROP_DOWN_TEXT).text
        assert leave_za_mkadom_text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
