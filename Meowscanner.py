#!/bin/python3
import sys
import socket
from datetime import datetime

# Check if the correct number of arguments are provided
if len(sys.argv) == 4:  # 3 arguments: target IP, starting port, ending port
    target = socket.gethostbyname(sys.argv[1])  # Resolve hostname to IP

    first_port = int(sys.argv[2])  # Starting port
    last_port = int(sys.argv[3])   # Ending port
    
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

# Raw string used here to avoid escape sequence warning for ASCII art
print(r"""
  /\_/\  
 ( o.o )
  > ^ <  
 /     \      /MEOW    
|       |  
 \     /  
  `~~~`   
""")

try:
    for port in range(first_port, last_port + 1):  # Start scanning
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout to 1 second
        result = s.connect_ex((target, port))  #establshing connection to the target ip address and the port...

        #if result 0 it means its successful if there is 1 or more it means that error are found
        if result == 0:
            print(f" Meow! Connection successful: Port {port} is open!")

        s.close()  #close the socket connection and goes through the loop again to see the next port

# Handle exceptions
except KeyboardInterrupt:
    print("\nExiting the program due to interruption")
    sys.exit()

except socket.error:
    print("Cannot connect to the server. Please try again.")
    sys.exit()

except socket.gaierror:  # there is a problem getting the address info 
    print("Some problem with getting the address info.")
    sys.exit()
