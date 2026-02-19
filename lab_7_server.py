from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 1019  # Changed port number

class FileHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Open and read the HTML file
        with open("index.html", "r") as file:
            content = file.read()
        # Write content to the client
        self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":
    print(f"Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), FileHandler)
    server.serve_forever()
