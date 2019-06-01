import socket
#创建socket
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sendAddr = ('10.18.250.119',8000) #可以通过这个实现和虚拟机的信息传输

#发送信息
sendData = input("Please input data: ")
udpSocket.sendto(sendData.encode('utf-8'),sendAddr) #使传入的数据支持中文


#接受信息
recvData = udpSocket.recvfrom(1024) #1024表示本次接受的最大字节数
print(recvData)
#关闭sokcet/ socket也属于计算机中的一种资源，要关掉，不然占着资源别人没法用
udpSocket.close()