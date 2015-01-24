#! /usr/bin/env python
#server.py
import socket

class HelloServer:
	def __init__(self, addr, port):
		self.server_sock = socket.socket()
		self.server_sock.bind((addr, port))
		self.server_sock.listen(1)

	def start(self):
		conn, addr = self.server_sock.accept()
		print "connected by", addr
		conn.send("Hello, world")
		conn.close()

server = HelloServer("10.211.55.31", 10000)
server.start()
