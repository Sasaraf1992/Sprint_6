from selenium.webdriver.common.by import By

class ScooterMainPage:
    HOW_MUCH_COST_BUTTON = [By.ID, 'accordion__heading-0']
    HOW_MUCH_COST_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'Оплата курьеру')]"]
    WANT_FEW_SCOOTER_BUTTON = [By.ID, 'accordion__heading-1']
    WANT_FEW_SCOOTER_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'один заказ — один самокат')]"]
    HOW_ARENDA_TIME_CALCULATED_BUTTON = [By.ID, 'accordion__heading-2']
    HOW_ARENDA_TIME_CALCULATED_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ')]"]
    CAN_ORDER_SCOOTER_BUTTON = [By.ID, 'accordion__heading-3']
    CAN_ORDER_SCOOTER_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'Но скоро станем расторопнее')]"]
    CAN_RETURN_SCOOTER_BUTTON = [By.ID, 'accordion__heading-4']
    CAN_RETURN_SCOOTER_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'всегда можно позвонить в поддержку')]"]
    CHARGER_WITH_SCOOTER_BUTTON = [By.ID, 'accordion__heading-5']
    CHARGER_WITH_SCOOTER_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'Этого хватает на восемь суток')]"]
    CAN_CANCELL_ORDER_BUTTON = [By.ID, 'accordion__heading-6']
    CAN_CANCELL_ORDER_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'Штрафа не будет')]"]
    LEAVE_ZA_MKADOM_BUTTON = [By.ID, 'accordion__heading-7']
    LEAVE_ZA_MKADOM_DROP_DOWN_TEXT = [By.XPATH, "//p[contains(text(), 'Всем самокатов!')]"]
    ORDER_BUTTON_ON_MAIN_PAGE = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
    QUESTION_ABOUT_IMPORTANT_HEADER = [By.XPATH, "//div[text() = 'Вопросы о важном']"]


