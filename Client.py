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


RsPort = 50000
TSPort = 60000
sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())

# connect to RS_SERVER
server_binding = (sa_sameas_myaddr, RsPort)
ctors.connect(server_binding)
## GENERAL SETUP
# Select Port number | Host Name | LocalHost IP

#localhost_ip = (mysoc.gethostbyname(myHost))


# DETERMINE HOSTNAME OF RS SERVER/PORT
# BIND CTORS TO RS ADDRESS/ RSPORT]

#FIRST Connect to RS Server
'''

ctors.send("hostname", RSserver)
dr = ctors = recv()

if flag field(dr) == 'A':
	output(dr)
else:
	if flag - field(dr) == 'NS':
		#Connect to TS server
		TSname = hostname - field(fr)
		# Determine IP address  of TSname/ bind ctots to TS addreess
		ctots.send(TSHostName..? )
		
		#Connect and send hostname string
		dr = ctots.recv()
		output(dr)
		'''
