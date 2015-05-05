#simple server socket programming
import socket

#creating socket with IPv4 address family and TCP connection
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server's IP and port is defined
mySocket.bind(("localhost",8888))
#sever can serve upto 3 client connections concurrently
mySocket.listen(3)
#blocking statement, waiting for client to connect
(client,(ip,port))=mySocket.accept()
client.send("HTTP/1.1 200 OK\n"
         +"Content-Type: text/html\n"
         +"\n" )


