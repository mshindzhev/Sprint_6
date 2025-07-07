import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait

import data
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.order_page import OrderPage


@allure.title('Тесты на проверку раздела "Вопросы о важном"')
class TestOrderPage:

    @pytest.mark.parametrize(
        'button, order_data',
        [
            (OrderPageLocators.BUTTON_ORDER_IN_NAVBAR, data.ORDER_DATA_1),
            (OrderPageLocators.BUTTON_ORDER, data.ORDER_DATA_2)
        ]
    )
    def test_create_order(self, button, order_data, driver):
        with allure.step('Открыть главную страницу'):
            order_page = OrderPage(driver)
            order_page.go_to_url(data.URL_MAIN)

        with allure.step('Тап на кнопку Заказать'):
            order_page.find_and_click_button_order(button)

        with allure.step('Заполнить данные клиента'):
            order_page.set_order(order_data)

        with allure.step('Проверить, что заказ создан'):
            assert order_page.check_order_created()

    def test_redirect_in_logo_scooter_click(self, driver):
        with allure.step('Открыть страницу заказа'):
            order_page = OrderPage(driver)
            order_page.go_to_url(data.URL_ORDER)
        with allure.step('Проверить переход на главную'):
            order_page.redirect_logo_scooter()
            assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_redirect_in_logo_yandex_click(self, driver):
        with allure.step('Открыть страницу заказа'):
            order_page = OrderPage(driver)
            order_page.go_to_url(data.URL_ORDER)
        with allure.step('Проверить переход на Дзен'):
            order_page.redirect_logo_yandex()
            driver.switch_to.window(driver.window_handles[-1])
            WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) == 2)
            order_page.find_logo_dzen()
            assert 'dzen.ru' in driver.current_url.lower()
