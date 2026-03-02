import http.server
import socketserver
import time

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server at http://localhost:{PORT}")
print(f"To view the page, open http://localhost:{PORT}/glowlingo_learning_tool.html")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
        pass