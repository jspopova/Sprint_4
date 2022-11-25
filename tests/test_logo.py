from pages.page_logo import GoFromLogo
import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Testlogo:

    browser = None
    base_url = None

    @allure.description('На главной странице нажимаем кнопку "Заказть", '
                        'ищем логотип "Самокат", проверяем, что по клику на "Самокат" '
                        'осуществляется переход на главную страницу')
    def test_go_from_logo_bike(self, browser, base_url):
        logo = GoFromLogo(browser)
        browser.get(base_url)
        WebDriverWait(logo.driver, 10)
        logo.click_on_bike_logo()
        assert logo.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.description('На главной странице ищем логотип Яндекс, '
                        'проверяем, что по клику осуществляется переход на Яндекс Дзен')
    def test_go_from_logo_yandex(self, browser, base_url):
        logo = GoFromLogo(browser)
        browser.get(base_url)
        WebDriverWait(logo.driver, 10)
        logo.click_on_yandex_logo()
        original_window = logo.driver.current_window_handle
        WebDriverWait(logo.driver, 10).until(ec.number_of_windows_to_be(2))
        for window_handle in logo.driver.window_handles:
            if window_handle != original_window:
                logo.driver.switch_to.window(window_handle)
                break
        # Ждем пока догрузится вторая вкладка
        WebDriverWait(logo.driver, 10).until(ec.title_is("Дзен"))
        assert logo.driver.current_url == 'https://dzen.ru/?yredirect=true'
