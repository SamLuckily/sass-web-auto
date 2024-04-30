import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.log_util import logger
from utils.screenshot_util import ui_exception_record


class AdvancedFeatures(BasePage):
    __YES = (By.CSS_SELECTOR, "#pane-advanced>form>div:nth-child(1) div>label:nth-child(2)>span>span")  # 选择是
    __INITIAL_VISITS = (By.CSS_SELECTOR,
                        ".el-main.inner-mg.bg-white>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>form>div:nth-child(2) div>input")  # 初始访问量
    __INITIAL_NUMBER_OF_ONLINE = (By.CSS_SELECTOR,
                                  ".el-main.inner-mg.bg-white>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>form>div:nth-child(3) div>input")
    __CLICK_ONLY_SCHOOL = (By.XPATH, "//span[text()='仅本校用户']")  # 初始在线人数
    __SAVE = (By.CSS_SELECTOR,
              ".el-main.inner-mg.bg-white>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>form>div:nth-child(5)>button>span")  # 权限仅本校用户
    __EDIT_TOAST = (By.XPATH, "//p[text()='直播信息编辑成功']")  # 直播信息编辑成功

    @ui_exception_record
    def edit_advanced_features(self, initial_visits_num, initial_online_num):
        logger.info("高级功能页面：设置文字互动，初始访问量/在线人数")
        with allure.step("文字互动选是"):
            self.do_find(self.__YES).click()
        with allure.step("初始访问量设置"):
            self.do_send_keys(initial_visits_num, self.__INITIAL_VISITS)
        with allure.step("初始在线人数设置"):
            self.do_send_keys(initial_online_num, self.__INITIAL_NUMBER_OF_ONLINE)
        with allure.step("权限：仅本校用户"):
            self.do_find(self.__CLICK_ONLY_SCHOOL).click()
        with allure.step("点击保存"):
            self.do_find(self.__SAVE).click()
        return AdvancedFeatures(self.driver)

    @ui_exception_record
    def get_edit_advance_features_result(self):
        logger.info("创建直播页：获取编辑后结果")
        logger.info("获取冒泡消息文本")
        with allure.step("获取冒泡消息文本"):
            toast = self.wait_element_until(self.__EDIT_TOAST)
        msg = toast.text
        logger.info(f"冒泡信息为：{msg}")
        # ==>返回消息文本
        return msg
