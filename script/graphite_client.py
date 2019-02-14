import socket


class GraphiteClient:

    def __init__(self, host):
        self.host = host
        self.port = 2003
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_message(self, name, value, tstamp):
        graphite_msg = "%s %s %s\n" % (name, value, tstamp)
        self.sock.sendall(graphite_msg.encode('utf-8'))

    def __del__(self):
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except Exception as e:
            self.sock.close()
            print('Socket Exception: ' + str(e))


if __name__ == "__main__":
    main()