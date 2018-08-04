#!/usr/bin/env python
# encoding:utf-8
#@author:Lastprism
#@file:vps_ssr_server.py
#@time:2018/8/319:41
#@contact:Lastprism@163.com

import socket
import sys
import threading
import time
import json

pp = "port_password"
file_name = "/etc/shadowsocks.json"

def loadJson():
    with open(file_name) as f:
        setting = json.load(f)
        return setting

def formatJson(setting):
    return json.dumps(setting,sort_keys=True,indent=4)

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


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
        if rev == 1:
            msg = loadJson();
            msg = msg[pp];
            msg["ip"] = get_host_ip()
            msg = formatJson(msg)
            self.socket.send(msg.encode("utf-8"))
        ######################
        self.socket.close()
        print("来自 %s 的连接已关闭" % str(self.addr))

class Serversocket:
    #port表示要开启的端口,self.counter表示共链接的个数
    def __init__(self, port):
        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = "0.0.0.0"
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


Server = Serversocket(56789)
Server.ServerListen(10);
