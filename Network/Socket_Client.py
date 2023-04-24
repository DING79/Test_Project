import socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建socket对象
host = socket.gethostname()    #获取本地主机名
port = 8888    #设置端口 8888
client_socket.connect((host,port))  #连接服务，指定主机名和端口
msg = client_socket.recv(1024)  #接受小于 1024 字节的数据
client_socket.close()   #关闭连接
print(msg.decode("UTF-8"))  #设置接受消息编码格式



