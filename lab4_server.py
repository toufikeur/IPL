from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 1019

Handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("HTTP Server is running at port", PORT)
    httpd.serve_forever()
