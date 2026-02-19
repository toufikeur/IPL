
import socket

HOST = 'localhost'  
PORT = 5001         

# Create socket
reg_3022_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


reg_3022_server_socket.bind((HOST, PORT))
reg_3022_server_socket.listen(1)
print(f"[SERVER] Listening on {HOST}:{PORT}")


conn, addr = reg_3022_server_socket.accept()
print(f"[SERVER] Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'allahhafiz':
        print("[SERVER] Client disconnected.")
        break

    print(f"[CLIENT]: {data}")

    
    conn.send(data.encode())

conn.close()
reg_3022_server_socket.close()
