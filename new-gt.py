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

time2sleep = (1/(int(bandwidth))) 
b = int(bandwidth)
if b <= 1000:
	time2sleep = time2sleep * 1
if b > 1000 and b <= 2000:
	time2sleep = time2sleep * 0.9
if b > 2000:
	time2sleep = time2sleep * 0.6777


print("Time to sleep is: ",time2sleep,"seconds")
while True:
	sock.sendto(bytes(1250),(destIP,int(port)))
	time.sleep(time2sleep)
