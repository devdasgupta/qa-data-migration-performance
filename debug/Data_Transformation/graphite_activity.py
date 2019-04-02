import socket
import time


class Graphite:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send_message(self, path, field, value):
        msg = "%s.%s %d %d\n" % (path, field, value, time.time())
        self.sock.sendall(msg.encode('utf-8'))

    def __del(self):
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except Exception as e:
            self.sock.close()
            print(e)
