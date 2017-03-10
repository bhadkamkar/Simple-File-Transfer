import BaseHTTPServer
import argparse
from os import curdir, stat, sep


class HTTPHandlerClass(BaseHTTPServer.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        content_length = self.headers.getheader('Content-Length')
        self.send_ok_response()

    def do_GET(self):
        try:
            file_size = stat(curdir + sep + self.path).st_size
            with open(curdir + sep + self.path, "rb") as file_handler:
                self.send_ok_response(data=file_handler.read(), file_size=file_size)
        except IOError as e:
            self.send_not_found_request_response()

    def send_ok_response(self, **kwargs):
        # send code 200 response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        if kwargs.get("data"):
            self.send_header('Content-Length', kwargs.get("file_size"))
            self.end_headers()
            self.wfile.write(kwargs.get("data"))
        else:
            self.end_headers()

    def send_not_found_request_response(self):
        self.send_response(404)

    # suppress logs
    def log_message(self, format, *args):
        return


def http_server(ip, port):
    server_address = (ip, port)
    httpd = BaseHTTPServer.HTTPServer(server_address, HTTPHandlerClass)
    print('http server is running...')
    httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Python HTTP server implementation. Please specify server IP and port")
    parser.add_argument('-i', '--server-ip', required=True, help='Server IP')
    parser.add_argument('-p', '--server-port', required=True, help='Server Port')
    args = parser.parse_args()
    http_server(args.server_ip, int(args.server_port))


if __name__ == "__main__":
    main()