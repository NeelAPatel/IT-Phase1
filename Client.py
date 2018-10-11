import socket as mysoc
import socket


# FIRST Socket
try:
	rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('{} \n'.format("socket open error ", err))



RsPort = 50000
my_hostname = mysoc.gethostbyname(mysoc.gethostname())

# connect to RS_SERVER first
server_bindingRS = (my_hostname, RsPort)
rs.connect(server_bindingRS)

data_from_server = rs.recv(1024)
print("[C]: Data received from server: [", data_from_server.decode('utf-8'), "]")
data_from_server_decoded= data_from_server.decode('utf-8')

splitList = data_from_server_decoded.split()

for i in splitList:
	if(i=='A'): #can hard code 2 bc it will always be in the 3rd position
		print(data_from_server_decoded)
	else:
		print("Will bind not need to find host name["+splitList[0])
		# second Socket
		try:
			ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
			print("socket created")
		except mysoc.error as err:
			print('{} \n'.format("socket open error ", err))
		
		tsHostName = splitList[0]
		
		TsPort = 60000
		#FIXME this should be a different hostshortcut but cant figure it out,
		#FIXME SETTING IT ALL AS SAME HOST NAME RN BC CANT FIGURE IT OUT
		#ts_ip = mysoc.gethostbyname(splitList[0])
		ts_ip = mysoc.gethostbyname(mysoc.gethostname())
		print(ts_ip, " ]ip ")
		server_bindingTS = (ts_ip, TsPort)
		ts.connect(server_bindingTS)
		ts.send(tsHostName.encode('utf-8')) #send the hostname to ts
		data_from_ts = ts.recv(1024)
		print("recieved: ", data_from_ts.decode('utf-8'))



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
