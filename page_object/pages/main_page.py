import allure

import data
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Тап на вопрос")
    def click_to_question(self, num):
        locator_question_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_question_formatted)

    @allure.step("Получаем текст ответа")
    def get_text_answer(self, num):
        locator_question_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_to_element(locator_question_formatted) == data.ANSWER_DATA[num]

