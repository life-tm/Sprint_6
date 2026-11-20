from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1: Для кого самокат
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    @staticmethod
    def metro_station_option(station_name):
        return (By.XPATH, f".//div[text()='{station_name}']/parent::button")

    # Шаг 2: Про аренду
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    @staticmethod
    def rent_period_option(period_text):
        return (By.XPATH, f".//div[@class='Dropdown-option' and text()='{period_text}']")

    # Модальное окно подтверждения
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
