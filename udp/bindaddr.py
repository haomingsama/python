import socket
#创建socket
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定窗口和地址. 这样就能用这个端口接受信息
bindAddr = ('10.18.250.119',9988)

udpSocket.bind(bindAddr)

#接受数据
recevData = udpSocket.recvfrom(1024)
print(recevData)

udpSocket.close()