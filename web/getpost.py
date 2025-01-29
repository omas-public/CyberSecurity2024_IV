from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        body = f'GET:{urlparse(self.path).query}'
        self.wfile.write(body.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        body = f'POST:{self.rfile.read(int(self.headers["content-length"])).decode("utf-8")}'
        self.wfile.write(body.encode())

PORT = 8000
SERVER = 'localhost'

server_address = (SERVER, PORT)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()