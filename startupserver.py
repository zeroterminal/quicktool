#!/usr/bin/python
import socket
import os

os.system("clear")
print "########################################"
print "##        ZeroTerminal Server         ##"
print "########################################"
print "##  ABOUT THE AUTHOR                  ##"
print "##  ___________________________       ##"
print "##  Name       : Jay                  ##"
print "##  mail       : zerolinuxx@gmail.com ##"
print "##  github     : zeroterminal         ##"
print "##                                    ##"
print "########################################"
print ""


	
## Global Variables ########
############################

HOST 	= 'localhost'   // Server ip
PORT 	= 8888          // Server Port
MAXC 	= 5             // Max Connections
STATUS  = "standby"   // server status

## Functions        ########
############################

def login():
	username = raw_input("username:")
	password = raw_input("password:")
	Attempts = 3

	while Attempts < 4:
		if(username == "zero" and password == "password?"):
		
			## Grant Permission ##
			Authorized = True
			return Authorized
			break
		else:
			## Deny Permission ##
			print "Invalid Username Or Password"
			Attempts --
def go():
		while Authorized == True:
			print "*** Initiating Server Startup ***"
			print "*** Accepting Connections "
			
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server.bind((HOST,PORT))
			server.listen(maxc)
			connection, addr = server.accept()

			if addr > 0:
				print "*** Connection from ", addr

			while True:
				data = connection.recv(1024)
				print "*** Incoming Message : ", repr(data)

				if not data:
					server.close()
					break

				if data == "clear":
					os.system("clear")

			break

## Initiate  		########
############################

cmd = raw_input("> ")
if(cmd == "start"):	
	login()

while True: go()

if(cmd == "stop"):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.close()
		print "*** Connection Terminated ***"	
		exit()

server.close()
