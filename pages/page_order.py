from pages.BasePage import BasePage
from locators.base_page_locators import Locator
from selenium.webdriver.support.wait import WebDriverWait


class Order(BasePage):
    loc = Locator()
    order_button_up = loc.order_button_up
    input_name = loc.input_name
    input_surname = loc.input_surname
    input_address = loc.input_address
    input_metro = loc.input_metro
    select_metro = loc.select_metro
    div_order_time = loc.div_order_time
    input_phone = loc.input_phone
    input_when = loc.input_when
    select_time = loc.select_time
    input_color_black = loc.input_color_black
    input_comment = loc.input_comment
    order_button_down = loc.order_button_down
    button_next = loc.button_next
    input_color_grey = loc.input_color_grey
    order_button_middle = loc.order_button_middle
    button_want_order = loc.button_want_order
    div_ok_order = loc.div_ok_order

    def click_on_order_up_button(self):
        self.driver.find_element(*self.order_button_up).click()

    def click_on_order_down_button(self):
        self.driver.find_element(*self.order_button_down).click()

    def input_name_to_order_form(self, person_name):
        self.driver.find_element(*self.input_name).send_keys(person_name)

    def input_surname_to_order_form(self, person_surname):
        self.driver.find_element(*self.input_surname).send_keys(person_surname)

    def input_address_to_order_form(self, person_address):
        self.driver.find_element(*self.input_address).send_keys(person_address)

    def input_phone_to_order_form(self, person_phone):
        self.driver.find_element(*self.input_phone).send_keys(person_phone)

    def input_metro_to_order_form(self):
        self.driver.find_element(*self.input_metro).click()
        WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.select_metro).click()

    def input_div_order_time(self):
        self.driver.find_element(*self.div_order_time).click()
        WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.select_time).click()

    def click_on_next_button(self):
        self.driver.find_element(*self.button_next).click()

    def input_when_to_order_form(self, when_date):
        self.driver.find_element(*self.input_when).click()
        self.driver.find_element(*self.input_when).send_keys(when_date)

    def click_color_black(self):
        self.driver.find_element(*self.input_color_black).click()

    def click_color_grey(self):
        self.driver.find_element(*self.input_color_grey).click()

    def input_text_in_comment(self, comment):
        self.driver.find_element(*self.input_comment).send_keys(comment)

    def click_on_order_middle_button(self):
        self.driver.find_element(*self.order_button_middle).click()

    def click_button_want_order(self):
        self.driver.find_element(*self.button_want_order).click()

    def input_text_in_modal(self):
        return self.driver.find_element(*self.div_ok_order).text

    def fill_person_info_by_button_up(self, person_name, person_surname, person_address, person_phone):
        # Шаг заполнение формы "Для кого самокат". Кнопка Заказать вверху
        self.click_on_order_up_button()
        self.input_name_to_order_form(person_name)
        self.input_surname_to_order_form(person_surname)
        self.input_address_to_order_form(person_address)
        self.input_phone_to_order_form(person_phone)
        self.input_metro_to_order_form()
        self.click_on_next_button()

    def fill_person_info_by_button_down(self, person_name, person_surname, person_address, person_phone):
        # Шаг заполнение формы "Для кого самокат". Кнопка Заказать внизу
        self.click_on_order_down_button()
        self.input_name_to_order_form(person_name)
        self.input_surname_to_order_form(person_surname)
        self.input_address_to_order_form(person_address)
        self.input_phone_to_order_form(person_phone)
        self.input_metro_to_order_form()
        self.click_on_next_button()

    def fill_info_in_about_rent_form(self, when_date, comment):
        # Шаг заполнение формы Об аренде
        self.input_div_order_time()
        self.click_color_black()
        self.input_text_in_comment(comment)
        self.input_when_to_order_form(when_date)
        self.click_on_order_middle_button()
        self.click_button_want_order()
