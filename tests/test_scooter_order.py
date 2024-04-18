from qa_python.Sprint_6 import settings
from selenium import webdriver
from qa_python.Sprint_6.pages.order_page import YandexScooterOrder
from qa_python.Sprint_6.pages.base_page import YandexScooterBase
import pytest
from qa_python.Sprint_6.data import ScooterTestData as SC


class TestYandexScooterOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()


    @pytest.mark.parametrize("name,surname,address,phone,click_cookie", [SC.USER_1,SC.USER_2])
    def test_button_order_on_header(self, name, surname, address, phone, click_cookie):
        self.driver.get(settings.URL)
        bp = YandexScooterBase(self.driver)
        bp.click_order_button_header()
        op = YandexScooterOrder(self.driver)
        op.set_name(name)
        op.set_surname(surname)
        op.set_address(address)
        op.click_metro()
        op.set_metro_sokolniky()
        op.set_phone_number(phone)
        if click_cookie:
            op.click_cookie_button()
        op.click_next_button()
        op.click_date_field()
        op.set_date_twenty_five()
        op.click_rental_period()
        op.set_rental_date_three_days()
        op.set_scooter_color_gray()
        self.driver.implicitly_wait(3)
        op.click_order_button()
        self.driver.implicitly_wait(3)
        op.click_confirmation_уes_button()
        assert op.check_successful_order_header()

        @classmethod
        def teardown_class(cls):
            cls.driver.quit()


