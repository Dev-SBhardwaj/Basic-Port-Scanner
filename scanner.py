#!/bin/python3

import sys #allow us to enter command line arguments, among other things
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate a hostname to IPV4
else:
	print("invalid amonuts of arguments")
	print("Syntax: Python3 scanner.py <ip>")
	sys.exit()
#Add a pretty banner
print("." * 50)
print("scanning target "+target)
print("time started: "+str(datetime.now()))
print("." * 50)
 
try:
	for port in range(50,200):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		result =s.connect_ex((target,port)) #returns error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nexiting program.")
	sys.exit()
except socket.gaierror:
	print("hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("couldn't connect to server.")
	sys.exit()
