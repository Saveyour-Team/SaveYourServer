from pymongo import MongoClient

usersMockup = {'Tommy':'poop', 'Brendan':'ih8slackbot', 'Nate':'kingProjectManager', 'Justin':'whyPoop?', 'Terrence':'What?', 'John':'mongoDBisDaBest', 'Simran':'pyth0n'}


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
	return data[field]

def getUserDoc(username):
	return None


