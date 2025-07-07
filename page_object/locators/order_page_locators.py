from selenium.webdriver.common.by import By

class OrderPageLocators:
    BUTTON_ORDER = By.XPATH, ".//*[@class = 'Header_Nav__AGCXC']/button[@class = 'Button_Button__ra12g']"
    BUTTON_ORDER_IN_NAVBAR = By.XPATH, ".//*[@class = 'Button_Button__ra12g'][text()='Заказать']"
    INPUT_FIRST_NAME = By.XPATH, ".//*[@placeholder='* Имя']"
    INPUT_LAST_NAME = By.XPATH, ".//*[@placeholder='* Фамилия']"
    INPUT_ADDRESS = By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"
    INPUT_METRO = By.XPATH, ".//*[@placeholder='* Станция метро']"
    POINT_METRO_STATION_FIRST = By.XPATH, ".//*[@class = 'select-search__row'][@data-index='1']"
    POINT_METRO_STATION_SECOND = By.XPATH, ".//*[@class = 'select-search__row'][@data-index='2']"
    INPUT_NUMBER_PHONE = By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_CONTINUE = By.XPATH, ".//*[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    CALENDAR_DELIVERY = By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"
    DATE_IN_CALENDAR_DELIVERY = By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--011']"
    DROPDOWN_RENTAL_PERIOD = By.XPATH, ".//*[text()='* Срок аренды']"
    POINT_IN_DROPDOWN_RENTAL_PERIOD = By.XPATH, ".//*[text()='трое суток']"
    CHECKBOX_BLACK_SCOOTER = By.XPATH, ".//*[@id='black']"
    CHECKBOX_GRAY_SCOOTER = By.XPATH, ".//*[@id='gray']"
    INPUT_COMMENT_FOR_COURIER = By.XPATH, ".//*[@placeholder='Комментарий для курьера']"
    BUTTON_CREATE_ORDER = By.XPATH, ".//button[text()='Заказать'][@class='Button_Button__ra12g Button_Middle__1CSJM']"
    BUTTON_APPROVE_CREATE_ORDER = By.XPATH, ".//button[text()='Да'][@class='Button_Button__ra12g Button_Middle__1CSJM']"
    HEADER_CREATED_ORDER = By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ'][text()='Заказ оформлен']"






