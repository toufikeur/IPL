import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    print(f"Client {addr} says:", data.decode())
    conn.send("Message received by server".encode())
    conn.close()
    print(f"Connection closed: {addr}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1019

server_socket.bind((host, port))
server_socket.listen(5)
print("Server is running and waiting for clients...")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
