# _*_ coding:utf-8 _*_
# @Author   : Sam
# @time 2024-03-09 11:03
import time
import pytest
from page_objects.login_page import LoginPage
from testcases.conftest import get_data


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
    def test_create_live(self, data):
        """新增直播"""
        create_page = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"])
        res = create_page.get_operate_result()
        assert "直播信息保存成功" == res
        # 清理数据
        create_page.click_live_manage().delete_live()
        time.sleep(2)

    @pytest.mark.parametrize("data", get_data()["del_live"])
    def test_del_live(self, data):
        """
        删除直播
        :return:
        """
        res = self.live_list \
            .click_add() \
            .create_live(data["live_name"], data["live_intro"]) \
            .click_live_manage() \
            .delete_live() \
            .get_del_result()
        assert "直播删除成功" == res


if __name__ == '__main__':
    pytest.main()
