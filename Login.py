import FileManager



def getFieldMockup(username, field):
	return ''


def hash(pw):
	return pw


def authenticate(username, password):
	passwordHash = hash(password)
	localpw = FileManager.getField(username, 'password')
	if localpw == None:
		return False
	return localpw == passwordHash

