"""父类"""
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testcases.conftest import web_env
from utils.log_util import logger


class BasePage:
    _BASE_URL = ""  # 每个页面都有一个url

    def __init__(self, base_driver=None):
        self.browser = web_env.get("browser")
        """
        定义一个构造方法
        :param base_driver: 注意：需要区分是否要传入现有的base_driver
        """
        if base_driver:
            self.driver = base_driver
        else:
            # self.driver = webdriver.Chrome()
            # # self.driver = webdriver.Firefox()
            # # 刷新浏览器
            # self.driver.refresh()
            # # 最大浏览器窗口操作
            # self.driver.maximize_window()
            # self.driver.implicitly_wait(20)
            print(f"获取到的浏览器信息为：{self.browser}")
            if self.browser == "firefox":
                self.driver = webdriver.Firefox()
                # 刷新浏览器
                self.driver.refresh()
                # 最大浏览器窗口操作
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)
            else:
                self.driver = webdriver.Chrome()
                # 刷新浏览器
                self.driver.refresh()
                # 最大浏览器窗口操作
                self.driver.maximize_window()
                self.driver.implicitly_wait(20)

        # 如果浏览器当前地址不是以http开头的，现在没有在某个页面中，那么就导航到基地址中
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)
            self.driver.refresh()

    def do_find(self, by, locator=None):
        """
        获取单个元素
        :param by: 定位策略
        :param locator: 定位表达式
        :return:
        """
        if locator:
            return self.driver.find_element(by, locator)  # 如果传递两个参数，就传到find_element中
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        """获取多个元素"""
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        """输入"""
        ele = self.do_find(by, locator)
        ele.send_keys(value)

    def do_quit(self):
        """关闭浏览器"""
        self.driver.quit()

    def wait_element_until(self, locator: tuple):
        """显示等待，冒泡消息文本"""
        # return WebDriverWait(self.driver, 20) \
        #     .until(EC.presence_of_element_located(locator))
        return WebDriverWait(self.driver, 20) \
            .until(EC.element_to_be_clickable(locator))

    def do_clear_send_keys(self, value, by, locator=None):
        """清空并输入"""
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def do_clear(self, by, locator=None):
        """清空输入框"""
        ele = self.do_find(by, locator)
        ele.clear()
