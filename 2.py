import socket


sock = socket.socket()
sock.connect(('localhost', 9000))
while True:
    a = input()
    sock.send(a.encode())
    data = sock.recv(1024)
    print(data)