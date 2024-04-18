import allure
from main_page import YandexScooterMainPage
from base_page import YandexScooterBase


class TestYandexScooterQuestionAbout:

    @allure.title('Проверка открытия текста под кнопкой "Сколько это стоит?"')
    def test_how_much_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_how_much_button()
        assert main_page.check_how_much_text() == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Проверка открытия текста под кнопкой "Хочу несколько самокатов"')
    def test_few_scooter_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_few_scooter_button()
        assert main_page.check_few_scooter_text() == ("Пока что у нас так: один заказ — один самокат. Если хотите "
                                                      "покататься с друзьями, можете просто сделать несколько заказов —"
                                                      " один за другим.")

    @allure.title('Проверка открытия текста под кнопкой "Расчёт время аренды"')
    def test_how_arenda_time_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_how_arenda_time_button()
        assert main_page.check_how_arenda_time_text() == (
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в '
            'течение дня. Отсчёт времени аренды начинается с момента, '
            'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
            '20:30, суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Проверка открытия текста под кнопкой "Заказ самоката сегодня"')
    def test_can_order_scooter_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_can_order_scooter_button()
        assert main_page.check_can_order_scooter_text() == ("Только начиная с завтрашнего дня. Но скоро станем "
                                                            "расторопнее.")

    @allure.title('Проверка открытия текста под кнопкой "Вернуть самокат раньше"')
    def test_can_return_scooter_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_can_return_scooter_button()
        assert main_page.check_can_return_scooter_text() == ("Пока что нет! Но если что-то срочное — всегда можно "
                                                             "позвонить в поддержку по красивому номеру 1010.")

    @allure.title('Проверка открытия текста под кнопкой "Зарядка с самокатом"')
    def test_charger_with_scooter_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_charger_with_scooter_button()
        assert main_page.check_charger_with_scooter_text() == (
            "Самокат приезжает к вам с полной зарядкой. Этого хватает "
            "на восемь суток — даже если будете кататься без "
            "передышек и во сне. Зарядка не понадобится.")

    @allure.title('Проверка открытия текста под кнопкой "Отмена заказа"')
    def test_can_cancel_order_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.scroll_script()
        main_page.click_can_cancel_order_button()
        assert main_page.check_can_cancel_order_text() == ("Да, пока самокат не привезли. Штрафа не будет, "
                                                           "объяснительной записки тоже не попросим. Все же свои.")

    @allure.title('Проверка открытия текста под кнопкой "Жизнь за МКАДом"')
    def test_leave_za_mkadom_button_active(self, driver):
        main_page = YandexScooterMainPage(driver)
        bp = YandexScooterBase(driver)
        bp.click_cookie_button()
        main_page.wait_until_questions_download()
        main_page.scroll_script()
        main_page.click_leave_za_mkadom_button()
        assert main_page.check_leave_za_mkadom_text() == ("Да, обязательно. Всем самокатов! И Москве, и Московской "
                                                          "области.")
