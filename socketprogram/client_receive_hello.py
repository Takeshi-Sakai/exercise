#! /usr/bin/env python
#client_receive_hello.py
import socket
import sys

argvs = sys.argv

if len(argvs) != 3:
	print "Invalid Argument."
	print "Usage: python client_receive_hello.py serverAddr serverPort."
	quit()

serverAddr = argvs[1]
serverPort = int(args[2])

client_sock = socket.socket()
client_sock.connect((serverAddr, serverPort))
client_sock.send("hello")
data = client_sock.recv(1024)
print data
client_sock.close()
