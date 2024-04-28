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
# password = generate_random_password()
# print("随机生成的密码为:", password)
