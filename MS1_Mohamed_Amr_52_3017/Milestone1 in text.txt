
import socket
from _thread import *;
import threading
import select
import sys

def server11():
  thr_counter = 0
  host = "localhost"
  port = 55645
  server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server_socket.bind((host, port))
  server_socket.listen(6)
  while True:
      conn, address = server_socket.accept()
      print('Connected to :', address[0])
      start_new_thread(thread_receive, (conn,))
      print(thr_counter)
      thr_counter=thr_counter+1
def thread_receive(conn):
    while True:

        data = conn.recv(1024)
        if data.decode("utf-8")=="CLOSE SOCKET":
            conn.close()
            break;
        data = data.upper()
        conn.send(data)
        s=threading.Thread(args=(conn,))
        s.start()



server11()


