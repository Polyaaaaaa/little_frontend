from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.lstrip('/')

        if path == "css/bootstrap.min.css":
            type_header = "text/css"
        elif path == "js/bootstrap.bundle.min.js":
            type_header = "text/javascript"
        elif path == "scripts.js":
            type_header = "text/javascript"
        elif path == "favicon.ico":
            type_header = "image/x-icon"
        else:
            path = "html/fourth_design.html"
            type_header = "text/html"

        try:
            with open(path, 'rb') as file:
                content = file.read()
            self.send_response(200)
            self.send_header("Content-type", type_header)
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "File Not Found: %s" % path)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(response, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
