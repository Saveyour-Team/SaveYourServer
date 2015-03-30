import FileManager
import bcrypt



def getFieldMockup(username, field):
	return ''


def hash(pw):
	return pw


def authenticate(username, password):
	passwordHash = hash(password)
	serversidepw = FileManager.getField(username, 'pwd')
	if serversidepw == None:
		return False
	return serversidepw == passwordHash


def authenticateHashed(username, password):
	serversidepw = FileManager.getField(username, 'pwd')
	print serversidepw
	if serversidepw == None:
		return False
	return bcrypt.hashpw(password, serversidepw)

def newPassword(username, newPassword):
	 hashedPW = bcrypt.hashpw(newPassword, bcrypt.gensalt())
	 FileManager.setField(username, 'pwd', hashedPW)
