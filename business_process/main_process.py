from util.excel_util import *
from util.datetime_util import *
from util.log_util import *
from util.global_var import *
from business_process.case_process import execute_case
from business_process.data_source_process import get_test_data


# # 执行具体模块的用例sheet（登录sheet，搜索sheet等）
def suite_process(excel_file_path, sheet_name, test_data_source=None):
    """
    :param excel_file_path: excel文件绝对路径或excel对象
    :param sheet_name: 测试步骤sheet名
    :param test_data_source: 数据驱动的数据源，默认没有
    :return:
    """
    # 记录测试结果统计
    global TOTAL_CASE
    global PASS_CASE
    global FAIL_CASE
    # 整个用例sheet的测试结果，默认为全部通过
    suite_test_result = True
    # excel对象初始化
    if isinstance(excel_file_path, Excel):
        excel = excel_file_path
    else:
        excel = Excel(excel_file_path)
    if not excel.get_sheet(sheet_name):
        error("sheet【】不存在，停止执行！" % sheet_name)
        return
    # 获取测试用例sheet的全部行数据
    all_row_data = excel.get_all_row_data()
    if len(all_row_data) <= 1:
        error("sheet【】数据不大于1行，停止执行！" % sheet_name)
        return
    # 标题行数据
    head_line_data = all_row_data[0]
    # 切换到测试结果明细sheet，准备写入测试结果
    if not excel.get_sheet("测试结果明细"):
        error("【测试结果明细】sheet不存在，停止执行！")
        return
    excel.write_row_data(head_line_data, None, True, "green")
    # 执行每行的测试用例
    for row_data in all_row_data[1:]:
        result_data = execute_case(excel, row_data, test_data_source)
        # 无需执行的测试步骤，跳过
        if result_data is None:
            continue
        TOTAL_CASE += 1
        if result_data[CASESTEP_TEST_RESULT_COL_NO].lower() == "fail":
            suite_test_result = False
            FAIL_CASE += 1
        else:
            PASS_CASE += 1
        excel.write_row_data(result_data)
    # 切换到测试结果统计sheet，写入统计数据
    if not excel.get_sheet("测试结果统计"):
        error("【测试结果统计】sheet不存在，停止执行！")
        return
    excel.insert_row_data(1, [TOTAL_CASE, PASS_CASE, FAIL_CASE])
    return excel, suite_test_result


# 执行【测试用例】主sheet的用例集
def main_suite_process(excel_file_path, sheet_name):
    # 初始化excel对象
    excel = Excel(excel_file_path)
    if not excel:
        error("excel数据文件【%s】不存在！" % excel_file_path)
        return
    if not excel.get_sheet(sheet_name):
        error("sheet名称【%s】不存在！" % sheet_name)
        return
    # 获取所有行数据
    all_row_datas = excel.get_all_row_data()
    if len(all_row_datas) <= 1:
        error("sheet【%s】数据不大于1行，停止执行！" % sheet_name)
        return
    # 标题行数据
    head_line_data = all_row_datas[0]
    for row_data in all_row_datas[1:]:
        # 跳过不需要执行的测试用例集
        if row_data[TESTCASE_IS_EXECUTE_COL_NO].lower() == "n":
            info("#" * 50 + " 测试用例集【%s】无需执行！" % row_data[TESTCASE_CASE_NAME_COL_NO] + "#" * 50 + "\n")
            continue
        # 记录本用例集的测试时间
        row_data[TESTCASE_TEST_TIME_COL_NO] = get_english_datetime()
        # 校验用例步骤sheet名是否存在
        if row_data[TESTCASE_CASE_STEP_SHEET_NAME_COL_NO] not in excel.get_all_sheet():
            error("#" * 50 + " 用例步骤集【%s】不存在！ " % row_data[TESTCASE_CASE_STEP_SHEET_NAME_COL_NO] + "#" * 50 + "\n")
            row_data[TESTCASE_TEST_RESULT_COL_NO] = "Fail"
            excel.write_row_data(head_line_data, None, True, "red")
            excel.write_row_data(row_data)
            continue
        # 判断本测试用例集是否进行数据驱动
        if row_data[TESTCASE_DATA_SOURCE_SHEET_NAME_COL_NO]:
            # 校验测试数据集sheet名是否存在
            if row_data[TESTCASE_DATA_SOURCE_SHEET_NAME_COL_NO] not in excel.get_all_sheet():
                error("#" * 50 + " 测试数据集【%s】不存在！ " % row_data[TESTCASE_DATA_SOURCE_SHEET_NAME_COL_NO] + "#" * 50 + "\n")
                row_data[TESTCASE_TEST_RESULT_COL_NO] = "Fail"
                excel.write_row_data(head_line_data, None, True, "red")
                excel.write_row_data(row_data)
                continue
            # 获取测试数据集
            test_data_source = get_test_data(excel, row_data[TESTCASE_DATA_SOURCE_SHEET_NAME_COL_NO])
            # 每条数据进行一次本用例集的测试
            for data_source in test_data_source:
                info("-" * 50 + " 测试用例集【%s】开始执行！" % row_data[TESTCASE_CASE_NAME_COL_NO] + "-" * 50)
                excel, test_result_flag = suite_process(excel, row_data[TESTCASE_CASE_STEP_SHEET_NAME_COL_NO], data_source)
                # 记录本用例集的测试结果
                if test_result_flag:
                    info("#" * 50 + " 测试用例集【%s】执行成功！ " % row_data[TESTCASE_CASE_NAME_COL_NO] + "#" * 50 + "\n")
                    row_data[TESTCASE_TEST_RESULT_COL_NO] = "Pass"
                else:
                    error("#" * 50 + " 测试用例集【%s】执行失败！ " % row_data[TESTCASE_CASE_NAME_COL_NO] + "#" * 50 + "\n")
                    row_data[TESTCASE_TEST_RESULT_COL_NO] = "Fail"
                # 全部测试步骤结果写入后，最后写入本用例集的标题行和测试结果行数据
                # 切换到“测试结果明细”sheet，以写入测试执行结果
                excel.get_sheet("测试结果明细")
                excel.write_row_data(head_line_data, None, True, "red")
                excel.write_row_data(row_data)
        # 本用例集无需数据驱动
        else:
            info("-" * 50 + " 测试用例集【%s】开始执行！" % row_data[TESTCASE_CASE_NAME_COL_NO] + "-" * 50)
            excel, test_result_flag = suite_process(excel, row_data[TESTCASE_CASE_STEP_SHEET_NAME_COL_NO])
            # 记录本用例集的测试结果
            if test_result_flag:
                info("#" * 50 + " 测试用例集【%s】执行成功！ " % row_data[TESTCASE_CASE_NAME_COL_NO] + "#" * 50 + "\n")
                row_data[TESTCASE_TEST_RESULT_COL_NO] = "Pass"
            else:
                error("#" * 50 + " 测试用例集【%s】执行失败！ " % row_data[TESTCASE_CASE_NAME_COL_NO] + "#" * 50 + "\n")
                row_data[TESTCASE_TEST_RESULT_COL_NO] = "Fail"
            # 全部测试步骤结果写入后，最后写入本用例集的标题行和测试结果行数据
            # 切换到“测试结果明细”sheet，以写入测试执行结果
            excel.get_sheet("测试结果明细")
            excel.write_row_data(head_line_data, None, True, "red")
            excel.write_row_data(row_data)
    return excel


if __name__ == "__main__":
    from util.report_util import create_excel_report_and_send_email
    # excel, _ = suite_process(TEST_DATA_FILE_PATH, "进入主页")
    # excel, _ = suite_process(excel, "登录")
    excel = main_suite_process(TEST_DATA_FILE_PATH, "测试用例")
    create_excel_report_and_send_email(excel, "182230124@qq.com", "app自动化测试", "请查收附件：app自动化测试报告")

