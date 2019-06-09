import socket
import time
import sys

if len(sys.argv)!=4:
	print("Usage: python3 new-gt.py destinationIP port bandwidth")
	sys.exit(1)

destIP = sys.argv[1]
port = sys.argv[2]
bandwidth = sys.argv[3]

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Sending data to '+destIP+ '@'+ port+' with bandwidth of '+bandwidth+'KBps')

time_sleep = 1/(int(bandwidth)*1024)

while True:
	sock.sendto(bytes(1),(destIP,int(port)))
	time.sleep(time_sleep)
