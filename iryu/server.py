import socket
import threading


def handleClient(client:socket.socket,addr):
    name = client.recv(1024).decode()
    if not name:
        client.close()
    print(name+" connected")
    client.send(b"hello "+name.upper().encode())
    while True:
        data = client.recv(1024).decode()
        if not data or data=="q":
            print(name+" disconnected")
            break
        print(str(name)+" : "+data)
        data=data.upper().encode()
        client.send(data)
    client.close()

host = "0.0.0.0"
port = 5600

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

while True :
    client,addr = server.accept()
    thread =threading.Thread(target=handleClient,args=(client,addr)) 
    thread.start()