import locators.base_page_locators as l
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Questions():
    loc = l.Locator()
    div_cost = loc.div_cost
    div_more_then_1 = loc.div_more_then_1
    div_rent_time = loc.div_rent_time
    div_rent_today = loc.div_rent_today
    div_continue_and_return = loc.div_continue_and_return
    div_battery = loc.div_battery
    div_cancel = loc.div_cancel
    div_not_in_Moscow = loc.div_not_in_Moscow
    p_cost = loc.p_cost
    p_more_then_1 = loc.p_more_then_1
    p_rent_time = loc.p_rent_time
    p_rent_today = loc.p_rent_today
    p_continue_and_return = loc.p_continue_and_return
    p_battery = loc.p_battery
    p_cancel = loc.p_cancel
    p_not_in_Moscow = loc.p_not_in_Moscow


    def __init__(self, driver):
        self.driver = driver

    def cost_click(self):

        self.driver.find_element(*self.div_cost).click()

    def more_1_click(self):

        self.driver.find_element(*self.div_more_then_1).click()

    def rent_today_click(self):
        self.driver.find_element(*self.div_rent_today).click()

    def rent_time_click(self):
        self.driver.find_element(*self.div_rent_time).click()

    def continue_and_return_click(self):
        self.driver.find_element(*self.div_continue_and_return).click()

    def battery_click(self):
        self.driver.find_element(*self.div_battery).click()

    def cancel_click(self):
        self.driver.find_element(*self.div_cancel).click()

    def not_in_Moscow_click(self):
        self.driver.find_element(*self.div_not_in_Moscow).click()

    def cost_text(self):
        return self.driver.find_element(*self.p_cost).text

    def more_then_1_text(self):
        return self.driver.find_element(*self.p_more_then_1).text

    def rent_time_text(self):
        return self.driver.find_element(*self.p_rent_time).text

    def rent_today_text(self):
        return self.driver.find_element(*self.p_rent_today).text

    def continue_and_return_text (self):
        return self.driver.find_element(*self.p_continue_and_return).text

    def battery_text (self):
        return self.driver.find_element(*self.p_battery).text

    def cancel_text (self):
        return self.driver.find_element(*self.p_cancel).text

    def not_in_Moscow_text (self):
        return self.driver.find_element(*self.p_not_in_Moscow).text
