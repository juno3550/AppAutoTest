from util.ini_reader import IniParser
from util.global_var import INI_FILE_PATH


def get_desired_caps():
    pcf = IniParser(INI_FILE_PATH)
    items = pcf.get_items("desired_caps")  # 获取的键会自动转成小写
    desired_caps = {
        "platformName": items.get("platformname"),
        "platformVersion": items.get("platformversion"),
        "deviceName": items.get("devicename"),
        "appPackage": items.get("apppackage"),
        "appActivity": items.get("appactivity"),
        "unicodeKeyboard": items.get("unicodekeyboard"),
        "autoAcceptAlerts": items.get("autoacceptalerts"),
        "resetKeyboard": items.get("resetkeyboard"),
        "noReset": items.get("noreset"),
        "newCommandTimeout": items.get("newcommandtimeout")
    }
    return desired_caps


if __name__ == "__main__":
    from util.global_var import *
    print(get_desired_caps())