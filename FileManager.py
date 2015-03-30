from pymongo import MongoClient

usersMockup = {'Tommy':'pop', 'Brendan':'ih8slackbot', 'Nate':'kingProjectManager', 'Justin':'whyPop?', 'Terrence':'What?', 'John':'mongoDBisDaBest', 'Simran':'pyth0n'}

DATABASE_ADDRESS = 'ec2-54-173-26-10.compute-1.amazonaws.com'
#DATABASE_ADDRESS = 'localhost'
DATABASE_PORT = 27017
DATABASE_NAME = 'SaveYourDB'

def connectToDB():
	global client
	global db
	global users
	client = MongoClient()
	db = client[DATABASE_NAME]
	users = db.SaveYourDB


def getFieldMockup(username, field):
	""" MOCKUP FOR NOW"""
	if (field != 'password'):
		return 'ACCESS DENIED'

	try:
		return usersMockup[username]
	except KeyError:
		return 'NOT FOUND'

def getField(username, field):
	data = users.find_one({"usr": username},{field:True})
	if data == None:
		return None
	return data[field]

def setField(username, field, data):
	users.find_one_and_update({'usr': username}, {'$set': {field: data}})

def createUser(username, password):
	if (users.count({'usr': username} > 0):
		return False
	hashedPW = bcrypt.hashpw(newPassword, bcrypt.gensalt())
	users.insert_one({'usr': username})
	setField(username, 'pwd', hashedPW)
	setField(username, 'data','')
	return True

connectToDB()
