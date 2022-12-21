import socket

# Create a socket object
s = socket.socket()

# Get the local machine name
host = socket.gethostname()

# Set the port number
port = 12345

# Bind to the port
s.bind((host, port))

# Listen for incoming connections
s.listen(5)

# Accept a connection
conn, addr = s.accept()

# Print the client address
print(f"Connected to {addr}")
i=1
while True :
    # Receive data from the client
    data = conn.recv(1024)
    if data.decode() =="q" :
        break
    print(data.decode())

    # Echo the data back to the client
    conn.send("server {} :".format(i).encode())
    i=i+1

# Close the connection
conn.close()
