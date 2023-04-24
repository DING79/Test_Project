import smtplib
from email.mime.text import MIMEText
from email.header import Header


#第三方SMTP服务
mail_host = "smtp.163.com"  #SMTP服务器地址
mail_user = "ding_jl79"   #邮箱用户名
mail_pass = "QNHCYNOJWRCYHZSW"  #POP3/IMAP/SMTP授权码

sender = "15119997815@163.com"   #设置发邮件者
receivers = ["1550828916@qq.com"]   #设置收邮件者
#第一个参数：邮件内容  第二个参数：邮件格式  第三个参数：邮件编码格式
massage = MIMEText("Python 发送邮件测试....","plain", "UTF-8")
#邮件三大头部信息
massage["From"] = Header(sender, "UTF-8")    #发件人
massage["To"] = Header("测试", "UTF-8")    #收件人
massage["Subject"] = Header("Python SMTP 邮件测试", "UTF-8")    #邮件主题
try:
    smtpObj = smtplib.SMTP()    #SMTP服务器地址
    smtpObj.connect(mail_host, 25)  #连接SMTP服务器
    smtpObj.login(mail_user,mail_pass)  #邮箱账号密码
    smtpObj.sendmail(sender, receivers, massage.as_string())    #发送邮件函数
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error：无法发送邮件！")




