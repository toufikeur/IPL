import socket

dns_records = {
    "google.com": "142.250.190.78",
    "facebook.com": "157.240.22.35",
    "localhost": "127.0.0.1"
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Allow reuse of address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("127.0.0.1", 5053))

print("DNS Server running on port 5053...")

while True:
    message, client_address = server_socket.recvfrom(1024)
    domain = message.decode().strip()

    print("Requested:", domain)

    ip = dns_records.get(domain, "Domain not found")

    server_socket.sendto(ip.encode(), client_address)
