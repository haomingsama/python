import socket
import time
#创建socket
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

bindAddr = ('10.18.250.119', 9988)

udpSocket.bind(bindAddr)



while True:
	
	recvData = udpSocket.recvfrom(1024)
	print('%s，发送方%s: %s, 返回信息'%(time.ctime(),recvData[1][0],recvData[0]))
	
	#udpSocket.sendto(recvData[0],recvData[1])
	
udpSocket.close()