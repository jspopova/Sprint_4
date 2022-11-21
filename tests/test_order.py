import pages.page_order as po
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_order:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.description('На главной странице нажимаем кнопку "Заказать" внизу страницы. Заполняем информацию о пользователе и об аренде.Проверяем отображение модалки "Заказ оформлен"')
    def test_order_by_button_down(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 60)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Order = po.Order(self.driver)
        Order.person_information_button_down('Иван', 'Заболоцкий', 'ул.Ленина д.123 кв. 48','+79280974567')
        Order.about_rent('15.12.2022','Звоните в домофон 123, если не открою звоните по телефону +79280974567')
        res = Order.text_in_modal()
        assert res[0:14] == 'Заказ оформлен'

    @allure.description('На главной странице нажимаем кнопку "Заказать" вверху страницы. Заполняем информацию о пользователе и об аренде.Проверяем отображение модалки "Заказ оформлен"')
    def test_order_by_button_up(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        Order = po.Order(self.driver)
        Order.person_information_button_up('Кузя', 'Ким', 'ул.Пушкина д.1','89281234567')
        Order.about_rent('03.12.2022','Комментарий для курьера')
        res = Order.text_in_modal()
        assert res[0:14] == 'Заказ оформлен'





    @classmethod
    def teardown_class(cls):
        # закрой браузер

        cls.driver.quit()


#to = Test_order()
#to.test_order_by_button_down()