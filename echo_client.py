
import socket

HOST = 'localhost'
PORT = 5001

reg_3022_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
reg_3022_client_socket.connect((HOST, PORT))
print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

while True:
    message = input("[CLIENT]: ")
    reg_3022_client_socket.send(message.encode())
    if message.lower() == 'allahhafiz':
        break

    
    echoed = reg_3022_client_socket.recv(1024).decode()
    print(f"[SERVER (echo)]: {echoed}")

reg_3022_client_socket.close()
