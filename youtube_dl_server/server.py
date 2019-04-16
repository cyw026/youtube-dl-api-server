import argparse
import socket
#from gevent.pywsgi import WSGIServer

from .app import app
from .version import __version__

"""
    A server for providing the app anywhere, no need for GAE
"""


def main():
    desc = """
           The youtube-dl API server.
           """

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        '-p', '--port',
        default=9191,
        type=int,
        help='The port the server will use. The default is: %(default)s',
    )

    parser.add_argument(
        '--host',
        default=socket.gethostbyname(socket.gethostname()),
        type=str,
        help='The host the server will use. The default is: %(default)s',
    )

    parser.add_argument(
        '--number-processes',
        default=1,
        type=int,
        help=('The number of processes the server will use. The default is: '
              '%(default)s'),
    )

    parser.add_argument('--version', action='store_true',
                        help='Print the version of the server')

    args = parser.parse_args()
    if args.version:
        print(__version__)
        exit(0)

    app.debug=True
    app.run(args.host, args.port, processes=args.number_processes, threaded=True)
    
    # Production
    #http_server = WSGIServer((args.host, args.port), app)
    #http_server.serve_forever()
