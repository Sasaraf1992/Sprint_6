from selenium.webdriver.common.by import By


class ScooterBasePage:
    ORDER_BUTTON_ON_HEADER = [By.CLASS_NAME, 'Button_Button__ra12g']
    SCOOTER_LOGO_BUTTON_ON_HEADER = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    YANDEX_LOGO_BUTTON_ON_HEADER = [By.XPATH, "//a[@href='//yandex.ru']"]
    ORDER_COOKIE_CONFIRM_BUTTON = [By.XPATH, "//button[text() = 'да все привыкли']"]
