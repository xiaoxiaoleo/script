#!/usr/bin/python
# SMPT username enumeration (VRFY) script 
import socket
import sys 

if len(sys.argv) !=2:
	print "Usage: vrfy.py <username>" 
	sys.exit(0) 

#create socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#connect to socket 
connect = s.connect(('10.11.1.217',25))
#receive banner 
banner = s.recv(1024)
print banner 
#VRFY user 
s.send('VRFY' + sys.argv[1] + '\r\n') 
result = s.recv(1024)
print result 
#close the socket 
s.close() 
