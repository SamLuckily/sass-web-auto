import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.log_util import logger
from utils.screenshot_util import ui_exception_record


class LiveList(BasePage):
    """直播列表页：点击新增直播"""
    __VIEW = (By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td>div>button:nth-child(1)>span")  # 查看按键
    __CLICK_ADD = (By.CSS_SELECTOR, 'span.text-base')  # 点击新增
    __DEL = (By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td>div>button:nth-child(2)>span")  # 点击删除按钮
    __ALERT = (By.CSS_SELECTOR, 'footer>span>button:nth-child(2)>span')  # 弹框点击确认
    __DEL_SUCCESS = (By.XPATH, "//p[text()='直播删除成功']")
    __HOVER_OVER = (By.CSS_SELECTOR, "#app .vxe-table--fixed-wrapper tbody>tr:nth-child(1)>td>div div>span")  # 定位需要悬浮元素
    __OPTIONS = (By.CSS_SELECTOR, "body>div:nth-child(2)>div:nth-child(3) div>ul>li:nth-child(2)")  # 定位鼠标悬浮后上架字样
    __Listing = (By.XPATH, "//*[text()='上架成功']")
    __REMOVE_SHELVES = (By.XPATH, "/html/body/div[2]/div[12]/div/div[1]/div/ul/li[2]")  # 定位下架
    __REMOVED = (By.XPATH, "//*[text()='下架成功']")

    @ui_exception_record
    def click_add(self):
        logger.info("直播列表页：点击新增直播")
        with allure.step("点击新增直播按钮"):
            self.do_find(self.__CLICK_ADD).click()
        # ==>新增直播页
        from page_objects.create_live_page import CreateLive
        return CreateLive(self.driver)

    @ui_exception_record
    def view_live(self):
        logger.info("直播列表页：点击查看按钮")
        with allure.step("点击查看按钮"):
            self.do_find(self.__VIEW).click()
        # ==>查看直播页
        from page_objects.live_info import LiveInfo
        return LiveInfo(self.driver)

    @ui_exception_record
    def delete_live(self):
        logger.info("点击删除按钮")
        with allure.step("点击删除按钮"):
            self.do_find(self.__DEL).click()
        time.sleep(1)
        logger.info("弹框点击确定")
        with allure.step("弹框点击确定"):
            self.do_find(self.__ALERT).click()
        # ==》跳转到当前页面
        return LiveList(self.driver)

    @ui_exception_record
    def get_del_result(self):
        logger.info("直播列表页：获取删除操作结果")
        logger.info("获取冒泡消息文本")
        time.sleep(2)
        with allure.step("显示等待获取冒泡消息文本"):
            toast = self.wait_element_until(self.__DEL_SUCCESS)
            msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        return msg

    @ui_exception_record
    def listing(self):
        logger.info("直播列表页：定位需要悬浮的元素")
        with allure.step("定位需要悬浮的元素"):
            hover_over = self.do_find(self.__HOVER_OVER)
        logger.info("创建一个ActionChains对象，将鼠标移动到元素 `hover_over` 上，然后执行操作")
        with allure.step("创建一个ActionChains对象，将鼠标移动到元素 `hover_over` 上，然后执行操作"):
            ActionChains(self.driver).move_to_element(hover_over).perform()
        logger.info("定位弹框显示的上架字样")
        with allure.step("定位弹框显示的上架字样"):
            options = self.do_find(self.__OPTIONS)
        logger.info("创建一个ActionChains对象，对元素 `上架` 执行点击操作。")
        with allure.step("创建一个ActionChains对象，对元素 `上架` 执行点击操作。"):
            ActionChains(self.driver).click(options).perform()
        logger.info("在确认上架弹框处点击确定")
        with allure.step("在确认上架弹框处点击确定"):
            self.do_find(self.__ALERT).click()
        return LiveList(self.driver)

    def get_listing_toast(self):
        time.sleep(1)
        logger.info("直播列表页：获取上架成功toast")
        with allure.step("直播列表页：获取上架成功toast"):
            toast = self.wait_element_until(self.__Listing)
            msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        return msg

    @ui_exception_record
    def remove_from_shelves(self):
        logger.info("直播列表页：定位需要悬浮的元素")
        with allure.step("定位需要悬浮的元素"):
            hover_over = self.do_find(self.__HOVER_OVER)
        logger.info("创建一个ActionChains对象，将鼠标移动到元素 `hover_over` 上，然后执行操作")
        with allure.step("创建一个ActionChains对象，将鼠标移动到元素 `hover_over` 上，然后执行操作"):
            ActionChains(self.driver).move_to_element(hover_over).perform()
        logger.info("定位弹框显示的下架字样")
        with allure.step("定位弹框显示的下架字样"):
            options = self.do_find(self.__REMOVE_SHELVES)
        logger.info("创建一个ActionChains对象，对元素 `下架` 执行点击操作。")
        with allure.step("创建一个ActionChains对象，对元素 `下架` 执行点击操作。"):
            ActionChains(self.driver).click(options).perform()
        logger.info("在确认下架弹框处点击确定")
        with allure.step("在确认下架弹框处点击确定"):
            self.do_find(self.__ALERT).click()
        return LiveList(self.driver)

    def get_remove_shelves_toast(self):
        time.sleep(1)
        logger.info("直播列表页：获取下架成功toast")
        with allure.step("直播列表页：获取下架成功toast"):
            toast = self.wait_element_until(self.__REMOVED)
            msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        return msg
