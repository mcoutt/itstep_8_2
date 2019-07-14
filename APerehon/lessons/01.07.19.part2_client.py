import socket
import time
s = socket.socket()
s.connect(('localhost', 6000))

data = input("Send>")
s.sendall(data.encode())

while True:
    try:
        data = s.recv(1024).decode()
    except:
        print('Server dead!!!')
        break
    print(data)
    data = input("Send>")
    s.sendall(data.encode())

s.close()
