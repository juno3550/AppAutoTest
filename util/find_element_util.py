from selenium.webdriver.support.ui import WebDriverWait


# 显式等待一个元素
def find_element(driver, locate_method, locate_exp):
    # 显式等待对象（最多等10秒，每0.2秒判断一次等待的条件）
    return WebDriverWait(driver, 10, 0.2).until(lambda x: x.find_element(locate_method, locate_exp))

# 显式等待一组元素
def find_elements(driver, locate_method, locate_exp):
    # 显式等待对象（最多等10秒，每0.2秒判断一次等待的条件）
    return WebDriverWait(driver, 10, 0.2).until(lambda x: x.find_elements(locate_method, locate_exp))