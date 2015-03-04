usersMockup = {'Tommy':'poop', 'Brendan':'ih8slackbot', 'Nate':'kingProjectManager', 'Justin':'whyPoop?', 'Terrence':'What?', 'John':'mongoDBisDaBest', 'Simran':'pyth0n'}

def getField(username, field):
	""" MOCKUP FOR NOW"""
	if (field != 'password'):
		return 'ACCESS DENIED'

	try:
		return usersMockup[username]
	except KeyError:
		return 'NOT FOUND'