from selenium.webdriver.common.by import By

class MainPageLocators:

    HEADER_IMPORTANT_QUESTIONS = By.XPATH, ".//div[text() = 'Вопросы о важном']"
    QUESTION_LOCATOR = By.XPATH, ".//div[@id = 'accordion__heading-{}']"
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, ".//div[@id = 'accordion__heading-7']"
    ANSWER_LOCATOR = By.XPATH, ".//*[@id = 'accordion__panel-{}']/p"
    ANSWER_LOCATOR_TO_SCROLL = By.XPATH, ".//*[@id = 'accordion__panel-7']/p"