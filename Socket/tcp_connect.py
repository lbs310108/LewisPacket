import socket
import sys


def set_tcp_connect(url, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((url, port))
        sock.close()
    except TimeoutError:
        print('*' * 50)
        print('url or port is not exist,procedure will be quit')
        sys.exit()
    except OSError:
        print('*' * 50)
        print('please put correct url or port,procedure will be quit')
        sys.exit()