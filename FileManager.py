import pymongo

usersMockup = {'Tommy':'poop', 'Brendan':'ih8slackbot', 'Nate':'kingProjectManager', 'Justin':'whyPoop?', 'Terrence':'What?', 'John':'mongoDBisDaBest', 'Simran':'pyth0n'}
DATABASE_ADDRESS = 'localhost'
DATABASE_PORT = 27017
DATABASE_NAME = 'saveryour-users'

##Not sure if these should be set to None to start out or not.
client = None
db = None
users = None



def connectToDB():
	global client = MongoClient(DATABASE_ADDRESS, DATABASE_PORT)
	global db = client[DATABASE_NAME]
	global users = db.users


def getField(username, field):
	data = users.find_one({"user": username},{field:True})
	return data



def getFieldMockup(username, field):
	""" MOCKUP FOR NOW"""
	if (field != 'password'):
		return 'ACCESS DENIED'

	try:
		return usersMockup[username]
	except KeyError:
		return None