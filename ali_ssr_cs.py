#!/usr/bin/env python
# encoding:utf-8
#@author:Lastprism
#@file:ali_ssr_cs.py
#@time:2018/8/319:41
#@contact:Lastprism@163.com


import socket
import sys
import threading
import time
import json

host = "45.32.112.200"
port = 56789

class myThread(threading.Thread):
    #ID表示线程的id，clientsocket表示客户端的socket，addr表示客户端的地址
    def __init__(self, ThreadID, clientsocket, addr):
        threading.Thread.__init__(self)
        self.ID = ThreadID
        self.socket = clientsocket
        self.addr = addr
    #对客户端的操作
    def run(self):
        print("收到链接: %s \n" % str(self.addr))
        ######################
        rev = int(self.socket.recv(1024))
        #waitting for improving
        if rev == 1:
            msg = query(host,port)
            self.socket.send(msg)
        ######################
        self.socket.close()
        print("来自 %s 的连接已关闭" % str(self.addr))

class Serversocket:
    #port表示要开启的端口,self.counter表示共链接的个数
    def __init__(self, port):
        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = "0.0.0.0"
        print(self.host)
        self.port = port
        self.serverSocket.bind((self.host,self.port))
        self.counter =  0
    #listenSize表示最大可连接的数量
    #开始监听并连接客户端
    def ServerListen(self, listenSize):
        self.serverSocket.listen(listenSize)
        while True:
            print("等待连接\n")
            clientsocket,addr = self.serverSocket.accept()
            my1 = myThread(self.counter, clientsocket, addr)
            self.counter += 1
            my1.start()

#waitting for improving
def query(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("1".encode("utf-8"))
    msg = s.recv(1024)
    s.close();
    print(msg.decode("utf-8"))
    return msg

def main(argv):
    if len(argv) > 2:
        host = argv[1]
        port = int(argv[2])
    else:
        host = input("please input the server's ip:\n")
        port = int(input("please input the server's port:\n"))
    print("host = " ,host , "  port = " ,port)
    Server = Serversocket(10010)
    Server.ServerListen(10);

if __name__ == '__main__':
    main(sys.argv)