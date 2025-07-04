import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Тап на вопрос")
    def click_to_question(self, num):
        locator_question_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_question_formatted)

