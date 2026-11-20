import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls, OrderData


@allure.feature("Оформление заказа и навигация по логотипам")
class TestOrderAndLogos:
    @allure.title("Позитивный сценарий заказа самоката через разные точки входа")
    @pytest.mark.parametrize(
        "entry_point, user_data",
        [
            ("header", OrderData.USER_1),
            ("page", OrderData.USER_2),
        ]
    )
    def test_create_order_positive_flow(self, driver, entry_point, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_url(Urls.MAIN_PAGE)
        main_page.accept_cookies()

        if entry_point == "header":
            main_page.click_header_order_button()
        else:
            main_page.click_page_order_button()

        order_page.fill_personal_info(user_data)
        order_page.fill_rent_info_and_submit(user_data)

        assert order_page.is_order_success_modal_displayed()

    @allure.title("Переход на главную страницу при клике на логотип «Самокат»")
    def test_click_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.click_header_order_button()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Открытие Дзена в новой вкладке при клике на логотип «Яндекс»")
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.wait_for_url_contains(Urls.DZEN_URL_PART)

        assert Urls.DZEN_URL_PART in main_page.get_current_url()
