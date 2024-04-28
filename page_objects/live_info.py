import time
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.log_util import logger
from utils.screenshot_util import ui_exception_record


class LiveInfo(BasePage):
    __LIVE_LINK = (By.XPATH, '//*[@id="pane-baseInfo"]/div/button/span')  # 点击直播链接
    __LIVE_MANAGE = (By.XPATH, "//span[@class='el-breadcrumb__inner is-link' and text()='直播管理']")  # 点击直播管理
    __CLICK_LINK_TOAST = (By.XPATH, "//p[contains(text(),'直播未上架，无法分享！')]")  # 点击直播链接toast

    @ui_exception_record
    def click_live_manage(self):
        logger.info("查看直播页：点击直播管理")
        with allure.step("点击直播管理"):
            self.do_find(self.__LIVE_MANAGE).click()
        # ==>返回直播列表页
        from page_objects.live_list_page import LiveList
        return LiveList(self.driver)

    @ui_exception_record
    def click_live_link(self):
        logger.info("查看直播页：点击直播链接")
        with allure.step("点击直播链接"):
            self.do_find(self.__LIVE_LINK).click()
        return LiveInfo(self.driver)

    @ui_exception_record
    def get_link_toast(self):
        logger.info("查看直播页：获取点击直播链接toast")
        with allure.step("获取点击直播链接提示"):
            toast = self.wait_element_until(self.__CLICK_LINK_TOAST)
            msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        return msg
