import locators.base_page_locators as l
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class Order:
    loc = l.Locator()

    order_button_up = loc.order_button_up
    input_name = loc.input_name
    input_surname = loc.input_surname
    input_address = loc.input_address
    input_metro = loc.input_metro
    select_metro = loc.select_metro
    div_order_time = loc.div_order_time
    input_phone = loc.input_phone
    input_when = loc.input_when
    div_order_time = loc.div_order_time
    select_time = loc.select_time
    input_color_black = loc.input_color_black
    input_comment = loc.input_comment
    button_want_order = loc.button_want_order
    order_button_down = loc.order_button_down
    button_next = loc.button_next
    input_color_grey = loc.input_color_grey
    order_button_middle = loc.order_button_middle
    button_want_order = loc.button_want_order
    div_ok_order = loc.div_ok_order


    def __init__(self, driver):
        self.driver = driver

    def click_on_order_up_button(self):
        self.driver.find_element(*self.order_button_up).click()

    def click_on_order_down_button(self):
        self.driver.find_element(*self.order_button_down).click()

    def inp_name_to_order_form(self, person_name):
        self.driver.find_element(*self.input_name).send_keys(person_name)

    def inp_surname_to_order_form(self, person_surname):
        self.driver.find_element(*self.input_surname).send_keys(person_surname)

    def inp_address_to_order_form(self, person_address):
        self.driver.find_element(*self.input_address).send_keys(person_address)

    def inp_phone_to_order_form(self, person_phone):
        self.driver.find_element(*self.input_phone).send_keys(person_phone)

    def inp_metro_to_order_form(self):
        self.driver.find_element(*self.input_metro).click()
        WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.select_metro).click()



    def inp_div_order_time(self):
        self.driver.find_element(*self.div_order_time).click()
        WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.select_time).click()
    def click_on_next_button(self):
        self.driver.find_element(*self.button_next).click()

    def inp_when_to_order_form(self, when_date):
        self.driver.find_element(*self.input_when).click()
        self.driver.find_element(*self.input_when).send_keys(when_date)

    def inp_color_black(self):
        self.driver.find_element(*self.input_color_black).click()

    def inp_color_grey(self):
        self.driver.find_element(*self.input_color_grey).click()

    def inp_comment(self, comment):
        self.driver.find_element(*self.input_comment).send_keys(comment)

    def click_on_order_middle_button(self):
        self.driver.find_element(*self.order_button_middle).click()

    def click_button_want_order(self):
        self.driver.find_element(*self.button_want_order).click()

    def text_in_modal(self):
        return self.driver.find_element(*self.div_ok_order).text

    def person_information_button_up(self,person_name,person_surname,person_address,person_phone): #Шаг заполнение формы "Для кого самокат". Кнопка Заказать вверху
        self.click_on_order_up_button()
        self.inp_name_to_order_form(person_name)
        self.inp_surname_to_order_form(person_surname)
        self.inp_address_to_order_form(person_address)
        self.inp_phone_to_order_form(person_phone)
        self.inp_metro_to_order_form()
        self.click_on_next_button()

    def person_information_button_down(self,person_name,person_surname,person_address,person_phone): #Шаг заполнение формы "Для кого самокат". Кнопка Заказать внизу
        self.click_on_order_down_button()
        self.inp_name_to_order_form(person_name)
        self.inp_surname_to_order_form(person_surname)
        self.inp_address_to_order_form(person_address)
        self.inp_phone_to_order_form(person_phone)
        self.inp_metro_to_order_form()
        self.click_on_next_button()

    def about_rent(self, when_date, comment): #Шаг заполнение формы Об аренде
        self.inp_div_order_time()
        self.inp_color_black()
        self.inp_comment(comment)
        self.inp_when_to_order_form(when_date)
        self.click_on_order_middle_button()
        self.click_button_want_order()

