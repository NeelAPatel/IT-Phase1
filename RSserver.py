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
print(RSarr)

# Take file contents, add to table
rowIndex= 0
while True:
 inLine = inFile.readline()
#if Line does not exist (EOF)
 if not inLine:
    break
 print("Current Line: " + str(rowIndex) + " >>" + inLine + "<<")
# 1. Separate by spaces (there are different # of spaces

 splitList = inLine.split()
 #print(*splitList, sep= "][")
 RSarr[rowIndex].append(splitList[0])
 RSarr[rowIndex].append(splitList[1])
 RSarr[rowIndex].append(splitList[2])
 print(RSarr)
 rowIndex+=1
 print("============")




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