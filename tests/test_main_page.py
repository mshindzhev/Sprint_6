import pytest
import allure

import data
from page_object.pages.main_page import MainPage


@allure.title('Тесты на проверку раздела "Вопросы о важном"')
class TestOrderPage:

    @pytest.mark.parametrize(
        'num',
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    )
    def test_drop_down_list_questions_and_answers(self, driver, num):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)
            main_page.go_to_url(data.URL_MAIN)

        with allure.step('Открыть ответ на вопрос в разделе "Вопросы о важном"'):
            main_page.click_to_question(num)
            assert main_page.get_text_answer(num)