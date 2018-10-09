import socket as mysoc
import socket

#second Socket
try:
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
	print('{} \n'.format("socket open error ", err))

 
server_binding = ('', 60000)
ss.bind(server_binding)
ss.listen(1)
host = mysoc.gethostname()
print("[S]: Server host name is: ", host)
localhost_ip = (mysoc.gethostbyname(host))
print("[S]: Server IP address is  ", localhost_ip)
csockid, addr = ss.accept()
print("[S]: Got a connection request from a client at ***TSSERVER", addr)


# Close the server socket
ss.close()
exit()
'''

if (hostnameStr in TS_table):
	entry = TS_table(hostnameStr)
else:
	entry = "hname" + "Error: Host not found"

ctsd.send(entry)
'''