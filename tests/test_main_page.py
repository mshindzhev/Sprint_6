import pytest
import selenium
import allure

import data

@allure.title('Тесты на проверку раздела "Вопросы о важном"')
class TestDropDownList:

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
    def test_drop_down_list_questions_click(self, main_page, num):
        with allure.step('Открыть главную страницу'):
            main_page.go_to_url(data.URL_MAIN)

        with allure.step('Доскроллить до раздела "Вопросы о важном"'):
            main_page.click_to_question()