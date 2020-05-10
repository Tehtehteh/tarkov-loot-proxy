import os
import socketserver
import http.server

loot_list = open('loot.json', 'rb').read()


class Proxy(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type',
                         'application/json')
        self.end_headers()
        self.wfile.write(loot_list)
        return


def main():
    port = int(os.environ.get('PORT', 8080))
    server = socketserver.TCPServer(('', port), Proxy)
    server.serve_forever()


if __name__ == '__main__':
    main()
