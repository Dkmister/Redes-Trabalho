import iperf3

server = iperf3.Server()
server.port = 6969
server.verbose = False

while True:
	result = server.run()

