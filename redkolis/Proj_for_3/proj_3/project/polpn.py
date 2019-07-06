import socket
import threading
import time

s = socket.socket()
PORT = 6014
s.bind(("0.0.0.0", PORT))
s.listen(5)
print('Server started with', PORT)


def handle(c):
    while True:
        try:
            try:
                data = c.recv(1024).decode()
                data = int(data)
                summ = 0
            except:
                m = "Only Number!"
                c.sendall(m)
                break
            for i in range(1, data+1):
                summ += i
            c.sendall(summ)
        except:
            print('!')
            break
            # c.close()
            # print(f"server stop{c}")
            # break


while True:
    c, a = s.accept()
    print("connected:", a)
    t = threading.Thread(target=handle, args=(c,))
    t.start()
