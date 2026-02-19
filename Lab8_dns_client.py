import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address (must match server port)
server_address = ("127.0.0.1", 5053)

try:
    while True:
        domain = input("Enter domain name (or type 'exit' to quit): ").strip()

        if domain.lower() == "exit":
            break

        # Send request to server
        client_socket.sendto(domain.encode(), server_address)

        # Receive response
        response, _ = client_socket.recvfrom(1024)

        print("IP Address:", response.decode())
        print("-" * 40)

except Exception as e:
    print("Error:", e)

finally:
    client_socket.close()
    print("Client closed.")
