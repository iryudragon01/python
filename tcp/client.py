import socket

# Create a socket object
s = socket.socket()

# Get the local machine name
host = socket.gethostname()

# Set the port number
port = 12345

# Connect to the server
s.connect((host, port))
while True :
    # Send a message to the server
    text=input("message to server:")
    if text == "q" :
        break
    s.send(text.encode())

    # Receive data from the server
    data = s.recv(1024)

    # Print the received data
    print("server say:",data.decode())


# Close the connection
s.close()
