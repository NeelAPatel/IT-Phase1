import socket as mysoc

def fileLineCount(path):
	with open(path) as fileIn:
		for index, element in enumerate(fileIn):
			pass

	val = index + 1
	return val


try:
    ss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    print("[S]: Server socket created")
except mysoc.error as err:
    print('{} \n'.format("socket open error ", err))
server_binding = ('', 50000)
ss.bind(server_binding)
ss.listen(1)
host = mysoc.gethostname()
print("[S]: Server host name is: ", host)
localhost_ip = (mysoc.gethostbyname(host))
print("[S]: Server IP address is  ", localhost_ip)
csockid, addr = ss.accept()
print("[S]: Got a connection request from a client at RSSERVER", addr)


# IMPORT FROM TS FILE HERE
inPath = 'PROJI-DNSTS.txt'
numLinesInFile = fileLineCount(inPath)
inFile = open(inPath, 'r')
print("Num Of Lines: " + str(numLinesInFile))


#Create Table
RSarr = [[] for _ in range(numLinesInFile)]

#fill in table
rowIndex= 0
while True:
 inLine = inFile.readline()
 if not inLine: #if Line does not exist (EOF)
    break
#print("Current Line: " + str(rowIndex) + " >>" + inLine + "<<")
#Separate by spaces (there are different # of spaces
 splitList = inLine.split()
 RSarr[rowIndex].append(splitList[0])
 RSarr[rowIndex].append(splitList[1])
 RSarr[rowIndex].append(splitList[2])
 #print(RSarr)
 rowIndex+=1
 #print("============")


testHostName = "www.rutgers.com"
foundHost =0
retHostDetail=""
for i in range(numLinesInFile):
	if (RSarr[i][0]== testHostName):
		print("FOUND HOST NAME")
		foundHost=1
		for j in range(3):
			retHostDetail= retHostDetail + RSarr[i][j]+ " "
		print(retHostDetail)
	
if(foundHost == 0):
	print("NEVER FOUND IT")



# Close the server socket
ss.close()
exit()

'''


if (hostnameStr in RS_table):
	entry = TS_table(hostnameStr)
else:
	entry = TS-Table-row(Flag = 'NS')

crsd.send(entry)
'''