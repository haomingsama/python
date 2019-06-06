###写一个服务端的监听程序和收发客户端发来的数据
###这个只能连一个客户端
###要连多个客户端，需要放到死循环里去，不断的接受客户端的连接--但这种方法只能接受最近客户端的信息，其他客户端的信息接收不到
###应该服务器和客户端的通信是相互不干扰，相互独立的。
###多线程和多进程 都可以解决这个问题
###系统提供的方法也可以

from socket import *
import  multiprocessing#导入进程
import copy


def clientProcess(clientSocket):
	while True:
		#与客户端通信
		recvData = clientSocket.recv(1024)
		print(recvData)

		#给客户端发
		clientSocket.send(b'hello')

		#关闭socket
		if recvData.decode() == 'break':
			break
	clientSocket.close()



serverSocket = socket(AF_INET,SOCK_STREAM)

#绑定地址

serverAddr=('10.18.150.208',8891)
serverSocket.bind(serverAddr)

#进入监听状态(listening)
serverSocket.listen(5) #这个参数代表什么？

#接受客户端连接
'''
这种是属于短链接，长链接需要保证客户端和服务器不断的接发数据的工作
所以需要一个死循环，和与服务器断开的机制

'''
while True:
	try:
		clientSocket, clientAddr = serverSocket.accept() #这个方法返回一个元祖。用一个新的socket和客户端通信
		print("接收到客户端：%s port %s"%(clientAddr[0],clientAddr[1])
		clientP = multiprocessing.Process(target = clientProcess, args = (clientSocket,))
		clientP.start()

	except: 
		pass

#关闭监听socket

serverSocket.close()


