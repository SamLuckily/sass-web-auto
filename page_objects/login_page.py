import logging
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.screenshot_util import ui_exception_record


class LoginPage(BasePage):
    """登录页面：用户登录"""
    # _BASE_URL = "https://dt.boweiedu.com/"
    _BASE_URL = "http://192.168.0.210/"

    __NAME = (By.XPATH, "//input[@placeholder='手机号码/帐号']")  # 输入手机号码/账号
    __PASSWORD = (By.XPATH, "//input[@placeholder='密码']")  # 输入密码
    __CLICK = (By.XPATH, '//*[@class="banner"]/div/div/div/form[1]/div[3]/div/div/button/span')  # 点击登录

    @ui_exception_record
    def login(self):
        logging.info("登录页面：用户登录")
        logging.info("访问登录页")
        # 输入“用户名
        self.do_send_keys("15830344885", self.__NAME)
        # 输入”密码“
        self.do_send_keys("admin123", self.__PASSWORD)
        # 点击”登录“按钮
        self.do_find(self.__CLICK).click()
        # ==》直播列表页
        # 注意：要用局部导入，导入到方法里面而不是导入到类中(locally)防止链式调用时产生循环依赖
        from page_objects.live_list_page import LiveList
        # 调用self.driver 只打开一个浏览器
        return LiveList(self.driver)
