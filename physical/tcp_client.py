import socket


class Tcp_client():
    def __init__(self, to_mac, to_message):
        self.tcpip = to_mac
        self.send_message = to_message
    
    def start_client(self):
        TCP_IP = self.tcpip
        TCP_PORT = 9999
        BUFFER_SIZE = 1024
        MESSAGE = self.send_message.encode()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()

        print ("received data:", data.decode())