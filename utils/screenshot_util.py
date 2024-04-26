import time
import allure


# 1.装饰器架子搭好
# 2.把相关逻辑嵌套进来
# 3.需要通过driver实例截图/打印page_source,装饰器需要先去获取driver对象
def ui_exception_record(func):
    def inner(*args, **kwargs):
        # 获取被装饰方法的self 也就是实例对象
        # 通过self就可以拿到声明的实例变量driver
        # 前提条件：1.被装饰的方法是一个实例方法 2.实例需要有实例变量self.driver
        # 被装饰函数还没有执行，所以还没有self.driver  解决方案1：获取driver 放在函数执行之后 方案二：放到初始函数里面
        # 隐藏bug,一旦被装饰方法有返回值，会丢失返回值 解决方案：在try:里面添加return
        try:  # 当被装饰方法/函数发生异常就捕获并做数据记录
            return func(*args, **kwargs)
        except Exception:
            # 出现异常的处理
            # 截图操作
            driver = args[0].driver
            print("出现异常了")
            timestamp = int(time.time())
            # 注意：一定要提前创建好images路径
            image_path = f"../images/image_{timestamp}.PNG"
            page_source_path = f"../page_source/page_source_{timestamp}.html"
            # 截图
            driver.save_screenshot(image_path)
            # 记录page_source
            with open(page_source_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            # 将截图放到allure报告的数据中
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            # 将page_source记录到allure报告中,页面格式用HTML 源码格式用TEXT
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            time.sleep(1)
            return None
            raise Exception

    return inner
