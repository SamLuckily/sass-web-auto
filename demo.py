import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 使用Firefox浏览器
# driver = webdriver.Firefox()
#
# # 打开百度网站
# driver.get('https://www.baidu.com')
# driver.find_element(By.NAME, "wd").send_keys("你好")
# time.sleep(3)
# driver.quit()

# from faker import Faker
#
# faker = Faker("zh_CN")
# live_name = faker.company()  # 生成一个虚假的直播名称
#
# live_full_name = live_name + "直播"  # 在直播名称后面加上“直播”字样
#
# print(live_full_name)
# from faker import Faker
#
# faker = Faker("zh_CN")
#
# # 生成直播标题（中文）
# live_title = faker.sentence(nb_words=6, variable_nb_words=True)  # 生成一个包含6个词的中文短语作为直播标题
#
# # 生成直播时间
# live_time = faker.date_time_this_month()
#
# # 生成主持人姓名
# host_name = faker.name()
#
# # 生成直播地点
# live_location = faker.city()
#
# # 组合成直播介绍
# live_description = f"本次直播标题：{live_title}\n时间：{live_time}\n主持人：{host_name}\n地点：{live_location}"
#
# print(live_description)

# 直播密码
from faker import Faker
import random
import string

fake = Faker()


def generate_random_password(min_length=4, max_length=16):
    password_length = random.randint(min_length, max_length)

    password_characters = string.ascii_letters + string.digits

    # 随机选择字符生成密码
    password = ''.join(random.choice(password_characters) for i in range(password_length))

    return password


# 生成密码
password = generate_random_password()
print("随机生成的密码为:", password)

