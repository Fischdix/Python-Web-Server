#!/usr/bin/env python3

"""
License: MIT License
Copyright (c) 2023 Jackson Fischer

HTTP Server in Python for browser hosting

Usage::
    python server.py
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, ssl, socketserver

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("cert.pem")

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        logging.info("GET request,\nPath: &s\nHeaders:\n&s\n", str(self.path), str(self.headers))
        self._set_response()
        #self.wfile.write("GET request for {}".format(self.path.encode('utf-8')))
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <-- Gets the size of data
        post_data = self.rfile.read(content_length) # <-- Gets the data
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path), str(self.headers), post_data.decode('utf-8'))
            
        self._set_response()
        #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        
#class MyTCPHandler(socketserver.BaseRequestHandler):
    #def handle(self):
        # #self.request is the TCP socket connected to the client
        #self.data = self.request.recv(1024).strip()
        #print("{} wrote:".format(self.client_address[0]))
        #print(self.data)
        #self.request.sendall(self.data.upper())
        
def run(server_class=HTTPServer, handler_class=S):
    logging.basicConfig(level=logging.INFO)
    #server_address = ('')
    #httpd = server_class(server_address, handler_class)
    logging.info('Starting HTTPD...\n')
    
    #try:
        #httpd.serve_forever()
    #except KeyboardInterrupt:
        #pass
    #httpd.server_close()
    #logging.info('Stopping HTTPD...\n')
    
if __name__ == '__main__':
    HOST, PORT = "<IP ADDR>", <port>
    # from sys import argv
    
    #if len(argv) == 2:
        #run(port=int(argv[1]))
    #else:
    with socketserver.TCPServer((HOST,PORT), S) as httpd:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        run()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server close()
        logging.info('Stopping HTTPD...\n')
        #run()