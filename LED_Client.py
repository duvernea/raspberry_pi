import socket
import sys
# Create a socket
try:
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("Failed to create socket")
	sys.exit()

# Connect socket to server
try:
	host = socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("Failed to get host")
	sys.exit()
# loopback address = same machine = 127.0.0.1
mysock.connect(("127.0.0.1", 1234))
# Send some data (a request)
message = "on"
try:
	mysock.sendall(message.encode())
except socket.error:
	print("Failed to send")
	sys.exit()
	
# Receive some data (a response)
# 1000 = maximum amount of bytes to receive
# recv is a blocking wait, by default
data = mysock.recv(1000)
print(data)

#Close the socket
mysock.close()


