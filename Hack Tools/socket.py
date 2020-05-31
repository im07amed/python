import socket

host = '127.0.0.1'
port = 9999
# 1 - 1023 registered ports
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))