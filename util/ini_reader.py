import os
import configparser


# 读取ini文件的工具类
class IniParser:

    # 初始化打开ini文件
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            print("ini文件【%s】不存在！" % file_path)
            return
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path, encoding="utf-8")

    # 获取所有分组
    def get_sections(self):
        return self.cf.sections()

    # 获取指定分组的所有键
    def get_options(self, section):
        return self.cf.options(section)  # 注意，获取的键会自动转小写

    # 获取指定分组的所有键值对
    def get_items(self, section):
        return dict(self.cf.items(section))  # 注意，获取的键会自动转小写

    # 获取指定分组指定键的值
    def get_value(self, section, option):
        return self.cf.get(section, option)


if __name__ == "__main__":
    from util.global_var import *
    p = IniParser(INI_FILE_PATH)
    print(p.get_sections())
    print(p.get_options("desired_caps"))
    print(p.get_items("desired_caps"))
    print(p.get_value("desired_caps", "deviceName"))
