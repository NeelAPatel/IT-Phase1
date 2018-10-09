import socket as mysoc
import socket


# FIRST Socket
try:
	rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('{} \n'.format("socket open error ", err))

#second Socket
try:
	ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('{} \n'.format("socket open error ", err))


RsPort = 50000
TsPort = 60000
sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())

# connect to RS_SERVER first
server_bindingRS = (sa_sameas_myaddr, RsPort)
rs.connect(server_bindingRS)

data_from_server = rs.recv(1024)
print("[C]: Data received from server: [", data_from_server.decode('utf-8'), "]")
data_from_server_decoded= data_from_server.decode('utf-8')

splitList = data_from_server_decoded.split()

for i in splitList:
	if(i=='A'): #can hard code 2 bc it will always be in the 3rd position
		print(data_from_server_decoded)
	else:
		print("Will bind not finding to hostname:["+splitList[0])
		ts_ip = mysoc.gethostbyname(splitList[0])
		server_bindingTS = (ts_ip, TsPort)
		ts.connect(server_bindingTS)
		
		



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
