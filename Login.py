import FileManager



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

