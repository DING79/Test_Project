from Chrome_Webdriver import run_chrome_webdriver
from selenium.webdriver.common.by import By
from time import sleep

wd = run_chrome_webdriver("https://op.ewit.com.cn/login.aspx")  # 赛博威数字化运营平台
wd.implicitly_wait(8)
sleep(1)
wd.find_element(By.XPATH, '//*[@id="txtUserName"]').send_keys("jialiang.ding")  # 账号
wd.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys("jialiang.ding")  # 密码
wd.find_element(By.XPATH, '//*[@id="btnLoginin"]').click()  # 登录
sleep(3)
wd.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[6]/a').click()  # 日志填报
sleep(1)
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_up1"]/div[2]/button').click()  # 新增
sleep(1)
wd.find_element(By.XPATH, '//*[@id="tbdate"]/div/div/button').click()  # 确定
sleep(1)
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_btnAddExpense"]').click()  # 新增行
sleep(1)
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek1"]').send_keys(8)    #星期一
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek2"]').send_keys(8)    #星期二
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek3"]').send_keys(8)    #星期三
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek4"]').send_keys(8)    #星期四
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek5"]').send_keys(8)    #星期五
# wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek6"]').send_keys(8)    #星期六
# wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtWeek7"]').send_keys(8)    #星期七
sleep(1)
wd.find_element(By.XPATH, '//*[@id="ctl00_PageContent_rptWorkLog_ctl00_txtRemark"]').send_keys("")  #备注
sleep(1)
wd.find_element(By.XPATH, '//*[@id="btnTempSave"]').click()    #暂存
sleep(1)