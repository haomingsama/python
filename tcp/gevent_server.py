
rom gevent import socket, monkey

monky.patch_all()


#客户端处理
def handleRequest(conn):
	while True:
		#收数据
		data = conn.recv(1024)
		if not data:
			conn.close()
			break
		else:
			print('收到数据%s'%data)
			conn.send(data)


#创建服务器
 
 def server(port):
 	s = socket.socket()#创建服务器
 	s.bind('',port)
 	s.listen(5)
 	while True:
 		client, addr = s.accept()
 		gevent.spawn(handleRequest,client)

 if __name__ == '__main__':
 	server(7788)
 	


