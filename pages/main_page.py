from main_page_locators import ScooterMainPage
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage


class YandexScooterMainPage(BasePage):

    @allure.step('Прокручиваем страницу до "Вопросы о важном"')
    def scroll_script(self):
        element = self.driver.find_element(*ScooterMainPage.QUESTION_ABOUT_IMPORTANT_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик на кнопку "Сколько это стоит?"')
    def click_how_much_button(self):
        self.driver.find_element(*ScooterMainPage.HOW_MUCH_COST_BUTTON).click()
        return self.driver.find_element(*ScooterMainPage.HOW_MUCH_COST_DROP_DOWN_TEXT).text

    @allure.step('Проверка наличия текста под кнопкой "Сколько это стоит?"')
    def check_how_much_text(self):
        return self.driver.find_element(*ScooterMainPage.HOW_MUCH_COST_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Хочу несколько самокатов!"')
    def click_few_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.WANT_FEW_SCOOTER_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Хочу несколько самокатов!"')
    def check_few_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.WANT_FEW_SCOOTER_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Расчет время аренды"')
    def click_how_arenda_time_button(self):
        self.driver.find_element(*ScooterMainPage.HOW_ARENDA_TIME_CALCULATED_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Расчет время аренды"')
    def check_how_arenda_time_text(self):
        return self.driver.find_element(*ScooterMainPage.HOW_ARENDA_TIME_CALCULATED_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Заказ самоката сегодня"')
    def click_can_order_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.CAN_ORDER_SCOOTER_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Заказ самоката сегодня"')
    def check_can_order_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.CAN_ORDER_SCOOTER_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Вернуть самокат раньше"')
    def click_can_return_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.CAN_RETURN_SCOOTER_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Вернуть самокат раньше"')
    def check_can_return_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.CAN_RETURN_SCOOTER_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Зарядка с самокатом"')
    def click_charger_with_scooter_button(self):
        self.driver.find_element(*ScooterMainPage.CHARGER_WITH_SCOOTER_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Зарядка с самокатом"')
    def check_charger_with_scooter_text(self):
        return self.driver.find_element(*ScooterMainPage.CHARGER_WITH_SCOOTER_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Отмена заказа"')
    def click_can_cancel_order_button(self):
        self.driver.find_element(*ScooterMainPage.CAN_CANCELL_ORDER_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Отмена заказа"')
    def check_can_cancel_order_text(self):
        return self.driver.find_element(*ScooterMainPage.CAN_CANCELL_ORDER_DROP_DOWN_TEXT).text

    @allure.step('Клик на кнопку "Жизнь за МКАДом"')
    def click_leave_za_mkadom_button(self):
        self.driver.find_element(*ScooterMainPage.LEAVE_ZA_MKADOM_BUTTON).click()

    @allure.step('Проверка наличия текста под кнопкой "Жизнь за МКАДом"')
    def check_leave_za_mkadom_text(self):
        return self.driver.find_element(*ScooterMainPage.LEAVE_ZA_MKADOM_DROP_DOWN_TEXT).text

    def wait_until_questions_download(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(ScooterMainPage.QUESTION_ABOUT_IMPORTANT_HEADER))
