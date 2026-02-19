from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"   # Localhost only
PORT = 1019         # You can change port if needed

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Localhost server running at http://{HOST}:{PORT}")
server.serve_forever()
