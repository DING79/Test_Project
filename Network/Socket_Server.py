import socket


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建socket对象
host = socket.gethostname()    #获取本地主机名
port = 8888    #设置端口 8888
server_socket.bind((host,port))    #绑定端口
server_socket.listen(5)    #设置最大连接数，超过后排队
while True:
    client_server,address = server_socket.accept()     #建立客户端连接
    print("连接地址：%s" % str(address))    #打印连接地址
    msg = "欢迎访问！" + "\r\n"     #连接成功提示信息
    client_server.send(msg.encode("UTF-8"))    #设置消息发送编码格式
    client_server.close()   #关闭连接



