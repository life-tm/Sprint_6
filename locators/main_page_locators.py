from selenium.webdriver.common.by import By


class MainPageLocators:
    # Куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Логотипы в шапке
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")

    # Кнопки "Заказать"
    ORDER_BUTTON_HEADER = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUTTON_PAGE = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    # Блок "Вопросы о важном" (динамические локаторы по индексу 0..7)
    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def faq_answer(index):
        return (By.ID, f"accordion__panel-{index}")
