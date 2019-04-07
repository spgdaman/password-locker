import unittest
from user_cred_classes import Users

class TestPasswordLocker(unittest.TestCase):
	"""
	Test class that defines test cases for the password_locker behaviour
	
	Args:
		unittest.TestCase: Class from the unittest module to create unit tests
	"""
	
	def setUp(self):
		'''
		Function creates a new user object
		'''
		self.new_user = Users("Simon","Gatheru","W3w3n!mkenya")
		
	def test_init(self):
		'''
		test_init test case to test if the object is the initialized properly
		'''
		
		self.assertEqual(self.new_user.first,"Simon")
		self.assertEqual(self.new_user.last,"Gatheru")
		self.assertEqual(self.new_user.password,"W3w3n!mkenya")
		
	def test_save_user(self):
		'''
		test_save_user test case to test if the object is saved
		'''
		
		self.new_user.create_user()
		self.assertEqual(len(Users.user_info),1)
		
		
		
		
		
if __name__ == '__main__':
	unittest.main()