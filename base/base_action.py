from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]

        # 加入WebDriverWait的意义:如果第一次没有找到元素,再给点时间找一次
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]

        # 加入WebDriverWait的意义:如果第一次没有找到元素,再给点时间找一次
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))
