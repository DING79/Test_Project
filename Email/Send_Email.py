import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


#第三方SMTP服务
mail_host = "smtp.163.com"  #SMTP服务器地址
mail_user = ""   #邮箱用户名
mail_pass = ""  #POP3/IMAP/SMTP授权码

sender = ""   #设置发邮件者
receivers = [""]   #设置收邮件者

message = MIMEMultipart()  #创建带附件实例
message["From"] = Header(sender, "UTF-8")    #发件人
message["To"] = Header("测试", "UTF-8")    #收件人
message["Subject"] = Header("Python SMTP 邮件测试", "UTF-8")    #邮件主题
message.attach(MIMEText("Python 发送邮件测试...","plain", "UTF-8"))   #正文

#带附件
annex = MIMEText(open(file=r"C:\Users\cyberway\Desktop\111.xlsx").read(), "base64", "UTF-8")
annex["Content-Type"] = "application/octet-stream"
annex["Content-Disposition"] = 'attachment; filename="test.xlsx"'
message.attach(annex)

try:
    smtpObj = smtplib.SMTP()    #SMTP服务器地址
    smtpObj.connect(mail_host, 25)  #连接SMTP服务器
    smtpObj.login(mail_user,mail_pass)  #邮箱账号密码
    smtpObj.sendmail(sender, receivers, message.as_string())    #发送邮件函数
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error：无法发送邮件！")




