#!/usr/bin/env python

import json
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import itho

prev_command = 'IthoLow'
counter = 0

class IthoRestApi(BaseHTTPRequestHandler):

    def do_GET(self):
        global prev_command
        global counter
        if self.path.startswith('/press?'):
            args_path = self.path.rsplit('?', 1)[1]
            args = args_path.split(',')
            assert len(args) == 1
            key, val = args[0].split('=')
            assert key == 'button'
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            command = {
                'high': 'IthoFull',
                'medium': 'IthoMedium',
                'low': 'IthoLow'
            }[val]
            itho.sendCommand(command, prev_command, counter)
            prev_command = command
            counter += 1
            self.wfile.write(json.dumps({'success': True, 'button': val}))
        else:
            self.send_error(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 9000)
    httpd = HTTPServer(server_address, IthoRestApi)
    httpd.serve_forever()
