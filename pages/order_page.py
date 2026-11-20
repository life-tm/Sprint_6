import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить первую страницу формы заказа")
    def fill_personal_info(self, user_data):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, user_data["name"])
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, user_data["surname"])
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, user_data["address"])
        
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.send_keys_to_element(OrderPageLocators.METRO_INPUT, user_data["metro"])
        self.click_element(OrderPageLocators.metro_station_option(user_data["metro"]))
        
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, user_data["phone"])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу формы заказа и подтвердить")
    def fill_rent_info_and_submit(self, user_data):
        date_field = self.find_visible_element(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(user_data["date"])
        date_field.send_keys(Keys.ENTER)

        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.rent_period_option(user_data["period"]))

        if user_data["color"] == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif user_data["color"] == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY_CHECKBOX)

        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, user_data["comment"])
        self.click_element(OrderPageLocators.ORDER_SUBMIT_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить отображение окна об успешном оформлении заказа")
    def is_order_success_modal_displayed(self):
        return self.find_visible_element(OrderPageLocators.ORDER_SUCCESS_MODAL).is_displayed()
