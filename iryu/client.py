import socket
host = "192.168.1.37"
port = 5600

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect((host,port))
data=input("input data:")
server.send(data.encode())
while True:
    data = server.recv(1024).decode()
    if not data:
        break
    print(data)
    data = input("input data:")
    server.send(data.encode())


