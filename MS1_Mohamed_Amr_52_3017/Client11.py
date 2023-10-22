import socket
import select
import sys


host = "localhost"
port = 55645

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input(" > ")

while message.strip() != "CLOSE SOCKET":
    client_socket.send(bytes(message, "utf-8"))
    data = client_socket.recv(1024)

    print('Received from server: ' + data.decode("utf-8"))

    message = input(" > ")

client_socket.close()
