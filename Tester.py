import socket as mysoc

# SECOND SOCKET
try:
	ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
	print("[C]: Socket for TS created")
except mysoc.error as err:
	print('{} \n'.format("TS socket open error ", err))

TsPort = 60000
tsHostName = "grep.cs.rutgers.edu"
clientHost = mysoc.gethostname()
ts_ip = mysoc.gethostbyname(tsHostName)
print("GREP IP IS: ", ts_ip)
server_bindingTS = (clientHost, TsPort)
ts.connect(server_bindingTS)
print("[C]: Connected to TS Server")

ts.send("Kill TS".encode('utf-8'))

ts.close()
