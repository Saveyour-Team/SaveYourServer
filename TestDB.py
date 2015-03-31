import FileManager
import unittest

class TestFileManager(unittest.TestCase):
	def setUp(self):
		global username
		global password
		username = 'TestUser\n\r"'+"'a'print text"
		password = "\aa\\\n\r\t\b'" + '"print username'
		FileManager.createUser(username , password)

  	def tearDown(self):
  		FileManager.removeUser(username)

  	def test_set_get_delete_field():
  		data = 'this\n\r\t\r\a\bis"data' + "'print data"
  		pwd = '""""""""""newpassword""' + "''''''''''\\\\\n"
  		FileManager.setField(username, 'data', data)
  		FileManager.setField(username, 'pwd', pwd)

  		data2 = FileManager.getField(username, 'data')
  		assertEquals(data, data2, 'Pulled data does not match set data!')

  		pwd2 = FileManager.getField(username, 'pwd')
  		assertEquals(pwd, pwd2, 'Pulled password does not match set password!')

  		notthere = FileManager.getField(username, 'balloons')
  		assertIsNone(notthere, 'Error: pulled nonexistant data!')

  		newField = 'apples\nand&&"cake'
  		FileManager.setField(username, newField)
  		newField2 = FileManager.getField(username, newField)
  		assertEquals(newField, newField2,'Pulled data does not match set data! For trickily formatted string.')

  		FileManager.deleteField(username, newField)
  		notthereagain = FileManager.getField(username, newField)
  		assertIsNone(notthereagain, 'Failed to delete field.')
   	

	def test_create_remove_user():

		name = randint(0, sys.maxint)
		name = 'testUser'+name
		pwd = "a'testpass\r\n" + 'more\t\b\\"testing'
		result = FileManager.createUser(name, pwd)
		assertTrue(result, 'Failed to add user!')

		result = FileManager.createUser(name, pwd)
		assertFalse(result, 'Improperly added a user with the same name as an existing user!')

		FileManager.removeUser(name)
		result = FileManager.createUser(name, pwd)
		assertTrue(result, 'Failed to remove and readd a user!')

		result1 = FileManager.removeUser(name)
		result2 = FileManager.removeUser(name)


if __name__ == '__main__':
    unittest.main()