import settings
from base_page import YandexScooterBase
import allure


class TestLogoButtonsOnHeader:

    @allure.title('Проверка перехода по клику на кнопку "Яндекс" в лого')
    def test_click_yandex_logo_on_header(self, driver):
        bp = YandexScooterBase(driver)
        bp.click_yandex_button_logo()
        bp.wait_until_two_number_of_windows()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        dzen_url = "https://dzen.ru/?yredirect=true"
        bp.wait_until_url_contains(dzen_url)
        assert driver.current_url == dzen_url

    @allure.title('Проверка перехода по клику на кнопку "Самокат" в лого')
    def test_click_scooter_logo_on_headers(self, driver):
        driver.get(settings.URL + "order")
        bp = YandexScooterBase(driver)
        bp.click_scooter_button_logo()
        main_page_url = "https://qa-scooter.praktikum-services.ru/"
        assert driver.current_url == main_page_url
