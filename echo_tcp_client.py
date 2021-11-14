import socket
import sys

data ="".join(sys.argv[1:])

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect(("10.10.10.2",5000))
    sock.sendall(bytes(data,"utf-8"))
    print("Send: "+data)
    recv_data = str(sock.recv(1024),"utf-8")
    print("Recv: "+recv_data)
    sock.close()
