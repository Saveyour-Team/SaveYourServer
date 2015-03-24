import threading
import socket
import Login
import FileManager
import ssl

#Adding this line to test git autodeploy! This counts as a difference I hope...
PORT = 1337 #Currently set to 80 so I can debug by going to localhost in my browser and seeing what it says.
ADDRESS = ('0.0.0.0', PORT)
MAX_INC_SIZE = 4096




def authenticate(username, password):
	"""Uses the Login Class to authenticate the username and password."""
	#This will need to be updated to call the Login class once it is implemented.
	return Login.authenticate(username,password)


def getConnection(clientSocket, addr):
	"""This method is called whenever a new connection thread is made."""
	print "NEW CONNECTION DETECTED"
	loggedIn = False;

 	clientRequest = clientSocket.recv(MAX_INC_SIZE)


 	clientInfo = clientRequest.split(",");
 	if len(clientInfo) != 2:
 		response = "Invalid Username or Password"
 		clientSocket.send(response)
 		clientSocket.close()
 		return

 	username = clientInfo[0]
 	password = clientInfo[1]
 	#print "Received: " + clientRequest
 	#print "Username: " + username
 	#print "Password: " + password
 	loggedIn = authenticate(username, password)
 	if (loggedIn == True):
 		response = "Logged in as " + username;
 	else:
 		response = "Invalid Username or Password"
 	#print response;

	if loggedIn:
		data = FileManager.getField(username, 'data')
		response = response + ", Data: " + data
 	clientSocket.send(response)

# 	if loggedIn:
# 		data = FileManager.getField(username, 'data')
# 		clientSocket.send(data)

 	clientSocket.close()
 	return



def startListening():
	"""Start listening for incoming connections"""
	#Prepare a sever socket
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket = ssl.wrap_socket(serverSocket, cerfile='server.pem', server_side=True)
	serverSocket.bind(ADDRESS)
	serverSocket.listen(5)
	print "NOW LISTENING"
	while True:
		#Establish the connection and spawn a new thread for each connection
 		clientSocket, addr = serverSocket.accept()
		print "ACCEPTED CONNECTION"
 		thread = threading.Thread(None, getConnection, None, (clientSocket, addr), {})
 		thread.start()

def stopListening():
	"""Stop the server from listening for incoming connections."""
	serverSocket.close()


#This line is here for debug purposes, later on the ClientListener will probably be called from elsewhere.
startListening()
FileManager.connectToDB()
