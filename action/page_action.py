import traceback
import os
import time
from appium import webdriver
from util.get_desired_caps import get_desired_caps
from util.datetime_util import *
from util.find_element_util import *
from util.global_var import *
from util.log_util import *


DRIVER = ""


# 打开APP，获取webdriver对象
def open_app():
    global DRIVER
    desired_caps = get_desired_caps()
    DRIVER = webdriver.Remote(APPIUM_SERVER, desired_caps)


# 设定开始活动页
def open_start_activity(app_name, start_activity_name):
    global DRIVER
    DRIVER.start_activity(app_name, start_activity_name)


# 退出APP
def quit_app():
    global DRIVER
    DRIVER.quit()


# 在页面输入框中输入数据
def input_string(location_type, locator_expression, input_content):
    global DRIVER
    find_element(DRIVER, location_type, locator_expression).send_keys(input_content)


# 清除输入框默认内容
def clear(location_type, locator_expression):
    global DRIVER
    find_element(DRIVER, location_type, locator_expression).clear()


# 点击页面元素
def click(location_type, locator_expression):
    global DRIVER
    find_element(DRIVER, location_type, locator_expression).click()


# 断言界面源码是否存在某关键字或关键字符串
def assert_string_in_pagesource(assert_string):
    global DRIVER
    try:
        assert assert_string in DRIVER.page_source, "%s not found in page source!" % assert_string
        info("断言成功【关键字：{}】".format(assert_string))
    except:
        error("断言失败【关键字：{}】".format(assert_string))
        raise


# 强制等待
def sleep(sleep_seconds):
    time.sleep(int(sleep_seconds))


# 批量断言
def assert_app_list(location_type, locator_expression, assert_string):
    global DRIVER
    assert_string_list = assert_string.split(",")
    elements = find_element(DRIVER, location_type, locator_expression)
    for element in elements[:3]:
        assert element.text in assert_string_list


# 截图函数
def take_screenshot():
    global DRIVER
    # 创建当前日期目录
    dir = os.path.join(EXCEPION_PIC_PATH, get_chinese_date())
    if not os.path.exists(dir):
        os.makedirs(dir)
    # 以当前时间为文件名
    file_name = get_chinese_time()
    file_path = os.path.join(dir, file_name+".png")
    try:
        DRIVER.get_screenshot_as_file(file_path)
        # 返回截图文件的绝对路径
        return file_path
    except:
        print("截图发生异常【{}】".format(file_path))
        traceback.print_exc()
        return file_path

