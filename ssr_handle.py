#!/usr/bin/env python
# encoding:utf-8
#@author:Lastprism
#@file:ssr_handle.py
#@time:2018/2/2711:13
#@contact:Lastprism@163.com

import os
import sys
import json

pp = "port_password"
file_name = "/etc/shadowsocks.json"
#file_name = "port.json"

def formatJson(setting):
    return json.dumps(setting,sort_keys=True,indent=4)

def loadJson():
    with open(file_name) as f:
        setting = json.load(f)
        return setting

def dumpJson(setting):
    with open(file_name,'w+') as f:
        json.dump(setting, f)

def open_port(port_id):
    os.system("iptables -I INPUT -p tcp --dport %s -j ACCEPT &"%str(port_id))
    print("open %s succeed"%str(port_id))

def open_all_port():
    setting = loadJson()
    for x in setting[pp]:
        open_port(x)

def add_user():
    setting = loadJson()
    print(formatJson(setting['port_password']))
    user_port = input("please input the port(1-65535):")
    pwd = input("please input the pwd:")
    setting[pp][user_port] = pwd
    dumpJson(setting)
    open_port(user_port)
    print("add succeed")

def delete_user():
    setting = loadJson()
    print(formatJson(setting[pp]))
    user_port = input("please input the port(1-65535):")
    del setting[pp][user_port]
    dumpJson(setting)
    print("delete succeed")

def mult_users():
    setting = loadJson()
    pwd = setting["password"]
    server_port = setting["server_port"]
    del setting["password"]
    del setting["server_port"]
    print(type(setting))
    setting[pp] = {}
    setting[pp][server_port] = pwd
    dumpJson(setting)

def restart_ssr():
    os.system("/etc/init.d/shadowsocks restart")
    print("restart succeed")
def formatWrite():
    setting = loadJson()
    dumpJson(formatJson(setting))
def menu():
    while True:
        print("1.open port")
        print("2.add user")
        print("3.delete user")
        print("4.open all port")
        #print("5.format write")
        print("7.mult-users")
        print("66.restart ssr")
        print("0.exit")
        op = int(input())
        if op == 1:
            port = input("please input the port(1-65535):")
            open_port(port)
        elif op == 2:
            add_user()
        elif op == 3:
            delete_user()
        elif op == 4:
            open_all_port()
        #elif op == 5:
         #   formatWrite()
        elif op == 7:
            mult_users()
        elif op == 0:
            exit()
        elif op == 66:
            restart_ssr();
        else:
            sys.exit(op)
def main(argv):
    menu();

if __name__ == '__main__':
    main(sys.argv)