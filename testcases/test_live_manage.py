# _*_ coding:utf-8 _*_
# @Author   : Sam
# @time 2024-03-09 11:03
import time
from datetime import datetime, timedelta
import allure
from faker import Faker
from page_objects.login_page import LoginPage
from utils.view_password_util import generate_random_password


@allure.feature("直播管理模块")
class TestLive:

    def setup_class(self):
        """
        前置步骤
        :return:
        """
        """登录页面：用户登录"""
        self.live_list = LoginPage().login()
        # 自动生成直播标题和直播介绍
        faker = Faker("zh_CN")
        # 生成直播标题（中文）
        self.live_title = faker.sentence(nb_words=6, variable_nb_words=True)  # 生成一个包含6个词的中文短语作为直播标题
        # 生成直播时间
        self.live_time = faker.date_time_this_month()
        # 生成主持人姓名
        self.host_name = faker.name()
        # 生成直播地点
        self.live_location = faker.city()
        # 组合成直播介绍
        self.live_description = f"本次直播标题：{self.live_title}\n时间：{self.live_time}\n主持人：{self.host_name}\n地点：{self.live_location}"
        # 观看直播课程密码
        self.password = generate_random_password()
        # 获取当前本地时间
        now = datetime.now()
        # 开始时间计算多出10分钟的时间
        self.ten_minutes_later = now + timedelta(minutes=10)
        # 结束时间计算多出130分钟的时间
        self.two_hours_later = now + timedelta(minutes=130)
        # 格式化时间为字符串，以便设置到时间选择框中（格式根据实际情况调整）
        self.formatted_start_time = self.ten_minutes_later.strftime("%Y-%m-%d %H:%M")
        self.formatted_end_time = self.two_hours_later.strftime("%Y-%m-%d %H:%M")
        # 初始访问量/在线人数 生成随机整数
        self.random_int = faker.random_int(min=0, max=100)

    def teardown_class(self):
        """
        后置步骤：退出浏览器
        :return:
        """
        self.live_list.do_quit()

    @allure.story("新增直播测试用例")
    @allure.title("新增直播")
    @allure.severity('critical')
    @allure.description("新增直播")
    def test_create_live(self):
        create_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = create_page.get_operate_result()
        assert "直播信息保存成功" == res
        # 清理数据
        create_page.click_live_manage().delete_live()
        time.sleep(1)

    @allure.story("查看直播测试用例")
    @allure.title("查看直播")
    @allure.severity('critical')
    @allure.description("查看直播页")
    def test_view_live(self):
        res = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description) \
            .click_live_manage() \
            .view_live() \
            .click_live_manage() \
            .delete_live() \
            .get_del_result()
        assert "直播删除成功" == res

    @allure.story("未上架查看直播链接测试用例")
    @allure.title("点击直播链接")
    @allure.severity('critical')
    @allure.description("查看直播页，点击直播链接")
    def test_view_link_live(self):
        view_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description) \
            .click_live_manage() \
            .view_live()
        res = view_page.click_live_link().get_link_toast()
        assert "直播未上架，无法分享！" == res
        # 清理数据
        view_page.click_live_manage().delete_live()

    @allure.story("删除直播测试用例")
    @allure.title("删除直播")
    @allure.severity('critical')
    @allure.description("删除直播")
    def test_del_live(self):
        res = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description) \
            .click_live_manage() \
            .delete_live() \
            .get_del_result()
        assert "直播删除成功" == res

    @allure.story("上架直播测试用例")
    @allure.title("上架直播")
    @allure.severity('critical')
    @allure.description("直播上架")
    def test_listing(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description) \
            .click_live_manage() \
            .listing()
        res = list_page.get_listing_toast()
        assert "上架成功" == res
        # 清理数据
        list_page.delete_live()

    @allure.story("下架直播测试用例")
    @allure.title("下架直播")
    @allure.severity('critical')
    @allure.description("直播下架")
    def test_remove_from_shelves(self):
        remove_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description) \
            .click_live_manage()
        remove_page.listing()
        time.sleep(1)
        res = remove_page.remove_from_shelves().get_remove_shelves_toast()
        assert "下架成功" == res
        # 清理数据
        remove_page.delete_live()

    @allure.story("保存并上架直播测试用例")
    @allure.title("保存并上架直播")
    @allure.severity('critical')
    @allure.description("保存并上架直播")
    def test_save_listing_live(self):
        create_page = self.live_list \
            .click_add() \
            .create_live_listing(self.live_title, self.live_description)
        res = create_page.get_save_listing_result()
        assert "直播信息保存成功" == res
        # 清理数据
        create_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播名称测试用例")
    @allure.title("编辑直播名称")
    @allure.severity('critical')
    @allure.description("编辑直播名称")
    def test_listing_edit_live_name(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_name(self.live_title + "_edit") \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播介绍测试用例")
    @allure.title("编辑直播介绍")
    @allure.severity('critical')
    @allure.description("编辑直播介绍")
    def test_listing_edit_live_introduce(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_introduce(self.live_description + "_edit") \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播介绍图片用例")
    @allure.title("编辑直播介绍图片")
    @allure.severity('critical')
    @allure.description("编辑直播介绍图片")
    def test_listing_edit_live_introduce_image(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_introduce_image() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播封面图片用例")
    @allure.title("编辑直播封面图片")
    @allure.severity('critical')
    @allure.description("编辑直播封面图片")
    def test_listing_edit_live_cover_image(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_cover_image() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播设置观看密码用例")
    @allure.title("编辑直播设置观看密码")
    @allure.severity('critical')
    @allure.description("编辑直播设置观看密码")
    def test_listing_edit_live_password(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_set_up_password(self.password) \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播修改观看密码用例")
    @allure.title("编辑直播修改观看密码")
    @allure.severity('critical')
    @allure.description("编辑直播修改观看密码")
    def test_listing_edit_live_change_password(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .clear_and_set_new_password(self.password) \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播清空观看密码用例")
    @allure.title("编辑直播清空观看密码")
    @allure.severity('critical')
    @allure.description("编辑直播清空观看密码")
    def test_listing_edit_live_clear_password(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .clear_password() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播开始时间用例")
    @allure.title("编辑直播开始时间")
    @allure.severity('critical')
    @allure.description("编辑直播开始时间")
    def test_listing_edit_live_start_time(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .change_start_time(self.formatted_start_time) \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播结束时间用例")
    @allure.title("编辑直播结束时间")
    @allure.severity('critical')
    @allure.description("编辑直播结束时间")
    def test_listing_edit_live_end_time(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .change_end_time(self.formatted_end_time) \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播开始和结束时间用例")
    @allure.title("编辑直播开始和结束时间")
    @allure.severity('critical')
    @allure.description("编辑直播开始和结束时间")
    def test_listing_edit_live_start_end_time(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .change_start_end_time(self.formatted_start_time, self.formatted_end_time) \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播开始时间大于结束时间用例")
    @allure.title("编辑直播开始时间大于结束时间")
    @allure.severity('critical')
    @allure.description("编辑直播开始时间大于结束时间")
    def test_listing_edit_live_start_greater_than_end_time(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .start_greater_than_end_time(self.formatted_end_time, self.formatted_start_time) \
            .info_error_time()
        assert "结束时间不能早于开始时间" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播回放选是测试用例")
    @allure.title("编辑直播回放选是")
    @allure.severity('critical')
    @allure.description("编辑直播回放选是")
    def test_listing_edit_live_playback(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_password(self.live_title, self.live_description, self.password)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_playback() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("保存并上架直播后编辑直播回放选否测试用例")
    @allure.title("编辑直播回放选否")
    @allure.severity('critical')
    @allure.description("编辑直播回放选否")
    def test_listing_edit_live_playback_no(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_playback(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_playback_no() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("创建直播后编辑直播页点击保存并上架测试用例")
    @allure.title("编辑直播页点击保存并上架")
    @allure.severity('critical')
    @allure.description("编辑直播页点击保存并上架")
    def test_listing_edit_live_save_and_list(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_playback(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_save_and_list() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("创建直播后编辑直播页点击保存测试用例")
    @allure.title("编辑直播页点击保存")
    @allure.severity('critical')
    @allure.description("编辑直播页点击保存")
    def test_listing_edit_live_save(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_playback(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_save() \
            .get_edit_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("创建直播上架后编辑直播页点击取消测试用例")
    @allure.title("编辑直播页点击取消")
    @allure.severity('critical')
    @allure.description("编辑直播页点击取消")
    def test_listing_edit_cancel(self):
        list_page = self.live_list \
            .click_add() \
            .create_live_playback(self.live_title, self.live_description)
        list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_live_cancel()
        # 清空数据
        list_page.click_live_manage().delete_live()

    @allure.story("创建直播上架后编辑直播添加高级功能测试用例")
    @allure.title("编辑直播添加高级功能")
    @allure.severity('critical')
    @allure.description("编辑直播添加高级功能")
    def test_listing_edit_advanced_features(self):
        list_page = self.live_list \
            .click_add() \
            .create_live(self.live_title, self.live_description)
        res = list_page.click_live_manage().listing() \
            .click_edit() \
            .edit_click_advanced_features() \
            .edit_advanced_features(self.random_int, self.random_int) \
            .get_edit_advance_features_result()
        assert "直播信息编辑成功" == res
        # 清空数据
        list_page.click_live_manage().delete_live()
