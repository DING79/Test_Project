import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = "15119997815@163.com"   #设置发邮件者
receivers = ["1550828916@qq.com"]   #设置收邮件者
#第一个参数：邮件内容  第二个参数：邮件格式  第三个参数：邮件编码格式
massage = MIMEText("Python 发送邮件测试....","plain", "UTF-8")
#邮件三大头部信息
massage["From"] = Header("来自发送者的邮件", "UTF-8")    #发件人
massage["To"] = Header("测试", "UTF-8")    #收件人
massage["Subject"] = Header("Python SMTP 邮件测试", "UTF-8")    #邮件主题
try:
    smtpObj = smtplib.SMTP("localhost")    #SMTP服务器地址
    smtpObj.sendmail(sender, receivers, massage.as_string())    #发送邮件函数
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error：无法发送邮件！")




