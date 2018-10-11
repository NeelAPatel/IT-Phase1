import socket as mysoc
import socket


def fileLineCount(path):
	with open(path) as fileIn:
		for index, element in enumerate(fileIn):
			pass
	
	val = index + 1
	return val


# second Socket
try:
	ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
	print("[TS]: Server socket created")
except mysoc.error as err:
	print('{} \n'.format("socket open error ", err))

server_binding = ('', 60000)
ts.bind(server_binding)
ts.listen(1)
# fixme i think we should be hardcoding the name of the host for ts
host = mysoc.gethostname()
print("[TS]: TS Server host name is: ", host)
localhost_ip = (mysoc.gethostbyname(host))
print("[TS]: TS Server IP address is  ", localhost_ip)
csockid, addr = ts.accept()
print("[TS]: Got a connection request from a client to this server: ", addr)

data_from_server = csockid.recv(100)
findHost = data_from_server.decode('utf-8')
print("[TS] Data received from client: [", findHost + "]")

# IMPORT FROM TS FILE HERE
inPath = 'PROJI-DNSTS.txt'
numLinesInFile = fileLineCount(inPath)
inFile = open(inPath, 'r')
print("Num Of Lines: " + str(numLinesInFile))

# Create Table
RSarr = [[] for _ in range(numLinesInFile)]

# fill in table
rowIndex = 0
while True:
	inLine = inFile.readline()
	if not inLine:  # if Line does not exist (EOF)
		break
	splitList = inLine.split()
	RSarr[rowIndex].append(splitList[0])
	RSarr[rowIndex].append(splitList[1])
	RSarr[rowIndex].append(splitList[2])
	rowIndex += 1

foundHost = 0
retHostDetail = ""
for i in range(numLinesInFile):
	if (RSarr[i][0] == findHost):
		print("FOUND HOST NAME")
		foundHost = 1
		for j in range(3):
			retHostDetail = retHostDetail + RSarr[i][j] + " "
		print("Going to sent to clinet" + retHostDetail)

# send the result back
if (foundHost == 0):
	errorMessage = findHost + "- Error:HOST NOT FOUND"
	csockid.send(errorMessage.encode('utf-8'))
else:
	csockid.send(retHostDetail.encode('utf-8'))

# Close the server socket
ts.close()
exit()
'''

if (hostnameStr in TS_table):
	entry = TS_table(hostnameStr)
else:
	entry = "hname" + "Error: Host not found"

ctsd.send(entry)
'''
