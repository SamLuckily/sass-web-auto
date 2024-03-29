from utils.read_util import base_data
from _pytest.config import Config
from _pytest.config.argparsing import Parser


# 读取yaml测试数据
def get_data():
    return base_data.read_data()


web_env = {}


# 实现命令行注册，解决自定义参数报错问题
# 多浏览器
def pytest_addoption(parser: Parser):
    # 注册一个命令行组
    hogwarts = parser.getgroup("hogwarts")
    # 第一个参数为指定的命令行的参数形式
    # pytest .\test_demo.py --browser=chrome
    # 注册一个命令行参数
    hogwarts.addoption("--browser", default="firefox", dest="browser")


def pytest_configure(config: Config):
    browser = config.getoption("browser")
    print(f"通过命令获取到的浏览器为{browser}")
    web_env["browser"] = browser
