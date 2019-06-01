import iperf3
import sys

client = iperf3.Client()
client.duration = 1
client.protocol = 'udp' 

if len(sys.argv)!= 4:
	print("Usage: python3 gt.py hostname port bandwitdh")
	sys.exit(1)

# Initialization
client.server_hostname = (sys.argv[1])
client.port = int(sys.argv[2])
client.bandwitdh = int(sys.argv[3])

print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
	print(result.error)
else:
	print('Test completed:')
	print('  started at         {0}'.format(result.time))
	print('  bytes transmitted  {0}'.format(result.bytes))
	print('  jitter (ms)        {0}'.format(result.jitter_ms))
	print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))
	
	print('Average transmitted data in all sorts of networky formats:')
	print('  bits per second      (bps)   {0}'.format(result.bps))
	print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
	print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
	print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
	print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
