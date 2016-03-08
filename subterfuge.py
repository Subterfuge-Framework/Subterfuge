import BaseHTTPServer
import SimpleHTTPServer
import SocketServer

from lib.GUIServer import *

#Start test listener
print "\nSubterfuge courtesy of r00t0v3rr1d3 & 0sm0s1z"

print "Starting GUI server..."
Handler = ServerHandler

SocketServer.TCPServer.allow_reuse_address=True
httpd = SocketServer.TCPServer(("", PORT), Handler)

#httpd.socket = ssl.wrap_socket (httpd.socket, certfile='cert.pem', server_side=True)
httpd.serve_forever()