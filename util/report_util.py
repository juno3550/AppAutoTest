from util.email_util import send_mail
from util.log_util import *
from util.datetime_util import *


# 生成测试报告并发送邮件
def create_excel_report_and_send_email(excel_obj, receiver, subject, content):
    """
    :param excel_obj: excel对象用于保存文件
    :param timestamp: 用于文件命名的时间戳
    :return: 返回excel测试报告文件名
    """
    time_stamp = get_timestamp()
    report_path = excel_obj.save(subject, time_stamp)
    send_mail(report_path, receiver, subject+"_"+time_stamp, content)