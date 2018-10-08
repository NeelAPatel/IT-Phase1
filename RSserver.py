import socket as mysoc

try:
    rssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
    print('[RS]{} \n'.format("RS server socket open error ", err))


## GENERAL SETUP
# Select Port number | Host Name | LocalHost IP
server_binding = ('', 50007)
myHost = mysoc.gethostname()
localhost_ip = (mysoc.gethostbyname(myHost))

#bind to socket
rssd.bind(server_binding)

crsd, addr = rssd.accept()

# hnstring = hostnameStr
hostnameStr = crsd.recv()

if (hostnameStr in RS_table):
	entry = TS_table(hostnameStr)
else:
	entry = TS-Table-row(Flag = 'NS')

crsd.send(entry)