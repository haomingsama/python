import socket
#创建socket
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

bindAddr = ('10.18.250.119', 9988)

udpSocket.bind(bindAddr)

num =0

while True:
	recvData = udpSocket.recvfrom(1024)
	print('已经收到%s 信息，内容为%s, 返回信息'%(num,recvData[0]))
	
	udpSocket.sendto(recvData[0],recvData[1])

	num +=1
udpSocket.close()