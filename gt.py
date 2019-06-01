import iperf3
import sys

client = iperf3.Client()
client.duration = 1
client.protocol = 'udp' 

if len(sys.argv)!= 4:
	print("Usage: python3 gt.py hostname port bandwitdh")
	sys.exit(1)

# Initialization
client.server_hostname = str(sys.argv[1])
client.port = int(sys.argv[2])
client.bandwitdh = int(sys.argv[3]) * 1024

client.run()
