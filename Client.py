import socket as mysoc


def fileLineCount(path):
	with open(path) as fileIn:
		for index, element in enumerate(fileIn):
			pass
	
	val = index + 1
	return val


# FIRST Socket
try:
	rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
	print('{} \n'.format("socket open error ", err))



RsPort = 50020
clientHost = mysoc.gethostname()
print("[C]: Client name is: " , clientHost)

clientIP = mysoc.gethostbyname(mysoc.gethostname())
print("[C]: Client IP is: " , clientIP)

# connect to RS_SERVER first
server_bindingRS = (clientIP, RsPort)
rs.connect(server_bindingRS)
print ("[C]:  Connected to RS Server")



# Import from file
inPath = 'PROJI-HNS.txt'
numLinesInFile = fileLineCount(inPath)
inFile = open(inPath, 'r')
print("Num Of Lines in HNS: " + str(numLinesInFile))

rs.send(str(numLinesInFile).encode('utf-8'))
data_from_server = rs.recv(100)
msg = data_from_server.decode('utf-8')
print("[C]: From RS: " + msg)
# send num of lookups


while True:
	# Each iteration = one lookup in TS/RS
	inLine = inFile.readline()
	if not inLine:
		break;
	
	# Send line to RS
	inLine = inLine.strip('\n')
	rs.send(inLine.encode('utf-8'))
	print("Line Sent: " + inLine)
	
	
	data_from_server = rs.recv(1024)
	msg = data_from_server.decode('utf-8')
	print("[C]: From RS Response : " + msg)
	
	#split it in 3 and check 3rd portion.
	
	splitList = msg.split()
	if splitList[2] == 'NS':
		print("MUST CONNECT TO TS NOW.")
	else:
		print("VALID")
	
	print("")





data_from_server = rs.recv(1024)
print("[C]: Data received from RS server: [", data_from_server.decode('utf-8'), "]")
data_from_server_decoded= data_from_server.decode('utf-8')




splitList = data_from_server_decoded.split()

for i in splitList:
	if(i=='A'): #can hard code 2 bc it will always be in the 3rd position
		print(data_from_server_decoded)
	else:
		print("[C]: Will not bind, need to find host name["+splitList[0] + "]")
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
		print("[C] recieved: ", data_from_ts.decode('utf-8'))



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
