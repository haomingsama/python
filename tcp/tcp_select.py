from sokect import * 
import select
import sys

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,)

serverAddr = ('', 8891)

serverSocket.bind(serverAddr)
serverSocket.listen(5)

inputlist = [serverSocekt, sys.stdin]

while True:
	running = True
	#使用select去查看每个设备的状况，并根据状态将其放入不同的列表
	readable, writeable, exceptionable  = select.select(inputlist, [],[])
	for sock in readable:
		if sock ==serverSocket: # 处理服务器（接受客户端连接）
			clientSocket,cleintAddr = sock.accept()
			print("接收到新的连接%s"%cleintAddr[0])
			inputlist.append(clientSocket)
		elif sock ==sys.stdin: # 处理用户键盘输入
			cmd =sys.stdin.readline()
			running =False
			break
		else: # 处理客户端socket
			recvData = sock.recv(1024)
			if recvData:
				print("jieshoudaoshuju %s"%recvData)
				sock.sned(recvData)
			else: #客户端已经断开
				sock.close()
				inputlist.remove(sock)
		if running - False:
			break
			
serverSocket.close()

