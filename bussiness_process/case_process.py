import traceback
import re
from util.global_var import *
from util.log_util import *
from util.datetime_util import *
from util.excel_util import Excel
from action.page_action import *


# 执行一条测试用例（即一行测试数据）
def execute_case(excel_file_path, case_data, test_data_source=None):
    # 用例数据格式校验
    if not isinstance(case_data, (list, tuple)):
        error("测试用例数据格式有误！测试数据应为列表或元组类型！【%s】" % case_data)
        case_data[CASESTEP_EXCEPTION_INFO_COL_NO] = "测试用例数据格式有误！应为列表或元组类型！【%s】" % case_data
        case_data[CASESTEP_TEST_RESULT_COL_NO] = "Fail"
    # 该用例无需执行
    if case_data[CASESTEP_IS_EXECUTE_COL_NO].lower() == "n":
        info("测试用例步骤【%s】无需执行" % case_data[CASESTEP_NAME_COL_NO])
        return
    # excel对象初始化
    if isinstance(excel_file_path, Excel):
        excel = excel_file_path
    else:
        excel = Excel(excel_file_path)
    # 获取各关键字
    operation_action = case_data[CASESTEP_ACTION_COL_NO]  # 操作动作（即函数名）
    locate_method = case_data[CASESTEP_LOCATE_METHOD_COL_NO]  # 定位方式
    locate_expression = case_data[CASESTEP_LOCATE_EXPRESSION_COL_NO]  # 定位表达式
    operation_value = case_data[CASESTEP_OPERATION_VALUE_COL_NO]  # 操作值
    # 由于数据驱动，需要进行参数化的值
    if test_data_source:
        if re.search(r"\$\{\w+\}", str(operation_value)):
            # 取出需要参数化的值
            key = re.search(r"\$\{(\w+)\}", str(operation_value)).group(1)
            operation_value = re.sub(r"\$\{\w+\}", test_data_source[key], str(operation_value))
            # 将参数化后的值回写excel测试结果中，便于回溯
            case_data[CASESTEP_OPERATION_VALUE_COL_NO] = operation_value
    # 拼接关键字函数
    if locate_method and locate_expression:
        if operation_value:
            func = "%s('%s', '%s', '%s')" % (operation_action, locate_method, locate_expression, operation_value)
        else:
            func = "%s('%s', '%s')" % (operation_action, locate_method, locate_expression)
    else:
        if operation_value:
            func = "%s('%s')" % (operation_action, operation_value)
        else:
            func = "%s()" % operation_action
    # 执行用例
    try:
        eval(func)
        info("测试用例步骤执行成功：【{}】 {}".format(case_data[CASESTEP_NAME_COL_NO], func))
        case_data[CASESTEP_TEST_RESULT_COL_NO] = "Pass"
    except:
        info("测试用例步骤执行失败：【{}】 {}".format(case_data[CASESTEP_NAME_COL_NO], func))
        case_data[CASESTEP_TEST_RESULT_COL_NO] = "Fail"
        error(traceback.format_exc())
        # 进行截图
        case_data[CASESTEP_EXCEPTION_PIC_DIR_COL_NO] = take_screenshot()
        # 异常信息记录
        case_data[CASESTEP_EXCEPTION_INFO_COL_NO] = traceback.format_exc()
    # 测试时间记录
    case_data[CASESTEP_TEST_TIME_COL_NO] = get_english_datetime()
    return case_data


if __name__ == "__main__":
    excel = Excel(TEST_DATA_FILE_PATH)
    excel.get_sheet("登录")
    all_data = excel.get_all_row_data()
    for data in all_data[1:]:
        execute_case(excel, data)
