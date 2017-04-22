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

# Bind the socket to an IP address and port
# first argument is the host we are connecting to. 
# it is empty - we don't know what the host is yet
try:
	mysock.bind(("", 1234))
except socket.error:
	sys.exit()
	
# Listen for a connection
# 5 = backlog = number of requests allowed to wait for service
# = how many clients can wait in line
try:
	mysock.listen(5)
except socket.error:
	sys.exit()
	
# LIVE SERVER
while True:
	# Accept the connection
	# returns a connection (for sending/receiving) and an address (IP, port)
	conn, addr = mysock.accept()
		
	# Receive the request
	# 1000 is maximum bytes received
	data = conn.recv(1000)
	sys.exit()
	if not data:
		break
	# Send the response
	conn.sendall(data)
	sys.exit()
	
#Close the connection and socket
conn.close()
mysock.close()


