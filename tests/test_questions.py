import allure
import pages.page_questions as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_questions:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()


    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Сколько это стоит"')
    def test_question_cost(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        question = pq.Questions(self.driver)
        WebDriverWait(self.driver, 10)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.cost_click()
        assert question.cost_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Хочу сразу несколько сокатов! Так можно?"')
    def test_question_more_then_1(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.more_1_click()
        assert question.more_then_1_text() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Как рассчитывается время аренды?"')
    def test_question_rent_time(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.rent_time_click()
        assert question.rent_time_text() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_question_rent_today(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.rent_today_click()
        assert question.rent_today_text() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_question_continue_and_return(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.continue_and_return_click()
        assert question.continue_and_return_text() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_question_battery(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.battery_click()
        assert question.battery_text() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Можно ли отменить заказ?"')
    def test_question_cancel(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.cancel_click()
        assert question.cancel_text() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.description('В разделе Вопросы о важном проверяем текст ответа на вопрос "Я жизу за МКАДом, привезёте?"')
    def test_question_not_in_Moscow(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        WebDriverWait(self.driver, 10)
        question = pq.Questions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        question.not_in_Moscow_click()
        assert question.not_in_Moscow_text() == "Да, обязательно. Всем самокатов! И Москве, и Московской области."


    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()





#tc = Test_questions()
#tc.test_question_cancel()