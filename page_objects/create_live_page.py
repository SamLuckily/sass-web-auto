import time
import allure
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
    __CLICK_SAVE_listing = (By.XPATH, "//span[text()=' 保存并上架 ']")  # 点击保存并上架
    __CLICK_SAVE_LISTING = (By.XPATH, "//p[text()='直播信息保存成功']")
    __EDIT_TOAST = (By.XPATH, "//p[text()='直播信息编辑成功']")  # 直播信息编辑成功
    __UPLOAD_IMG = (By.CSS_SELECTOR, ".el-form-item__content>div:nth-child(3) ul svg")  # 直播介绍点击上传图片按键
    __INPUT_INTRO = (By.CSS_SELECTOR, ".el-form-item__content>div:nth-child(3) input")  # 上传直播介绍图input
    __UPLOAD_COVER_IMG = (By.CSS_SELECTOR, ".el-form-item__content>div:nth-child(2) ul svg")  # 直播封面上传图片按键
    __INPUT_COVER = (By.CSS_SELECTOR, ".el-form-item__content>div:nth-child(2) input")  # 上传直播封面图input
    __SET_PASSWORD = (By.XPATH, "//input[@placeholder='密码']")  # 密码
    __START_TIME = (By.XPATH, "//input[@placeholder='设置开始时间']")  # 设置开始时间
    __END_TIME = (By.XPATH, "//input[@placeholder='设置结束时间']")  # 设置结束时间
    __INFO_ERROR_TIME = (By.XPATH, "//*[text()='结束时间不能早于开始时间']")  # 结束时间不能早于开始时间

    @ui_exception_record
    def create_live(self, live_name, live_intro):
        logger.info("创建直播页：创建直播点击保存")
        logger.info("输入直播名称")
        with allure.step("输入直播名称"):
            self.do_send_keys(live_name, self.__LIVE_NAME)
        logger.info("输入直播介绍")
        with allure.step("输入直播介绍"):
            self.do_send_keys(live_intro, self.__LIVE_INTRO)
        logger.info("向下滑动屏幕")
        with allure.step("向下滑动到屏幕底部"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("点击选择老师")
        with allure.step("点击选择老师"):
            self.do_find(self.__CLICK_CHOOSE).click()
        time.sleep(1)
        logger.info("选择老师")
        with allure.step("选择老师"):
            self.do_find(self.__CHOOSE_TEACHER).click()
        logger.info("点击请选择教室")
        with allure.step("点击请选择教室"):
            self.do_find(self.__CLICK_ROOM).click()
        time.sleep(1)
        # 选择E02-Pro
        logger.info("选择教室")
        with allure.step("选择教室"):
            self.do_find(self.__CHOOSE_ROOM).click()
        logger.info("点击保存")
        with allure.step("点击保存"):
            self.do_find(self.__CLICK_SAVE).click()
        time.sleep(1)
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def get_operate_result(self):
        logger.info("创建直播页：获取操作结果")
        logger.info("获取冒泡消息文本")
        with allure.step("获取冒泡消息文本"):
            toast = self.wait_element_until(self.__TOAST_ASSERT)
        msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        # ==>返回消息文本
        return msg

    @ui_exception_record
    def click_live_manage(self):
        logger.info("创建直播页：点击直播管理,跳转到直播列表页面")
        with allure.step("点击直播管理,跳转到直播列表页面"):
            self.do_find(self.__LIVE_MANAGE).click()
        return LiveList(self.driver)

    @ui_exception_record
    def create_live_listing(self, live_name, live_intro):
        logger.info("创建直播页：创建直播完成后点击保存并上架")
        logger.info("输入直播名称")
        with allure.step("输入直播名称"):
            self.do_send_keys(live_name, self.__LIVE_NAME)
        logger.info("输入直播介绍")
        with allure.step("输入直播介绍"):
            self.do_send_keys(live_intro, self.__LIVE_INTRO)
        logger.info("向下滑动屏幕")
        with allure.step("向下滑动屏幕"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("点击选择老师")
        with allure.step("点击选择老师"):
            self.do_find(self.__CLICK_CHOOSE).click()
        time.sleep(1)
        logger.info("选择老师")
        with allure.step("选择老师"):
            self.do_find(self.__CHOOSE_TEACHER).click()
        logger.info("点击请选择教室")
        with allure.step("点击请选择教室"):
            self.do_find(self.__CLICK_ROOM).click()
        time.sleep(1)
        # 选择E02-Pro
        logger.info("选择教室")
        with allure.step("选择教室"):
            self.do_find(self.__CHOOSE_ROOM).click()
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        time.sleep(1)
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def get_save_listing_result(self):
        logger.info("创建直播页：获取保存并上架后结果")
        logger.info("获取冒泡消息文本")
        with allure.step("获取冒泡消息文本"):
            toast = self.wait_element_until(self.__CLICK_SAVE_LISTING)
        msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        # ==>返回消息文本
        return msg

    @ui_exception_record
    def edit_live_name(self, live_name):
        logger.info("创建直播页：清空输入框并编辑直播名称")
        logger.info("清空输入框并编辑直播名称")
        with allure.step("清空输入框并编辑直播名称"):
            self.do_send_keys(live_name, self.__LIVE_NAME)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        time.sleep(1)
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def get_edit_result(self):
        logger.info("创建直播页：获取编辑后结果")
        logger.info("获取冒泡消息文本")
        with allure.step("获取冒泡消息文本"):
            toast = self.wait_element_until(self.__EDIT_TOAST)
        msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        # ==>返回消息文本
        return msg

    @ui_exception_record
    def edit_live_introduce(self, live_intro):
        logger.info("创建直播页：清空输入框并编辑直播介绍")
        logger.info("清空输入框并编辑直播介绍")
        with allure.step("清空输入框并编辑直播介绍"):
            self.do_send_keys(live_intro, self.__LIVE_INTRO)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        time.sleep(1)
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def edit_introduce_image(self):
        logger.info("创建直播页：上传直播介绍图片")
        logger.info("点击上传图片按键")
        with allure.step("点击上传图片按键"):
            self.do_find(self.__UPLOAD_IMG).click()
        logger.info("上传图片的input标签位置")
        with allure.step("上传图片的input标签位置"):
            ele_add = self.do_find(self.__INPUT_INTRO)
        logger.info("使用send_keys传文件路径")
        with allure.step("使用send_keys传文件路径"):
            # send_keys使用绝对路径
            ele_add.send_keys(r"E:\python_project\own_project\web_ui\sass_webauto\file\shenzhen.jpg")
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def edit_cover_image(self):
        logger.info("创建直播页：上传直播封面图片")
        logger.info("向下滑动200像素")
        with allure.step("向下滑动200像素"):
            self.driver.execute_script("window.scrollTo(0, 200);")
        logger.info("点击上传图片按键")
        with allure.step("点击上传图片按键"):
            self.do_find(self.__UPLOAD_COVER_IMG).click()
        logger.info("上传图片的input标签位置")
        with allure.step("上传图片的input标签位置"):
            ele_add = self.do_find(self.__INPUT_COVER)
        logger.info("使用send_keys传文件路径")
        with allure.step("使用send_keys传文件路径"):
            # send_keys使用绝对路径
            ele_add.send_keys(r"E:\python_project\own_project\web_ui\sass_webauto\file\tiantan.jpg")
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    def edit_set_up_password(self, password):
        logger.info("创建直播页：设置密码")
        logger.info("向下滑动400像素")
        with allure.step("向下滑动400像素"):
            self.driver.execute_script("window.scrollTo(0, 400);")
        logger.info("输入密码")
        with allure.step("输入密码"):
            self.do_send_keys(password, self.__SET_PASSWORD)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def create_live_password(self, live_name, live_intro, live_password):
        logger.info("创建直播页：创建直播点击保存")
        logger.info("输入直播名称")
        with allure.step("输入直播名称"):
            self.do_send_keys(live_name, self.__LIVE_NAME)
        logger.info("输入直播介绍")
        with allure.step("输入直播介绍"):
            self.do_send_keys(live_intro, self.__LIVE_INTRO)
        logger.info("向下滑动屏幕")
        with allure.step("向下滑动到屏幕底部"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("设置密码")
        with allure.step("设置密码"):
            self.do_send_keys(live_password, self.__SET_PASSWORD)
        logger.info("点击选择老师")
        with allure.step("点击选择老师"):
            self.do_find(self.__CLICK_CHOOSE).click()
        time.sleep(1)
        logger.info("选择老师")
        with allure.step("选择老师"):
            self.do_find(self.__CHOOSE_TEACHER).click()
        logger.info("点击请选择教室")
        with allure.step("点击请选择教室"):
            self.do_find(self.__CLICK_ROOM).click()
        time.sleep(1)
        # 选择E02-Pro
        logger.info("选择教室")
        with allure.step("选择教室"):
            self.do_find(self.__CHOOSE_ROOM).click()
        logger.info("点击保存")
        with allure.step("点击保存"):
            self.do_find(self.__CLICK_SAVE).click()
        time.sleep(1)
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def clear_and_set_new_password(self, password):
        logger.info("创建直播页：清空密码并设置新密码")
        logger.info("向下滑动400像素")
        with allure.step("向下滑动400像素"):
            self.driver.execute_script("window.scrollTo(0, 400);")
        logger.info("清空并输入密码")
        with allure.step("清空并输入密码"):
            self.do_clear_send_keys(password, self.__SET_PASSWORD)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def clear_password(self):
        logger.info("创建直播页：清空观看密码")
        logger.info("向下滑动400像素")
        with allure.step("向下滑动400像素"):
            self.driver.execute_script("window.scrollTo(0, 400);")
        logger.info("清空观看密码")
        with allure.step("清空观看密码"):
            self.do_clear(self.__SET_PASSWORD)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def change_start_time(self, start_time):
        logger.info("创建直播页：修改开始时间")
        logger.info("向下滑动500像素")
        with allure.step("向下滑动500像素"):
            self.driver.execute_script("window.scrollTo(0, 500);")
        logger.info("清空现有时间并新设置时间多出当前时间10分钟")
        with allure.step("清空现有开始时间并新设置时间多出当前时间10分钟"):
            self.do_clear_send_keys(start_time, self.__START_TIME)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def change_end_time(self, end_time):
        logger.info("创建直播页：修改结束时间")
        logger.info("向下滑动500像素")
        with allure.step("向下滑动500像素"):
            self.driver.execute_script("window.scrollTo(0, 500);")
        logger.info("清空现有结束时间并新设置时间多出当前时间130分钟")
        with allure.step("清空现有时间并新设置结束时间多出当前时间130分钟"):
            self.do_clear_send_keys(end_time, self.__END_TIME)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def change_start_end_time(self, start_time, end_time):
        logger.info("创建直播页：修改开始和结束时间")
        logger.info("向下滑动500像素")
        with allure.step("向下滑动500像素"):
            self.driver.execute_script("window.scrollTo(0, 500);")
        logger.info("清空现有时间并新设置开始和结束时间")
        with allure.step("清空现有时间并新设置开始和结束时间"):
            self.do_clear_send_keys(start_time, self.__START_TIME)
            self.do_clear_send_keys(end_time, self.__END_TIME)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def start_greater_than_end_time(self, start_time, end_time):
        logger.info("创建直播页：修改开始时间大于结束时间")
        logger.info("向下滑动500像素")
        with allure.step("向下滑动500像素"):
            self.driver.execute_script("window.scrollTo(0, 500);")
        logger.info("清空现有时间并新设置开始时间大于结束时间")
        with allure.step("清空现有时间并新设置开始时间大于结束时间"):
            self.do_clear_send_keys(start_time, self.__START_TIME)
            self.do_clear_send_keys(end_time, self.__END_TIME)
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        # ==>创建直播页
        return CreateLive(self.driver)

    @ui_exception_record
    def info_error_time(self):
        logger.info("创建直播页：获取开始时间大于结束时间提示语")
        logger.info("点击保存并上架")
        with allure.step("点击保存并上架"):
            self.do_find(self.__CLICK_SAVE_listing).click()
        logger.info("获取开始时间大于结束时间提示语")
        with allure.step("获取开始时间大于结束时间提示语"):
            info = self.wait_element_until(self.__INFO_ERROR_TIME)
            msg = info.text
        logger.info(f"提示信息为：{msg}")
        return msg
