# use HTTPServer to combine CGI

import BaseHTTPServer
import CGIHTTPServer

HOST=''
PORT=8000

#Create the server
server=BaseHTTPServer.HTTPServer((HOST,PORT),CGIHTTPServer.CGIHTTPRequestHandler)

#Start the server
server.serve_forever()
