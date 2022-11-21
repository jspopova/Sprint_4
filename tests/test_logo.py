import pages.page_logo as pl
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Test_logo:

    driver = webdriver.Firefox()


    @classmethod

    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.description('На главной странице нажимаем кнопку "Заказть", ищем логотип "Самокат", проверяем, что по клику на "Самокат" осуществляется переход на главную страницу')
    def test_go_from_logo_bike(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        logo = pl.Go_from_logo(self.driver)
        logo.bike_click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.description('На главной странице ищем логотип Яндекс, проверяем, что по клику осуществляется переход на Яндекс Дзен')
    def test_go_from_logo_yandex(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        logo = pl.Go_from_logo(self.driver)
        logo.yandex_click()
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
      #Ждем пока догрузится вторая вкладка
        WebDriverWait(self.driver, 10).until(EC.title_is("Дзен"))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'




    @classmethod

    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()


#tc = Test_logo()
#tc.test_go_from_logo_yandex()