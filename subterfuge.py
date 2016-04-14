import argparse
import SocketServer
import ssl
from lib.GUIServer import ServerHandler, PORT

__version__ = [2, 0]
__authors__ = ['r00t0v3rr1d3', '0sm0s1z']

#placeholder for future logging module foo
def tprint(x): print x
def xprint(x): pass
def dprint(x): print "Denug: {0}".format(x)
debug = dprint
info = tprint
warning = tprint
error = tprint

if __name__ == "__main__":
    print "\nSubterfuge courtesy of {}".format(' & '.join(__authors__))
    parser = argparse.ArgumentParser(prog="Subterfuge",usage="python subterfuge.py",
                                     description="Subterfuge MiTM framework",
                                     version='.'.join(map(str,__version__))+ 'a'
                                     )
    parser.add_argument('--ssl',action='store_true',help="Use ssl", default=False)
    parser.add_argument('--port',action='store',type=int,help="Port to listen on",default=PORT)
    opts = parser.parse_args()

    info("Starting GUI server...")
    SocketServer.TCPServer.allow_reuse_address = True

    try:
        httpd = SocketServer.TCPServer(("", opts.port), ServerHandler)
        info("Server started on http{1}://{0[0]}:{0[1]}{1}".format(httpd.socket.getsockname(),
                                                         "" if not opts.ssl else "s"))
    except Exception as e:
        error("Could not init server: {0}".format(e))
        exit()

    if opts.ssl:
        httpd.socket = ssl.wrap_socket (httpd.socket, certfile='cert.pem', server_side=True)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt as k:
        info("\rExiting...")
    except Exception as e:
        import traceback
        info("Exiting due to exception: {0}".format(e))
        error(traceback.format_exc())
    finally:
        httpd.shutdown()