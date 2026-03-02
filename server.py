import http.server
import socketserver

PORT = 8888

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"To view the page, open http://localhost:{PORT}/glowlingo_learning_tool.html")
    httpd.serve_forever()