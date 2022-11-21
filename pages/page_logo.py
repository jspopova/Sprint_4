import locators.base_page_locators as l

class Go_from_logo():
    loc = l.Locator()
    logo_yandex = loc.logo_yandex
    logo_bike = loc.logo_bike
    order_button_up = loc.order_button_up

    def __init__(self, driver):
        self.driver = driver

    def yandex_click(self):
        self.driver.find_element(*self.logo_yandex).click()

    def bike_click(self):
        self.driver.find_element(*self.order_button_up).click()
        self.driver.find_element(*self.logo_bike).click()