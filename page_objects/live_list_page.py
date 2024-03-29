import logging
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.log_util import logger
from utils.screenshot_util import ui_exception_record


class LiveList(BasePage):
    """直播列表页：点击新增直播"""
    __CLICK_ADD = (By.CSS_SELECTOR, 'span.text-base')  # 点击新增
    __DEL = (By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td>div>button:nth-child(2)>span")  # 点击删除按钮
    __ALERT = (By.CSS_SELECTOR, 'footer>span>button:nth-child(2)>span')  # 弹框点击确认
    __DEL_SUCCESS = (By.XPATH, "//p[text()='直播删除成功']")

    @ui_exception_record
    def click_add(self):
        logging.info("直播列表页：点击新增直播")
        # 点击”新增直播“按钮
        self.do_find(self.__CLICK_ADD).click()
        # ==>新增直播页
        from page_objects.create_live_page import CreateLive
        return CreateLive(self.driver)

    @ui_exception_record
    def delete_live(self):
        """删除自己创建的直播"""
        self.do_find(self.__DEL).click()
        logger.info("点击删除按钮")
        time.sleep(1)
        logger.info("弹框点击确定")
        self.do_find(self.__ALERT).click()
        # ==》跳转到当前页面
        return LiveList(self.driver)

    def get_del_result(self):
        logging.info("直播列表页：获取操作结果")
        logger.info("获取冒泡消息文本")
        time.sleep(2)
        toast = self.wait_element_until(self.__DEL_SUCCESS)
        msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        return msg
