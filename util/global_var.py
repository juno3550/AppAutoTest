import os


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# APP配置信息路径
INI_FILE_PATH = os.path.join(PROJECT_DIR, "conf", "desired_caps_config.ini")

# 异常截图路径
EXCEPION_PIC_PATH = os.path.join(PROJECT_DIR, "exception_pic")

# 日志配置文件路径
LOG_CONF_FILE_PATH = os.path.join(PROJECT_DIR, "conf", "logger.conf")

# 测试数据文件路径
TEST_DATA_FILE_PATH = os.path.join(PROJECT_DIR, "test_data", "test_case.xlsx")

# 测试报告存放路径
TEST_REPORT_FILE_DIR = os.path.join(PROJECT_DIR, "test_report")

# Appium server地址
APPIUM_SERVER = 'http://localhost:4723/wd/hub'

# 测试数据文件中，测试用例sheet中部分列对应的数字序号
TESTCASE_CASE_NAME_COL_NO = 0
TESTCASE_FRAMEWORK_TYPE_COL_NO = 1
TESTCASE_CASE_STEP_SHEET_NAME_COL_NO = 2
TESTCASE_DATA_SOURCE_SHEET_NAME_COL_NO = 3
TESTCASE_IS_EXECUTE_COL_NO = 4
TESTCASE_TEST_TIME_COL_NO = 5
TESTCASE_TEST_RESULT_COL_NO = 6

# 用例步骤sheet中，部分列对应的数字序号
CASESTEP_NAME_COL_NO = 0
CASESTEP_ACTION_COL_NO = 1
CASESTEP_LOCATE_METHOD_COL_NO = 2
CASESTEP_LOCATE_EXPRESSION_COL_NO = 3
CASESTEP_OPERATION_VALUE_COL_NO = 4
CASESTEP_IS_EXECUTE_COL_NO = 5
CASESTEP_TEST_TIME_COL_NO = 6
CASESTEP_TEST_RESULT_COL_NO = 7
CASESTEP_EXCEPTION_INFO_COL_NO = 8
CASESTEP_EXCEPTION_PIC_DIR_COL_NO = 9

# 数据源sheet中，是否执行列对应的数字编号
DATASOURCE_DATA = 0
DATASOURCE_KEYWORD = 1
DATASOURCE_IS_EXECUTE = 2
DATASOURCE_TEST_TIME = 3
DATASOURCE_TEST_RESULT = 4

# 测试执行结果统计
TOTAL_CASE = 0
PASS_CASE = 0
FAIL_CASE = 0


if __name__ == "__main__":
    print(PROJECT_DIR)
