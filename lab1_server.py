import socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 
port = 12345 
server_socket.bind((host, port)) 
server_socket.listen(1) 
print("Server is listening...") 
conn, addr = server_socket.accept() 
print("Connection from:", addr) 
data = conn.recv(1024).decode() 
print("Client says:", data) 
conn.send("Hello Client, this is Server!".encode()) 
conn.close() 
server_socket.close() 