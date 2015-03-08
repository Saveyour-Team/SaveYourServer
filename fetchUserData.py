import pymongo

DATABASE_ADDRESS = 'localhost'
DATABASE_PORT = 27017
DATABASE_NAME = 'saveryour'

class fetchUserData:

    def __init__(self, usrname, pwd):
        self.u = usrname;
        self.p = pwd;
        conn = pymongo.mongoClient();
        collection = db.SaveYourDB
        print('Connecting to saveyour db')

    def userExists(self.u):
        result = collection.find_one({usr:self.u})
        return result

    def getPassword(self.u):
        result  = collection.find_one({usr:self.u})
        return result

    def getData(self.u):
        result  = collection.find_one({usr:self.u})
        return result

    def createNewUser(self.u, self.p):
        newUser = {usr:self.u, pwd:self.p,data:""}
        collection.insert(newUser)


