# 用tftp发送文件给服务器

from socket import *
import struct

udpSocket = socket(AF_INET,SOCK_DGRAM)
filename = 'test.gif'
fmt = str.format('!H%ssb5sb'%len(filename))
#定义要下载服务器的地址
tftpAddr = ('ip地址'，端口)
#依照特定的格式打包数据
msg = struct.pack(fmt,1,filename.encode(),0,'octet', 0)

udpSocket.sendto(msg,tftpAddr)
f = None


### 但是只是发送，服务器没有接收
while True: #不断滴接受服务器的信息，并且发送确认信息，然后再接收，直到接受完毕
	### 接受服务器返回的信息
	recevData = udpSocket.recvfrom(1024)
	print(recevData)

	### 服务器直接返回了数据包，直接将发送的数据包往文件里写
	### 第一步： 解包

	data = strcut.unpack('!HH',recvData[0][:4])




	##如果收到错误信息，则将其打印出来
	datatype = data[0]
	dataNO = data[1] #数据序号
	
	if datatype ==5:
		print('%s'%recvData[0][4:].decode())
		break #出错要退出循环
	## 如果是正常的数据包，开始写数据

	elif datatype ==3:
		datalen = len(recevData[0][4:]) # 弄清楚数据长度，决定什么时候关闭file，长度正常是512字节，如果少于512字节，则是最后一块
		if dataNO ==1 : # 第一块数据，只有第一块需要打开文件,其他区块直接往里写就行了
			f = open(filename, 'wb')
			f.write(recvData[0][4:]) ## 对正常的数据包来说，前4个字节是类型和长度
		else: 
			f.write(recvData[0][4:])

		#给服务器发送确认包

		msg = struct.pack('!HH',4,dataNo)
		udpSocket.sendto(msg,recvData[1]) #需要给正在给你发数据的那个端口发， 而不是服务器本身的端口。因为服务器会创建socket给你发数据


		#收到数据包中的数据的长度，如果小于512， 就认为文件已经接受完毕
		if datalen < 512:
			f.close()
			break # 文件接受完了要退出循环


udpSocket.close()