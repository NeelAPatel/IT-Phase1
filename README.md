# IT-Phase1
Simplified DNS with one Client Server and two Remote servers that maintain a DNS table

- TS and RS servers each have a DNS table and Client must connect to them to look up a specific DNS. 
- One socket per server.
- Client connects to RS first, RS attempts lookup. If not found, it tells client the name of TS server and client proceeds to connect there instead. 


-----------
- Class project for Rutgers University's Internet Technology class
