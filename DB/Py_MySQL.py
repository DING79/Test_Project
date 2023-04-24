import pymysql

db = pymysql.connect(host="localhost", user="test_user", password="test123", database="数据库名称")  #打开数据库连接
cursor = db.cursor()  #使用cursor()方法创建游标对象
execute = cursor.execute("select * from table")    #使用execute()方法执行SQL
data = cursor.fetchone()   #使用fetchone()方法获取单条数据
print("Database version：%s " % data)
db.close()  #关闭数据库连接