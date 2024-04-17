from qa_python.Sprint_6 import settings
from selenium import webdriver
from qa_python.Sprint_6.pages.main_page import YandexScooterMainPage


class TestYandexScooterQuestionAbout:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_how_much_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_how_much_button()
        assert main_page.get_how_much_text() == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_few_scooter_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_few_scooter_button()
        assert main_page.get_few_scooter_text() == ("Пока что у нас так: один заказ — один самокат. Если хотите "
                                                    "покататься с друзьями, можете просто сделать несколько заказов —"
                                                    " один за другим.")

    def test_how_arenda_time_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_how_arenda_time_button()
        assert main_page.get_how_arenda_time_text() == (
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в '
            'течение дня. Отсчёт времени аренды начинается с момента, '
            'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
            '20:30, суточная аренда закончится 9 мая в 20:30.')

    def test_can_order_scooter_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_can_order_scooter_button()
        assert main_page.get_can_order_scooter_text() == ("Только начиная с завтрашнего дня. Но скоро станем "
                                                          "расторопнее.")

    def test_can_return_scooter_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_can_return_scooter_button()
        assert main_page.get_can_return_scooter_text() == ("Пока что нет! Но если что-то срочное — всегда можно "
                                                           "позвонить в поддержку по красивому номеру 1010.")

    def test_charger_with_scooter_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_charger_with_scooter_button()
        assert main_page.get_charger_with_scooter_text() == ("Самокат приезжает к вам с полной зарядкой. Этого хватает "
                                                             "на восемь суток — даже если будете кататься без "
                                                             "передышек и во сне. Зарядка не понадобится.")

    def test_can_cancel_order_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_can_cancel_order_button()
        assert main_page.get_can_cancel_order_text() == ("Да, пока самокат не привезли. Штрафа не будет, "
                                                         "объяснительной записки тоже не попросим. Все же свои.")

    def test_leave_za_mkadom_button_active(self):
        self.driver.get(settings.URL)
        main_page = YandexScooterMainPage(self.driver)
        main_page.scroll_script()
        main_page.click_leave_za_mkadom_button()
        assert main_page.get_leave_za_mkadom_text() == ("Да, обязательно. Всем самокатов! И Москве, и Московской "
                                                        "области.")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
