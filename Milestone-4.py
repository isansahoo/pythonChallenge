#simple server socket programming
import socket
import os

#creating socket with IPv4 address family and TCP connection
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server's IP and port is defined
mySocket.bind(("127.0.0.1",8886))
#GET request stored in a string
request = 'HTTP/1.1 200 OK \n Content-type:text/html\r\n\r\n Python Client - Server via TCP \n'
path = 'G:\\python'
#list = os.listdir(path)
filelist = ''
dirlist = ''


#sever can serve upto 3 client connections concurrently
mySocket.listen(3)
#continue to listen until the limit has reached 3 clients
while True:
    #waiting for client to connect to server
    client,add = mySocket.accept()
    #expecting message from client of 4096 bytes
    recv=client.recv(4096)
    #if nothing received from client, close client socket
    if not recv:
        client.close()
        break
    #send respose to the client
    for root, dirl, files in os.walk(path):
        dirlist = root + '\n'
        client.send(dirlist.encode('utf-8'))
        for fname in files:
            filelist = fname + '\n'
            client.send(filelist.encode('utf-8'))
        
    
    
    #client.send(request.encode('utf-8'))
    
#socket closed for server
mySocket.close()


