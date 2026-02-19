import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1019

client_socket.connect((host, port))
client_socket.send("Hello Server, this is Client!".encode())

response = client_socket.recv(1024).decode()
print("Server says:", response)

client_socket.close()
