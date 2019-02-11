import socket


class GraphiteClient:

    def __init__(self, host):
        self.host = host
        self.port = 2003

    def graphite_connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        return sock

    def send_message(self, sock, path, msg):
        graphite_msg = "%s %s %d" % (path, msg, 1)
        sock.sendall(graphite_msg.encode('utf-8'))

    def __del__(self, sock):
        try:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        except Exception as e:
            sock.close()
            print('Socket Exception: ' + e)

if __name__ == "__main__":
    main()