import socket as mysoc


# FIRST Socket
try:
	ctors = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('{} \n'.format("socket open error ", err))


# SECOND SOCKET
try:
	ctots = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('{} \n'.format("socket open error", err))

## GENERAL SETUP
# Select Port number | Host Name | LocalHost IP
server_binding = ('', 50007)
myHost = mysoc.gethostname()
localhost_ip = (mysoc.gethostbyname(myHost))


# DETERMINE HOSTNAME OF RS SERVER/PORT
# BIND CTORS TO RS ADDRESS/ RSPORT]

#FIRST Connect to RS Server
ctors.send("hostname", RSserver)
dr = ctors = recv()

if flag field(dr) == 'A':
	output(dr)
else:
	if flag - field(dr) == 'NS'
		#Connect to TS server
		TSname = hostname - field(fr)
		# Determine IP address  of TSname/ bind ctots to TS addreess




	[determine hostname of RS server and port ] [bind ctors socket to RS address, rsport] #First Connect to RS server ctors.send(“hostname”,RSserver ) dr=ctors.recv(…..) if flag field(dr) == ‘A’ output(dr) else
if flag-field (dr) == ‘NS’
[connect to TS server] TSname= hostname-field(dr)
[Determine IP address of TSname bind ctots socket to TS address,
tsport] ctots.send(hostname)
[Connect and send hostname string ] dr=ctots.recv(…..)
output (dr