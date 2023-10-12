import socket
import select
import sys

host = "localhost"

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 55143
server_socket.bind((host, port))

server_socket.listen(2)
while True:
    client, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = client.recv(1024)
        if data.decode("utf-8") == "CLOSE SOCKET":
            client.close()
            break;
        data = data.upper()
        client.send(data)

client.close()




