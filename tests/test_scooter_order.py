import allure
from order_page import YandexScooterOrder
from base_page import YandexScooterBase
import pytest
from data import ScooterTestData as SC


class TestYandexScooterOrderPage:
    @allure.title('Проверка успешного заказа самоката с двумя наборами данных"')
    @pytest.mark.parametrize("name,surname,address,phone", [SC.USER_1, SC.USER_2])
    def test_button_order_on_header(self,driver, name, surname, address, phone):
        bp = YandexScooterBase(driver)
        bp.click_order_button_header()
        op = YandexScooterOrder(driver)
        op.set_name(name)
        op.set_surname(surname)
        op.set_address(address)
        op.click_metro()
        op.set_metro_sokolniky()
        op.set_phone_number(phone)
        bp.click_cookie_button()
        op.click_next_button()
        op.click_date_field()
        op.set_date_twenty_five()
        op.click_rental_period()
        op.set_rental_date_three_days()
        op.set_scooter_color_gray()
        op.click_order_button()
        op.click_confirmation_уes_button()
        assert op.check_successful_order_header()




