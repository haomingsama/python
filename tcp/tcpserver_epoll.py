from sokect import * 
import select
import sys

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,)

serverAddr = ('', 8891)

serverSocket.bind(serverAddr)
serverSocket.listen(5)
#创建出epoll对象
epoll = select.epoll()
#向epoll注册设备
#注册了两个设备，服务器socket的编号，和输入的编号
epoll.register(serverSocket.fileno(),select.EPOLLIN(select.EPOLLET))
epoll.register(sys.stdin.fileno(),select.EPOLLIN(select.EPOLLET))
connections = {}
cleintAddrs = {}
while True:
	running = True
	#使用epoll去查看每个设备的状况，将有事件发生的设备其放入列表
	pollist = epoll.poll()
	for fd,even in pollist:
		if fd == serverSocket.fileno(): # 处理服务器（接受客户端连接）
			clientSocket,cleintAddr = serverSocket.accept()
			print("接收到新的连接%s"%cleintAddr[0])
			connections[clientSocket.fileno()] = clientSocket
			cleintAddrs[clientSocket.fileno()] = clinetAddr
			epoll.register(clientSocket.fileno(),select.EPOLLIN(select.EOPPLET))

		elif fd == sys.stdin.fileno(): # 处理用户键盘输入
			cmd =sys.stdin.readline()
			running =False
			break
		else: # 处理客户端socket
			recvData = connections[fd].recv(1024)
			if recvData:
				print("jieshoudaoshuju %s"%recvData)
				connections[fd].send(recvData)

			else: #客户端已经断开
				connections[fd].close()
				print('%s客户端关闭'%clientAddrs[fd][1])
				epoll.unregister[fd]
				
	if running - False:
			break
			
serverSocket.close()

