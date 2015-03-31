import ClientListener
import Login
import FileManager
import unittest

class testServer(unittest.TestCase):
	#In Visual Studio, create accounts with (username,password):
	#("Bob", "Builder")
	#("Barney", Dinosaur")
	#("BeAutY", " bEAsT")

	#test authenticateHashed
	def testAuthenticateHashed1(self):
		self.assertTrue(Login.authenticateHashed("Bob", "Builder"))

	def testAuthenticateHashed2(self):
		self.assertTrue(Login.authenticateHashed("Barney", "Dinosaur"))

	def testAuthenticateHashed3(self):
		self.assertFalse(Login.authenticateHashed("Bob ", "Marley"))

	def testAuthenticateHashed4(self):
		self.assertTrue(Login.authenticateHashed("BeAutY", " bEAsT"))

	def testAuthenticateHashed5(self):
		self.assertFalse(Login.authenticateHashed("Bob ", "Builder"))

	def testAuthenticateHashed6(self):
		self.assertFalse(Login.authenticateHashed(" Barney", "Dinosaur"))

	def testAuthenticateHashed7(self):
		self.assertFalse(Login.authenticateHashed("BeAutY", "bEAst"))

	#test newPassword
	def testNewPassword1(self):
		Login.newPassword("Bob", "Burden")
		self.assertFalse(Login.authenticateHashed("Bob", "Builder"))
		self.assertTrue(Login.authenticateHashed("Bob", "Burden"))

	def testNewPassword2(self):
		Login.newPassword("Barney", "Hippo")
		self.assertFalse(Login.authenticateHashed("Barney", "hippo"))
		self.assertTrue(Login.authenticateHashed("Barney", "Hippo"))

	def testNewPassword3(self):
		Login.newPassword("BeAutY", "  bEAsT")
		self.assertFalse(Login.authenticateHashed("BeAutY", " bEAsT"))
		self.assertTrue(Login.authenticateHashed("BeAutY", "  bEAsT"))

	#not sure how to test getConneciton(). We can use Visual Studio to check if it is sending back the right 
	#strings

	#not sure how to test startListening(). Since it prints out "NOW LISTENING" and "ACCEPTED CONNECTION", 
	#we can check in Visual Studio to see if it prints out the correct messages

	#test getField
	def testGetField1(self):
		self.assertEquals(FileManager.getField("Bob", "pwd"), "Burden")
		self.assertEquals(FileManager.getField("Barney", "pwd"), "Hippo")
		self.assertEquals(FileManager.getField("BeAutY", "pwd"), "  bEAsT")

	def testGetField2(self):
		self.assertEquals(FileManager.getField("Bob", "usr"), "Bob")
		self.assertEquals(FileManager.getField("Barney", "usr"), "Barney")
		self.assertEquals(FileManager.getField("BeAutY", "usr"), "BeAutY")

	def testGetField3(self):
		self.assertEquals(FileManager.getField("Bob", "data"), "")
		self.assertEquals(FileManager.getField("Barney", "data"), "")
		self.assertEquals(FileManager.getField("BeAutY", "data"), "")

	#test setFeild
	def testSetField1(self):
		FileManager.setField("Bob", "pwd", "NotBuilder")
		self.assertEquals(Login.authenticateHashed("Bob", "NotBuilder"))

	def testSetField2(self):
		FileManager.setField("Barney", "pwd", "Spider")
		self.assertEquals(Login.authenticateHashed("Barney", "Spider"))

	def testSetField3(self):
		FileManager.setField("BeAutY", "pwd", "Sleeping")
		self.assertEquals(Login.authenticateHashed("BeAutY", "Sleeping"))

	def testSetField4(self):
		FileManager.setField("Bob", "usr", "Eric")
		self.assertEquals(Login.authenticateHashed("Eric", "NotBuilder"))

	def testSetFeild5(self):
		FileManager.setField("Barney", "usr", "Marcus")
		self.assertEquals(Login.authenticateHashed("Marcus", "Spider"))

	def testSetField6(self):
		FileManager.setField("BeAutY", "usr", "Sleeping")
		self.assertEquals(Login.authenticateHashed("Sleeping", "Sleeping"))

	#test setting data and getting data
	def testBothFields1(self):
		FileManager.setField("Eric", "data", "the happy snowman")
		self.assertEquals(FileManager.getField("Eric", "data"), "the happy snowman")

	def testBothFields2(self):
		FileManager.setField("Marcus", "data", "the frosty snowman")
		self.assertEquals(FileManager.getField("Marcus", "data"), "the frosty snowman")

	def testBothFields3(self):
		FileManager.setField("Sleeping", "data", "the melting snowman")
		self.assertEquals(FileManager.getField("Sleeping", "data"), "the melting snowman")
	
	#test New fields
	def testNewfields1(self):
		FileManager.setField("Eric", "Condition", "Living")
		self.assertEquals(FileManager.getField("Eric", "Condition"), "Living")

	def testNewfields2(self):
		FileManager.setField("Marcus", "Condition", "Frozen")
		self.assertEquals(FileManager.getField("Marcus", "Condition"), "Frozen")

	def testNewfields3(self):
		FileManager.setField("Sleeping", "Condition", "Dying")
		self.assertEquals(FileManager.getField("Sleeping", "Condition"), "Dying")

	#createUser and connectToDB may be database related functions that should be tested in database testing

unittest.main()