import socket
import sys
# Create a socket
# AF_INET = Address Family Internet
# SOCK_STREAM = indicates TCP (connection-based)
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
mysock.connect((host, 80))
# Send some data (a request)
message = "GET / HTTP/1.1\r\n\r\n"
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


