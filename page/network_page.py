from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NetworkPage(BaseAction):
    # 更多按钮
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 移动网络
    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    # 首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2G按钮
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3G按钮
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    # def __init__(self, driver):
    #     self.driver = driver

    def click_more(self):
        self.click(self.more_button)

    def click_network(self):
        self.click(self.network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)
