import argparse
import SocketServer
import ssl
from lib.GUIServer import ServerHandler, PORT

__version__ = [2, 0]
__version_str__ = '.'.join(map(str,__version__)) + 'a'
__authors__ = ['r00t0v3rr1d3', '0sm0s1z']
__program__ = "Subterfuge"
__welcome__ = "{0} {1} courtesy of {2}".format(__program__, __version_str__, ' & '.join(__authors__))
#placeholder for future logging module foo
def tprint(x): print x
def xprint(x): pass
def dprint(x): print "Denug: {0}".format(x)
debug = dprint
info = tprint
warning = tprint
error = tprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__welcome__, version=__version_str__)
    parser.add_argument('-s', '--ssl', action='store_true', help='Use ssl', default=False)
    parser.add_argument('-p', '--port', action='store', type=int, help='Port to listen on', default=PORT)
    parser.add_argument('-G', '--global', dest="GL", action='store_true', help='Bind on all interfaces instead of local', default=False)
    opts = parser.parse_args()
    info("Starting subterfuge...")
    SocketServer.TCPServer.allow_reuse_address = True

    try:
        httpd = SocketServer.TCPServer(("" if opts.GL else "127.0.0.1", opts.port), ServerHandler)
        info("GUI server started on http{1}://{0[0]}:{0[1]}{1}".format(httpd.socket.getsockname(), "" if not opts.ssl else "s"))
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