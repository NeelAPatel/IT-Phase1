import socket as mysoc

try:
	tssd = mysoc.socket(mysoc.AF_INET,mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('[TS]: {}	\n '.format("socket open error ",err))


## GENERAL SETUP
# Select Port number | Host Name | LocalHost IP
server_binding = ('', 50007)
myHost = mysoc.gethostname()
localhost_ip = (mysoc.gethostbyname(myHost))

# bind to socket
tssd.bind(server_binding)

ctsd, addr = tssd.accept()

# hnstring = hostnameStr
hostnameStr = ctsd.recv()

if (hostnameStr in TS_table):
	entry = TS_table(hostnameStr)
else:
	entry = "hname" + "Error: Host not found"

ctsd.send(entry)