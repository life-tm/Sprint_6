import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open_url(self, url):
        self.driver.get(url)

    def find_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_element(self, locator):
        self.find_clickable_element(locator).click()

    def send_keys_to_element(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку браузера")
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидать наличия '{url_part}' в URL")
    def wait_for_url_contains(self, url_part, timeout=25):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))
