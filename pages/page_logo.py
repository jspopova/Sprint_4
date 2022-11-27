from pages.BasePage import BasePage
from locators.base_page_locators import Locator


class GoFromLogo(BasePage):
    loc = Locator()
    logo_yandex = loc.logo_yandex
    logo_bike = loc.logo_bike
    order_button_up = loc.order_button_up

    def click_on_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex).click()

    def click_on_bike_logo(self):
        self.driver.find_element(*self.order_button_up).click()
        self.driver.find_element(*self.logo_bike).click()
