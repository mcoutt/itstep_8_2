import socket
import time

s = socket.socket()
s.connect(('127.5.5.11', 6014))

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

# sock = socket.socket()
# sock.connect(('localhost', 6000))
#
# data = input('Send> ')
# sock.sendall(data.encode())
#
# while True:
#     try:
#         data = sock.recv(1024).decode()
#     except:
#         print('Server Dead!!!')
#         break
#
#     print(data)
#     data = input('Send> ')
#     sock.sendall(data.encode())
#
# sock.close()
