# _*_ coding:utf-8 _*_
# @Author   : Sam
# @time 2024-03-09 11:03
import time
import allure
import pytest
from page_objects.login_page import LoginPage
from testcases.conftest import get_data


@allure.feature("直播管理模块")
class TestLive:

    def setup_class(self):
        """
        前置步骤
        :return:
        """
        """登录页面：用户登录"""
        self.live_list = LoginPage().login()

    def teardown_class(self):
        """
        后置步骤：退出浏览器
        :return:
        """
        self.live_list.do_quit()

    @pytest.mark.parametrize("data", get_data()["create_live"])
    @allure.story("新增直播测试用例")
    @allure.title("新增直播")
    @allure.severity('critical')
    @allure.description("新增直播")
    def test_create_live(self, data):
        create_page = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"])
        res = create_page.get_operate_result()
        assert "直播信息保存成功" == res
        # 清理数据
        create_page.click_live_manage().delete_live()
        time.sleep(2)

    @pytest.mark.parametrize("data", get_data()["create_live"])
    @allure.story("查看直播测试用例")
    @allure.title("查看直播")
    @allure.severity('critical')
    @allure.description("查看直播页")
    def test_view_live(self, data):
        res = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"]) \
            .click_live_manage() \
            .view_live() \
            .click_live_manage() \
            .delete_live() \
            .get_del_result()
        assert "直播删除成功" == res

    @pytest.mark.parametrize("data", get_data()["create_live"])
    @allure.story("未上架查看直播链接测试用例")
    @allure.title("点击直播链接")
    @allure.severity('critical')
    @allure.description("查看直播页，点击直播链接")
    def test_view_link_live(self, data):
        view_page = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"]) \
            .click_live_manage() \
            .view_live()
        res = view_page.click_live_link().get_link_toast()
        assert "直播未上架，无法分享！" == res
        # 清理数据
        view_page.click_live_manage().delete_live()

    @pytest.mark.parametrize("data", get_data()["del_live"])
    @allure.story("删除直播测试用例")
    @allure.title("删除直播")
    @allure.severity('critical')
    @allure.description("删除直播")
    def test_del_live(self, data):
        res = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"]) \
            .click_live_manage() \
            .delete_live() \
            .get_del_result()
        assert "直播删除成功" == res

    @pytest.mark.parametrize("data", get_data()["create_live"])
    @allure.story("上架直播测试用例")
    @allure.title("上架直播")
    @allure.severity('critical')
    @allure.description("直播上架")
    def test_listing(self, data):
        list_page = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"]) \
            .click_live_manage() \
            .listing()
        res = list_page.get_listing_toast()
        assert "上架成功" == res
        # 清理数据
        list_page.delete_live()

    @pytest.mark.parametrize("data", get_data()["create_live"])
    @allure.story("下架直播测试用例")
    @allure.title("下架直播")
    @allure.severity('critical')
    @allure.description("直播下架")
    def test_remove_from_shelves(self, data):
        remove_page = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"]) \
            .click_live_manage()
        remove_page.listing()
        time.sleep(1)
        res = remove_page.remove_from_shelves().get_remove_shelves_toast()
        assert "下架成功" == res
        # 清理数据
        remove_page.delete_live()
