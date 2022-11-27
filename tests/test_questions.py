import allure
from pages.page_questions import Questions
from selenium.webdriver.support.wait import WebDriverWait


class TestQuestions:

    browser = None
    base_url = None

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Сколько это стоит"')
    def test_question_cost(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 11)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_cost_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_cost_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Хочу сразу несколько сокатов! Так можно?"')
    def test_question_more_then_1(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_more_then_1_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_more_then_1_text() == 'Пока что у нас так: один заказ — один самокат. ' \
                                              'Если хотите покататься с друзьями, ' \
                                              'можете просто сделать несколько заказов — один за другим.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Как рассчитывается время аренды?"')
    def test_question_rent_time(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_rent_time_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_rent_time_text() == 'Допустим, вы оформляете заказ на 8 мая. ' \
                                            'Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды ' \
                                            'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                                            'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_question_rent_today(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_rent_today_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_rent_today_text() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_question_continue_and_return(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_continue_and_return_question()
            break
        else:
            WebDriverWait(question.driver, 11)

        assert question.check_continue_and_return_text() == 'Пока что нет! Но если что-то срочное — всегда ' \
                                                      'можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_question_battery(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_battery_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_battery_text() == 'Самокат приезжает к вам с полной зарядкой. ' \
                                          'Этого хватает на восемь суток — даже если будете ' \
                                          'кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Можно ли отменить заказ?"')
    def test_question_cancel(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_cancel_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_cancel_text() == 'Да, пока самокат не привезли. Штрафа не будет, ' \
                                         'объяснительной записки тоже не попросим. Все же свои.'

    @allure.description('В разделе Вопросы о важном проверяем '
                        'текст ответа на вопрос "Я жизу за МКАДом, привезёте?"')
    def test_question_not_in_moscow(self, browser, base_url):
        question = Questions(browser)
        browser.get(base_url)
        question.hide_a_bike()
        WebDriverWait(question.driver, 10)
        while question.load_is_complete():
            question.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            question.click_on_not_in_moscow_question()
            break
        else:
            WebDriverWait(question.driver, 11)
        assert question.check_not_in_moscow_text() == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
