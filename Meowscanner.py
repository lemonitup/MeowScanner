#!/bin/python3
import sys
import socket
from datetime import datetime

# Check if the correct number of arguments are provided
if len(sys.argv) == 4:  #3 arguments target IP, starting port, ending port
	target = socket.gethostbyname(sys.argv[1]) #gethostbyname basically resolve the hostname and resolves it into a IP address
	#the sys first argument is after the script since the script is the 0 argument.

	first_port = int(sys.argv[2])  # the next argument would be the starting port the user want to start the scan with
	last_port = int(sys.argv[3])  # the last argument would be the ending port the user want to stop the port scannig at.
    
else:
	print("Invalid Syntax: Error due to invalid number of arguments")
	print("Syntax: python3 scanner.py <hostname or IP> <starting port> <ending port>")
	sys.exit()  

# Banner
print("-" * 60)
print(f"Scanning target: {target}")
current_datetime = datetime.now()
print(f"Time started: {current_datetime}")
print("-" * 60)
print("""
  /\_/\\  
 ( o.o )
  > ^ <  
 / 	\\    	/MEOW	 
|   	|  
 \\ 	/  
  `~~~`   
""")

try:
	for port in range(first_port, last_port + 1):  #start scanning
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	s.settimeout(1)  # Set timeout to 1 second
    	result = s.connect_ex((target, port))  #establshing connection to the target ip address and the port...

    	#if result 0 it means its successful if there is 1 or more it means that error are found
    	if result == 0:
        	print(f" Meow ! Connection successful: Port number {port} is open!")
    	else:
        	print(f"Port number {port} is closed.")

    	s.close()  # #close the socket connection and goes through the loop again to see the next port

# Handle exceptions
except KeyboardInterrupt:
	print("\nExiting the program due to interruption")
	sys.exit()
	#to terminate the scripts

except socket.error:
	print("Cannot connect to the server. Please try again.")
	sys.exit()

except socket.gaierror:  # #there is a problem with ...getting the address info

	print("Some problem with getting the address info.")
	sys.exit()
