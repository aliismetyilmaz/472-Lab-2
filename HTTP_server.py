# import socket module
from socket import *

# Prepare a sever socket
#Fill in start
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        #Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], 'utf-8'))
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        #Fill in start
        connectionSocket.send(
            b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
        connectionSocket.close()
        #Fill in end

serverSocket.close()
