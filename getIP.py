# how-to-get-ip1
import socket
host = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
print(ip)
