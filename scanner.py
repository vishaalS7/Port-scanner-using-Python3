#!/bin/python3

import sys
import socket
from datetime import datetime 
 #define our target 
 
if len (sys.argv)==2:
 	target= socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
 	
else:
 	print("invalid amount of arguments ")
 	print ("syntax: python3 scanner.py <ip>")
 	
#add a pretty banner 
print ("-" * 50)
print ("scanning target: "+target)
print ("time started: " +str(datetime.now()))
print ("-" * 50)
 
try: 
	for port in range (50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex ((target,port))
		if result ==0:
			print (f"port {port} is open")
		s.close()
		
		
except KeyboardInterrupt:
	print ("\n Exiting program.")
	sys.exit()
	
except socket.gaierror:
	print ("hostname could not be resolved.")
	sys.exit()
	

except socket.error:
	print ("could not connect to server.")
	sys.exit()
	
