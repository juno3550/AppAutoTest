from bussiness_process.main_process import *
from util.report_util import *


# 组装测试场景
# excel, _ = suite_process(TEST_DATA_FILE_PATH, "进入主页")
# excel, _ = suite_process(TEST_DATA_FILE_PATH, "登录")
# excel, _ = suite_process(TEST_DATA_FILE_PATH, "退出")

# 执行主sheet的用例集
excel = main_suite_process(TEST_DATA_FILE_PATH, "测试用例")

# 生成测试报告并发送邮件
create_excel_report_and_send_email(excel, ['itsjuno@163.com', '182230124@qq.com'], "app自动化测试", "请查收附件：app自动化测试报告")
