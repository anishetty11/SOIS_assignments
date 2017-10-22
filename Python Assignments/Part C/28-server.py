########################################################################
#
# Program to set up a server socket at port 6000
#
#######################################################################


import socket
import sys
from _thread import *


# create the socket for IPv4 and TCP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Bind the socket to the corresponding IP address and Port
try:
	s.bind(('127.0.0.1',int('6010')))
except socket.error as e:
	print (e)
	sys.exit(0)


# listen to clients
s.listen(1)

def connection_handle(conn):
	''' Handles each client in a seperate thread '''

	# send a welcome message
	conn.sendall(("Welcome to the server, hit something\n").encode())

	# get the data from client, and reply
	while(True):
		data=conn.recv(1024)
		print(data.decode())

		if not data:
			break

		reply="ok..."+data.decode()

		conn.sendall(reply.encode())

	conn.close()


# accept the connection continuisly
while(1):
	try:
		conn,addr=s.accept()
		print ("COnnected to %s:%s"%(addr[0],addr[1]))
	except socekt.error as e:
		print (e)
	# initiate a new thread for each connection
	start_new_thread(connection_handle,(conn,))

s.close()




