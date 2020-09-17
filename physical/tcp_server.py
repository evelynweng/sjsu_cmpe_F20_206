#!/usr/bin/env python

import socket
class Tcp_server():
    def start_server(self):
        TCP_IP = '127.0.0.1' #default local host name
        TCP_PORT = 9999
        BUFFER_SIZE = 1024  # Normally 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)
        
        conn, addr = s.accept()
        print ('Connection address:', addr)
        # while 1: reopen when finished process input message
        data = conn.recv(BUFFER_SIZE)
        if data:
            data = data.decode()
            print ("received data:", data)
            conn.send("ack".encode())  # echo
        conn.close()
        return data