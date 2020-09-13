import os
from socket import *

host ="192.168.0.101"
port = 9999

s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(5)

while True:
    c,addr = s.accept()

    type = c.recv(1024).decode('utf-8')
    if type == "shutdown":
        os.system("shutdown /f")
    elif type =="restart":
        os.system("shutdown /r")
    elif type == "music":
        os.system("E:\\Atif.mp3")

