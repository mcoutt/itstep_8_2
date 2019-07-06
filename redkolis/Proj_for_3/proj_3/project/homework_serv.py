import socket

sock = socket.socket()
sock.bind(('', 3019))
sock.listen(5)
conn, adr = sock.accept()

while True:
    try:
        data = conn.recv(1024).decode()
    except:
        conn.close()

sock.close()
