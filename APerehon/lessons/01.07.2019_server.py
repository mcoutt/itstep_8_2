import socket
import threading
import time

s = socket.socket()
PORT = 6000
s.bind(("0.0.0.0", PORT))
s.listen(5)
print('Server started with ', PORT)


def handle(c):
    while True:
        try:
            data = c.recv(1024).decode()
            print(f"from client{c}", data)
            data = input("send client->")
            c.sendall(data.encode())
        except:
            c.close()
            print(f"server stop{c}")
            break


while True:
    c, a = s.accept()
    print("connected:", a)
    t = threading.Thread(target=handle, args=(c,))
    t.start()

# while True:
#     try:
#         data = c.recv(1024).decode()
#         print('try')
#     except:
#         print('except')
#         c.close()
#         c,a = s.accept()
#         print('new accept')
#     else:
#         print(f"Data client->{data}")
#         data = input('Send client->')
#         try:
#             c.sendall(data.encode())
#         except:
#             print('Not response!')
#             c.close()
# c.close()
# s.close()

# while True:
#     c,a = s.accept()
#     print('connected:',a)
#     try:
#         data = c.recv(1024).decode()
#     except:
#         continue
#     print("from client",data)
#     data = input("Send client>")
#     c.sendall(data.encode())
