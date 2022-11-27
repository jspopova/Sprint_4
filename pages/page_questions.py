from pages.BasePage import BasePage
from locators.base_page_locators import Locator

class Questions(BasePage):

    loc = Locator()
    div_cost = loc.div_cost
    div_more_then_1 = loc.div_more_then_1
    div_rent_time = loc.div_rent_time
    div_rent_today = loc.div_rent_today
    div_continue_and_return = loc.div_continue_and_return
    div_battery = loc.div_battery
    div_cancel = loc.div_cancel
    div_not_in_moscow = loc.div_not_in_moscow
    p_cost = loc.p_cost
    p_more_then_1 = loc.p_more_then_1
    p_rent_time = loc.p_rent_time
    p_rent_today = loc.p_rent_today
    p_continue_and_return = loc.p_continue_and_return
    p_battery = loc.p_battery
    p_cancel = loc.p_cancel
    p_not_in_moscow = loc.p_not_in_moscow
    logo_bike = loc.logo_bike

    def click_on_cost_question(self):
        self.driver.find_element(*self.div_cost).click()

    def click_on_more_then_1_question(self):
        self.driver.find_element(*self.div_more_then_1).click()

    def click_on_rent_today_question(self):
        self.driver.find_element(*self.div_rent_today).click()

    def click_on_rent_time_question(self):
        self.driver.find_element(*self.div_rent_time).click()

    def click_on_continue_and_return_question(self):
        self.driver.find_element(*self.div_continue_and_return).click()

    def click_on_battery_question(self):
        self.driver.find_element(*self.div_battery).click()

    def click_on_cancel_question(self):
        self.driver.find_element(*self.div_cancel).click()

    def click_on_not_in_moscow_question(self):
        self.driver.find_element(*self.div_not_in_moscow).click()

    def check_cost_text(self):
        return self.driver.find_element(*self.p_cost).text

    def check_more_then_1_text(self):
        return self.driver.find_element(*self.p_more_then_1).text

    def check_rent_time_text(self):
        return self.driver.find_element(*self.p_rent_time).text

    def check_rent_today_text(self):
        return self.driver.find_element(*self.p_rent_today).text

    def check_continue_and_return_text(self):
        return self.driver.find_element(*self.p_continue_and_return).text

    def check_battery_text(self):
        return self.driver.find_element(*self.p_battery).text

    def check_cancel_text(self):
        return self.driver.find_element(*self.p_cancel).text

    def check_not_in_moscow_text(self):
        return self.driver.find_element(*self.p_not_in_moscow).text

    def load_is_complete(self):
        if self.driver.execute_script("return document.readyState;") != "complete":
            return False
        else:
            return True

    def hide_a_bike(self):
        self.driver.execute_script("document.images[2].parentNode.style.visibility = 'hidden'")
        self.driver.execute_script("document.images[3].parentNode.style.visibility = 'hidden'")
