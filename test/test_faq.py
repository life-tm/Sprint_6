import pytest
import allure
from pages.main_page import MainPage
from data import Urls, FaqData


@allure.feature("Раздел «Вопросы о важном»")
class TestFaq:
    @allure.title("Проверка текста ответа на вопрос №{index}")
    @pytest.mark.parametrize("index, expected_text", FaqData.ANSWERS)
    def test_faq_answer_matches_expected(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.accept_cookies()
        
        main_page.click_faq_question(index)
        actual_text = main_page.get_faq_answer_text(index)
        
        assert actual_text == expected_text
