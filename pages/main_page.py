import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять куки, если баннер отображается")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Нажать на логотип «Самокат»")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип «Яндекс»")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Нажать на кнопку «Заказать» в шапке")
    def click_header_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать на кнопку «Заказать» внизу страницы")
    def click_page_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_PAGE)
        self.click_element(MainPageLocators.ORDER_BUTTON_PAGE)

    @allure.step("Нажать на вопрос №{index} в разделе «Вопросы о важном»")
    def click_faq_question(self, index):
        locator = MainPageLocators.faq_question(index)
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получить текст ответа №{index}")
    def get_faq_answer_text(self, index):
        locator = MainPageLocators.faq_answer(index)
        return self.find_visible_element(locator).text
