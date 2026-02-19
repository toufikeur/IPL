import socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 
port = 12346 
client_socket.connect((host, port)) 
print("Connected to Echo Server. Type 'exit' to quit.") 
while True: 
    message = input("You: ") 
    client_socket.send(message.encode()) 
    if message.lower() == 'exit': 
        break 
    response = client_socket.recv(1024).decode() 
    print("Server:", response) 
client_socket.close()