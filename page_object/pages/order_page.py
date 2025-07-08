import allure

from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Поиск и тап на элемент")
    def find_and_click_button_order(self, button):
        self.find_element_with_wait(button)
        self.click_to_element(button)

    @allure.step("Запролнение данных для заказа")
    def set_order(self, data):
        self.add_text_to_element(OrderPageLocators.INPUT_FIRST_NAME, data['name'])
        self.add_text_to_element(OrderPageLocators.INPUT_LAST_NAME, data['last_name'])
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS, data['address'])
        self.add_text_to_element(OrderPageLocators.INPUT_NUMBER_PHONE, data['phone_number'])
        self.click_to_element(OrderPageLocators.INPUT_METRO)
        self.click_to_element(OrderPageLocators.POINT_METRO_STATION_FIRST)
        self.click_to_element(OrderPageLocators.INPUT_LAST_NAME)
        self.click_to_element(OrderPageLocators.BUTTON_CONTINUE)
        self.click_to_element(OrderPageLocators.CALENDAR_DELIVERY)
        self.click_to_element(OrderPageLocators.DATE_IN_CALENDAR_DELIVERY)
        self.click_to_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.POINT_IN_DROPDOWN_RENTAL_PERIOD)
        self.add_text_to_element(OrderPageLocators.INPUT_COMMENT_FOR_COURIER, data['text_comment'])
        self.click_to_element(OrderPageLocators.BUTTON_CREATE_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_APPROVE_CREATE_ORDER)

    @allure.step("Проверка созданного заказа")
    def check_order_created(self):
        return self.find_element_with_wait(OrderPageLocators.HEADER_CREATED_ORDER)

    @allure.step("Редирект по логотипу Самоката")
    def redirect_logo_scooter(self):
        self.click_to_element(OrderPageLocators.LOGO_SCOOTER)

    @allure.step("Поиск логотипа Дзен")
    def find_logo_dzen(self):
        self.find_element_with_wait(OrderPageLocators.LOCATOR_DZEN)

    @allure.step("Редирект по логотипу Яндекса")
    def redirect_logo_yandex(self):
        self.click_to_element(OrderPageLocators.LOGO_YANDEX)




