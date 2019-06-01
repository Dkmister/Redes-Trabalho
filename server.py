import iperf3

server = iperf3.Server()
server.bind_address = '10.10.10.10'
server.port = 6969
server.verbose = False

while True:
	result = server.run()

