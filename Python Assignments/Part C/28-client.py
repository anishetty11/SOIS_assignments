########################################################################
#
# Program to set up a client socket to connect to port 6000
#
#######################################################################
import socket

# create a socket for ipv4 and tcp
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect the sokcet to a server at localhost port 6000
s.connect(('127.0.0.1',int('6010')))
print ("Connection established")

data='dummy'

# take the data from user, send it to the server and 
# get replies and print it on the screen
while(1):
	reply=s.recv(1024)
	print(reply.decode())

	
	data=input("Enter something to be sent to the server:\n")
	s.sendall(data.encode())

	if not data:
		break

	
s.close()