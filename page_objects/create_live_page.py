import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from page_objects.live_list_page import LiveList
from utils.log_util import logger
from utils.screenshot_util import ui_exception_record


class CreateLive(BasePage):
    """新增直播页：创建直播"""
    __LIVE_NAME = (By.CSS_SELECTOR, "[placeholder='输入直播名称']")  # 输入直播名称
    __LIVE_INTRO = (By.CSS_SELECTOR, "[placeholder='输入直播介绍']")  # 输入直播介绍
    __CLICK_CHOOSE = (By.CSS_SELECTOR, "form>div:nth-child(6)>div div div.el-input__wrapper>input")  # 点击选择老师
    __CHOOSE_TEACHER = (By.XPATH, "//span[text()='常同学']")  # 选择老师  //span[text()='常同学']
    __CLICK_ROOM = (By.XPATH, "//input[@placeholder='请选择教室']")  # 点击选择教室
    __CHOOSE_ROOM = (By.XPATH, "//span[text()='ITC015G2']")  # 选择教室E02-ProITC015G2  5G车教室
    __CLICK_SAVE = (By.CSS_SELECTOR, ".step-btn-group>button:nth-child(2)")  # 点击保存
    __TOAST_ASSERT = (By.XPATH, "//p[text()='直播信息保存成功']")  # toast信息
    __LIVE_MANAGE = (By.XPATH, "//span[@class='el-breadcrumb__inner is-link' and text()='直播管理']")  # 点击直播管理

    @ui_exception_record
    def create_live(self, live_name, live_intro):
        logger.info("新增直播页：创建直播")
        # 输入”直播名称“等信息
        # 点击”确定“按钮
        self.do_send_keys(live_name, self.__LIVE_NAME)
        logger.info("输入直播名称")
        self.do_send_keys(live_intro, self.__LIVE_INTRO)
        logger.info("输入直播介绍")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("向下滑动屏幕")
        self.do_find(self.__CLICK_CHOOSE).click()
        logger.info("点击选择老师")
        time.sleep(1)
        self.do_find(self.__CHOOSE_TEACHER).click()
        logger.info("选择老师")
        self.do_find(self.__CLICK_ROOM).click()
        logger.info("点击请选择教室")
        time.sleep(1)
        # 选择E02-Pro
        self.do_find(self.__CHOOSE_ROOM).click()
        logger.info("选择教室")
        self.do_find(self.__CLICK_SAVE).click()
        logger.info("点击保存")
        time.sleep(1)
        # ==>直播列表页
        return CreateLive(self.driver)

    def get_operate_result(self):
        logger.info("创建直播页：获取操作结果")
        logger.info("获取冒泡消息文本")
        toast = self.wait_element_until(self.__TOAST_ASSERT)
        msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        # ==>返回消息文本
        return msg

    def click_live_manage(self):
        logger.info("点击直播管理,跳转到直播列表页面")
        self.do_find(self.__LIVE_MANAGE).click()
        return LiveList(self.driver)
