import http.server
import socketserver

# Define the port number for the server to listen on
PORT = 8000

# Create a request handler by extending the SimpleHTTPRequestHandler class
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the default behavior of the do_GET method
    def do_GET(self):
        # Customize the response message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world! This is your HTTP server.')

# Create an HTTP server with the custom request handler
with socketserver.TCPServer(('', PORT), MyRequestHandler) as server:
    print(f'Server running on port {PORT}. Press Ctrl+C to stop.')
    server.serve_forever()