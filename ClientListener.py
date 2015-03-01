import threading
import socket

PORT = 13372
ADDRESS = ('127.0.0.1', PORT)
MAX_INC_SIZE = 4096

def getConnection(connectionSocket, addr):
	"""This method is called whenever a new connection thread is made."""
 
 	clientRequest = connectionSocket.recv(MAKE_INC_SIZE)

 	response = ''
 		
 	connectionSocket.send(response)
 	connectionSocket.close()



def startListening:
	"""Start listening for incoming connections"""
	#Prepare a sever socket
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind(ADDRESS)
	serverSocket.listen(5)
	while True:
		#Establish the connection and spawn a new thread for each connection
 		connectionSocket, addr = serverSocket.accept()
 		thread = threading.Thread(None, getConnection, None, (connectionSocket, addr), {})
 		thread.start()

def stopListening:
	"""Stop the server from listening for incoming connections."""
	serverSocket.close() 
 	

