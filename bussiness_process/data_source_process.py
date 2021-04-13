from util.excel_util import Excel
from util.global_var import *
from util.log_util import *


# 数据驱动
# 每行数据作为一个字典，存储在一个列表中。如[{"登录用户名": "xxx", "登录密码": "xxx", ...}, {...}, ...]
def get_test_data(excel_file_path, sheet_name):
    # excel对象初始化
    if isinstance(excel_file_path, Excel):
        excel = excel_file_path
    else:
        excel = Excel(excel_file_path)
    # 校验sheet名
    if not excel.get_sheet(sheet_name):
        error("sheet【】不存在，停止执行！" % sheet_name)
        return
    result_list = []
    all_row_data = excel.get_all_row_data()
    if len(all_row_data) <= 1:
        error("sheet【】数据不大于1行，停止执行！" % sheet_name)
        return
    # 将参数化的测试数据存入全局字典
    head_line_data = all_row_data[0]
    for data in all_row_data[1:]:
        if data[-1].lower() == "n":
            continue
        row_dict = {}
        for i in range(len(data[:-1])):
            row_dict[head_line_data[i]] = data[i]
        result_list.append(row_dict)
    return result_list


if __name__ == "__main__":
    from util.global_var import *
    print(get_test_data(TEST_DATA_FILE_PATH, "搜索词"))
    # [{'搜索词': 'python', '断言词': 'python'}, {'搜索词': 'mysql', '断言词': 'mysql5.6'}]
