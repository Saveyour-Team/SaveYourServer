SaveYourServer
GitHub Repository: https://github.com/Saveyour-Team/SaveYourServer.git
Website: https://github.com/Saveyour-Team/SaveYourServer
Bugs are Tracked on the SaveYour issue repository (the same one that the client uses): https://github.com/Saveyour-Team/Saveyour/issues

This is everything you need to run your own server for SaveYour.  The server is written in Python and is multi-threaded so that it accepts as many incoming connections as there are ports available on the host machine simultaneously. All connections to users running the SaveYour client goes through a connection that uses TLS to secure it, and passwords are hashed using the Python BCrypt library before being stored in the MongoDB database along with user information.

If you don't know what SaveYour is, SaveYour is an organizational, productive application that contains weekly to-do’s, calendars, agendas, notes, etc. into one tool. Its target in particular is the college student; however, entreprenuers, professors, and busy individuals will find the tool useful as well! It supports modularized togglable windows that can be customized by other developers. There are certain macros for quick task management such as parsing highlighted text to add to one's weekly to-do module or to add to one's homework module. There is a button to quickly hide and unhide Saveyour as a reference to one's schedule in a glance. SaveYour is able to take ones tasks and look through one's weekly to-do in order to find an available time to assign those tasks to do.

By using the following instructions you can host your own server for the SaveYour client, although you will also have to modify the client source to direct it towards your server!

Note: Since the Server is written in Python, the binary and source files are the same.

1) Installation:
	a) First make sure that Python 2.7, the Python BCrypt library, and PyMongo 2.7 are installed on your server host.
		i) You can input "pip install bcrypt" in your system console to install BCrypt once python is installed.
		ii) To install Pymongo input "pip install pymongo==2.7"

	b) Install MongoDB and set it to run with a database named 'SaveYourDB' and a 'users' collection.
	
	b) Change the DATABASE_ADDRESS and DATABASE_PORT fields in FileManager.py to the address and port of your database server.
	
	c) Name your private key certificate for TLS connection 'server.pem' and place it in the SaveYourServer folder.  We did not include our server.pem file in this distribution as you should keep your private key secret, or else you're forfeiting all of the security of the TLS connection.
		i) If you do not have such a certificate, create one in Linux by inputting the command 
		openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

		Fill out the fields as directed by the console. Once this file has been created, move it to your SaveYourServer folder and open it up with a text editor. Copy the lines '-----BEGIN CERTIFICATE-----' through '-----END CERTIFICATE-----' into a new file called ServerCertificate.pem

		This ServerCertificate.pem must replace the one in the SaveYour client program's executable directory, since it is the certificate used to confirm the private key you created in server.pem when performing the secure TLS connection.

2) Running the Server:
	a) In your server console cd to the SaveYourServer directory and input "sudo nohup python ClientListener.py" to launch the server.

	That's it!  The server will run until killed even if you close your console.  If you only want the server to run while the console is open, omit the nohup command and instead input "sudo python ClientListener.py"

3) Known Issues:
	a) Incoming packets of size greater than 4096 bytes will be dropped.  This is very unlikely to ever be a practical issue, but if it is you can modify the line "MAX_INC_SIZE = 4096" in ClientListener.py to some greater value.

	b) There is a race condition when saving user data to the database.  In a future update we plan to start parsing incoming data and checking the "Last Modified" tag embedded in it in order to resolve this, but it is low priority for the moment as it is very unlikely that one user will be actively modifying their data in different ways at the same time.

4) Testing:
	a) There are two test suites included with the distribution: ServerTest.py and TestDB.py
		Both of these are Python Unit tests and can be run by inputting "python ServerTest.py" or "python TestDB.py" in your console, and they will automatically run the test suites on the server and database respectively and inform you of the results.