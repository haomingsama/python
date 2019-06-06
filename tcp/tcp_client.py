from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)

#连接服务器
serverAddr = ('10.18.150.208',8899)
'''
这种是属于短链接，长链接需要保证客户端和服务器不断的接发数据的工作
所以需要一个死循环，和与服务器断开的机制

'''
if clientSocket.connect(serverAddr): #比起udp，tcp需要connect到服务器
	while True:
		msg = input('请输入你的数据')
		#发送数据
		clientSocket.send(msg.encode())
		#接受数据
		recvData = clientSocket.recv(1024)
		print('收到的数据为%s'%recvData)
		
		if msg == 'break':
			break

clientSocket.close()

