import socket
import time

sock = socket.socket()
sock.connect(('localhost', 4013))

data = input('Send> ')
sock.sendall(data.encode())

while True:
    try:
        data = sock.recv(1024).decode()
    except:
        print('Server Dead!!!')
        break

    print(data)
    data = input('Send> ')
    sock.sendall(data.encode())

sock.close()
