import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page_locators import ScooterBasePage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на кнопку "Заказать" в шапке сайта')
    def click_order_button_header(self):
        self.driver.find_element(*ScooterBasePage.ORDER_BUTTON_ON_HEADER).click()

    @allure.step('Клик на лого "Самокат" в шапке сайта')
    def click_scooter_button_logo(self):
        self.driver.find_element(*ScooterBasePage.SCOOTER_LOGO_BUTTON_ON_HEADER).click()

    @allure.step('Клик на лого "Яндекс" в шапке сайта')
    def click_yandex_button_logo(self):
        self.driver.find_element(*ScooterBasePage.YANDEX_LOGO_BUTTON_ON_HEADER).click()

    @allure.step('Клик на кнопку "Принять куки"')
    def click_cookie_button(self):
        self.driver.find_element(*ScooterBasePage.ORDER_COOKIE_CONFIRM_BUTTON).click()

    def wait_until_two_number_of_windows(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

    def wait_until_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))

