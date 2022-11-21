from selenium import webdriver
from selenium.webdriver.common.by import By

class Locator():
    order_button_up = [By.XPATH,'//div[@class=\'Header_Nav__AGCXC\']/button[contains(text(),\'Заказать\')]']
    order_button_down = [By.XPATH,'.//div[@class=\'Home_FinishButton__1_cWm\']/button[text()= \'Заказать\']']
    input_name = [By.XPATH,'.//input[@placeholder=\'* Имя\']']
    input_surname = [By.XPATH, './/input[@placeholder=\'* Фамилия\']']
    input_address = [By.XPATH, './/input[@placeholder=\'* Адрес: куда привезти заказ\']']
    input_metro = [By.XPATH, './/input[@placeholder=\'* Станция метро\']']
    select_metro = [By.XPATH, '//div[@class=\'select-search__select\']/ul[@class=\'select-search__options\']/li[@data-index=\'0\']']
    input_phone = [By.XPATH, './/input[@placeholder=\'* Телефон: на него позвонит курьер\']']
    button_next = [By.XPATH, '//button[contains(text(),\'Далее\')]']
    input_when = [By.XPATH, './/input[@placeholder=\'* Когда привезти самокат\']']
    div_order_time = [By.XPATH, '//div[contains(text(),\'* Срок аренды\')]']
    select_time = [By.XPATH, '//div[contains(text(),\'двое суток\')]']
    input_color_black = [By.XPATH, '//input[@id=\'black\']']
    input_color_grey= [By.XPATH, '//input[@id=\'grey\']']
    input_comment = [By.XPATH, './/input[@placeholder=\'Комментарий для курьера\']']
    button_want_order = [By.XPATH, '//button[contains(text(),\'Да\')]']
    div_ok_order = [By.XPATH, '//div[@class=\'Order_ModalHeader__3FDaJ\']']
    button_status = [By.XPATH, '//button[contains(text(),\'Посмотреть статус\')]']
    order_button_middle = [By.XPATH,'.//div[@class=\'Order_Buttons__1xGrp\']/button[text()=\'Заказать\']']
    div_cost =[By.XPATH,'// div[ @ id = \'accordion__heading-0\']']
    div_more_then_1 = [By.XPATH, '// div[ @ id = \'accordion__heading-1\']']
    div_rent_time = [By.XPATH, '// div[ @ id = \'accordion__heading-2\']']
    div_rent_today = [By.XPATH, '// div[ @ id = \'accordion__heading-3\']']
    div_continue_and_return = [By.XPATH, '// div[ @ id = \'accordion__heading-4\']']
    div_battery = [By.XPATH, '// div[ @ id = \'accordion__heading-5\']']
    div_cancel = [By.XPATH, '// div[ @ id = \'accordion__heading-6\']']
    div_not_in_Moscow = [By.XPATH, '// div[ @ id = \'accordion__heading-7\']']
    logo_yandex = [By.XPATH, './/img[@alt=\'Yandex\']']
    logo_bike = [By.XPATH, './/img[@alt=\'Scooter\']']
    p_cost =[By.XPATH,'//p[contains(text(),\'Сутки — 400 рублей. Оплата курьеру — наличными или\')]']
    p_more_then_1 = [By.XPATH, '//p[contains(text(),\'Пока что у нас так: один заказ — один самокат\')]']
    p_rent_time = [By.XPATH, '//p[contains(text(),\'Допустим, вы оформляете заказ на 8 мая.\')]']
    p_rent_today = [By.XPATH, '//p[contains(text(),\'Только начиная с завтрашнего дня. Но скоро станем \')]']
    p_continue_and_return = [By.XPATH, '//p[contains(text(),\'Пока что нет! Но если что-то срочное — всегда можн\')]']
    p_battery = [By.XPATH, '//p[contains(text(),\'Самокат приезжает к вам с полной зарядкой. Этого х\')]']
    p_cancel = [By.XPATH, '//p[contains(text(),\'Да, пока самокат не привезли. Штрафа не будет,\')]']
    p_not_in_Moscow = [By.XPATH, '//p[contains(text(),\'Да, обязательно. Всем самокатов! И Москве, и Моско\')]']


    def __init__(self):
        self

