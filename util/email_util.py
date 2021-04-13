import yagmail
import traceback
from util.log_util import *


def send_mail(attachments_report_name, receiver, subject, content):
    try:
        # 连接邮箱服务器
        # 注意：若使用QQ邮箱，则password为授权码而非邮箱密码；使用其它邮箱则为邮箱密码
        # encoding设置为GBK，否则中文附件名会乱码
        yag = yagmail.SMTP(user="******@163.com", password="******", host="smtp.163.com", encoding='GBK')

        # 收件人、标题、正文、附件（若多个收件人或多个附件，则可使用列表）
        yag.send(to=receiver, subject=subject, contents=content, attachments=attachments_report_name)

        # 可简写：yag.send("****@163.com", subject, contents, report)

        info("测试报告邮件发送成功!【邮件标题：%s】【邮件附件：%s】【收件人：%s】" % (subject, attachments_report_name, receiver))
    except:
        error("测试报告邮件发送失败!【邮件标题：%s】【邮件附件：%s】【收件人：%s】" % (subject, attachments_report_name, receiver))
        error(traceback.format_exc())


if __name__ == "__main__":
   # send_mail("e:\\code.txt", "182230124@qq.com", "测试邮件", "正文")
   send_mail("E:\\pycharm_project_dir\\AppAutoTest\\test_report\\2021年04月12日\\测试用例_20210412_215802.xlsx", ["itsjuno@163.com", "182230124@qq.com"], "测试邮件", "正文")