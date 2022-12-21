import socket,sys,threading,traceback,ssl,time,os
max_conn=10000
buffer_size=10000

# Load the certificate and key
cert_file = os.path.abspath("DigiCertTLSECCP384RootG5.crt.pem")
def main():
    # Get the listening port from the user
    try:
        listen_port = 9999 # int(input("Enter a listening port: "))
    except KeyboardInterrupt:
        sys.exit (0)

    # Set the maximum number of connections and the buffer size
    #max_conn = 10000
    #buffer_size = 10000
    
    # Create a socket and bind it to the listening port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("192.168.1.37", listen_port))
        s.listen(max_conn)
        print("[*] Intializing socket. Done.")
        print("[*] Socket binded successfully...")
        print("[*] Server started successfully [{}]".format(listen_port))
    except Exception as e:
        print(e)
        sys.exit(2)
    
    # Accept incoming connections and start a new thread for each connection
    while True:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
            threading.Thread(target=conn_string,args=(conn,data,addr)).start()
        except KeyboardInterrupt:
            s.close()
            print("\n[*] Shutting down...")
            sys.exit(1)
    s.close()
def conn_string(conn, data, addr):
    try:
        # Print the client's IP address9999
        print("Client IP address:",addr)
        # Parse the first line of the request message to extract the URL
        first_line = data.decode('latin-1').split("\n")[0]
        print("First line of the request message:",first_line)
        url = first_line.split(" ")[1]
        
        # Split the URL into the webserver and resource path
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]
            
        port_pos = temp.find(":")
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1
        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int(temp[(port_pos + 1):][:webserver_pos - port_pos -1])
            webserver = temp[:port_pos]
        
        print("Webserver:",webserver)
        # Call the proxy_server function to handle the connection
        proxy_server(webserver, port, conn, data, addr)
    except Exception as e:
        print(e)
        traceback.print_exc()

def proxy_server(webserver, port, conn, data, addr):
    print("Webserver:",webserver,"Port:",port,"Connection:",conn,"Address:",addr)
    try:
        # Check if the connection is HTTPS or HTTP
        if False:
            # Create a socket and wrap it in an SSL/TLS layer
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #ssl_sock = ssl.wrap_socket(s,            ssl_version=ssl.PROTOCOL_TLS,                cert_reqs=ssl.CERT_REQUIRED,    ca_certs=pem)
            ssl_sock=ssl.wrap_socket(s,ca_certs=cert_file)
            # Connect to the webserver
            ssl_sock.connect((webserver, port))
            # Send the request message
            ssl_sock.send(data)
            # Receive the response message
            while 1:
                reply = ssl_sock.recv(buffer_size)
                if len(reply) > 0:
                    conn.sendall(reply)
                    print("[*] Request sent 443:",addr[0] ," > ",webserver)
                else:
                    break
            # Close the socket
            ssl_sock.close()
        else:
            # Create a socket for HTTP connections
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the webserver
            s.connect((webserver, port))
            # Send the request message
            s.send(data)
            # Receive the response message
            while 1:
                reply = s.recv(buffer_size)
                if len(reply) > 0:
                    conn.sendall(reply)
                    print("[*] Request sent: {} > {}".format(addr[0],webserver))
                else:
                    break
            # Close the socket
            s.close()
        # Close the connection to the client
        conn.close()
    except Exception as e:
        print(e)
        traceback.print_exc()
        s.close()
        conn.close()
        sys.exit(1)

main()