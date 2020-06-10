import os
import socketserver
import http.server

from urllib import request

loot_list = b''
ftb_loot_url = 'https://licensing.ftbcheats.com/static/items/items.json'


class Proxy(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type',
                         'application/json')
        self.end_headers()
        self.wfile.write(loot_list)
        return


def update_loot_list(url):
    req = request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
    })
    with request.urlopen(req) as response, open('loot.json', 'wb') as writer:
        writer.write(response.read())


def read_loot_list(file_name: str):
    global loot_list
    with open(file_name, 'rb') as reader:
        loot_list = reader.read()


def main():
    update_loot_list(ftb_loot_url)
    read_loot_list('loot.json')
    port = int(os.environ.get('PORT', 8080))
    server = socketserver.TCPServer(('', port), Proxy)
    server.serve_forever()


if __name__ == '__main__':
    main()
