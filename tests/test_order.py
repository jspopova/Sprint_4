from pages.page_order import Order
import allure
from selenium.webdriver.support.wait import WebDriverWait


class TestOrder:

    browser = None
    base_url = None

    @allure.description('На главной странице нажимаем кнопку "Заказать" внизу страницы. '
                        'Заполняем информацию о пользователе и об аренде. '
                        'Проверяем отображение модалки "Заказ оформлен"')
    def test_order_by_button_down(self, browser, base_url):
        ord_ivan = Order(browser)
        browser.get(base_url)
        WebDriverWait(ord_ivan.driver, 10)
        ord_ivan.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ord_ivan.fill_person_info_by_button_down('Иван', 'Заболоцкий', 'ул.Ленина д.123 кв. 48', '+79280974567')
        ord_ivan.fill_info_in_about_rent_form('15.12.2022', 'Звоните в домофон 123, если не открою звоните по телефону +79280974567')
        res = ord_ivan.input_text_in_modal()
        assert res[0:14] == 'Заказ оформлен'

    @allure.description('На главной странице нажимаем кнопку "Заказать" вверху страницы. '
                        'Заполняем информацию о пользователе и об аренде. '
                        'Проверяем отображение модалки "Заказ оформлен"')
    def test_order_by_button_up(self, browser, base_url):
        ord_kuzya = Order(browser)
        browser.get(base_url)
        WebDriverWait(ord_kuzya.driver, 10)
        ord_kuzya.fill_person_info_by_button_up('Кузя', 'Ким', 'ул.Пушкина д.1', '89281234567')
        ord_kuzya.fill_info_in_about_rent_form('03.12.2022', 'Комментарий для курьера')
        res = ord_kuzya.input_text_in_modal()
        assert res[0:14] == 'Заказ оформлен'
