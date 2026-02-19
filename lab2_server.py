import socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 
port = 12346 
server_socket.bind((host, port)) 
server_socket.listen(1) 
print("Echo Server is waiting for connection...") 
client_socket, addr = server_socket.accept() 
print(f"Connected with {addr}") 
while True: 
    data = client_socket.recv(1024).decode() 
    if not data or data.lower() == 'exit': 
        print("Connection closed by client.") 
        break 
    print("Client:", data) 
    client_socket.send(data.encode()) 
client_socket.close() 
server_socket.close()