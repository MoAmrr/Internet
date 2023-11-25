import socket
from _thread import *
import threading

server = socket.socket()
print("socket successfully created")
port = 12343
server.bind(('172.20.10.2', port))
server.listen(5)
print("socket is listening")


def thread_receive(client):
    while True:
        msg = client.recv(1024)
        print("from client: " + msg.decode('utf-8'))


while True:
    client, address = server.accept()
    print("got connection from", address)
    start_new_thread(thread_receive, (client,))