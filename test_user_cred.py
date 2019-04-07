import unittest
from user_cred_classes import Users, Credentials

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
		
	def tearDown(self):
		'''
		Function to reinitialize back to square one
		'''
		Users.user_info = []
		
	def test_auth_check(self):
		'''
		test_auth_check test case to test if the user provided correct information
		'''
		
		self.new_user.create_user()
		self.another_user = Users("Twende","Kazi","mkenya")
		self.another_user.create_user()
		
		for cred in Users.user_info:
			if cred.first == self.new_user.first and cred.password == self.new_user.password:
				identity = self.new_user.first
		return identity
		
		self.assertEqual(identity, Credentials.user_check(self.new_user.first,self.new_user.password))
		
		
		
if __name__ == '__main__':
	unittest.main()