from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.2"
PORT = 1019  # HTTP server port

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("Website running for csebatcheight1019.com")
print(f"Open: http://127.0.0.2:{PORT}")

server.serve_forever()
