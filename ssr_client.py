#!/usr/bin/env python
# encoding:utf-8
#@author:Lastprism
#@file:ssr_client.py
#@time:2018/8/321:05
#@contact:Lastprism@163.com


import sys
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "101.200.42.79"
#host = "45.32.112.200"

port = 10010
#port = 56789
s.connect((host,port))
s.send("1".encode("utf-8"))
msg =  s.recv(1024)
s.close();
print(msg.decode("utf-8"))