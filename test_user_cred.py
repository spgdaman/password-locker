import unittest
from user_cred_classes import Users, Credentials


class TestUsers(unittest.TestCase):
	"""
	Test class that defines test cases for the Users behaviour
	
	Args:
		unittest.TestCase: Class from the unittest module to create unit tests
	"""
	
	def setUp(self):
		"""
			#Function creates a new user object
		"""
		self.new_user = Users("Simon","Gatheru","W3w3n!mkenya")
		
	def test_init(self):
		"""
		#test_init test case to test if the object is the initialized properly
		"""
		
		self.assertEqual(self.new_user.first,"Simon")
		self.assertEqual(self.new_user.last,"Gatheru")
		self.assertEqual(self.new_user.password,"W3w3n!mkenya")
		
	def test_save_user(self):
		"""
		#test_save_user test case to test if the object is saved
		"""
		
		self.new_user.create_user()
		self.assertEqual(len(Users.user_info),1)
		
	def tearDown(self):
		"""
		#Function to reinitialize back to square one
		"""
		Users.user_info = []


	
class TestCredentials(unittest.TestCase):
	"""
		Test class that defines test cases for the Credentials behaviour
	
		Args:
			unittest.TestCase: Class from the unittest module to create unit tests
	"""

	def test_auth_check(self):
		"""
		test_auth_check test case to test if the user provided correct information
		"""
		self.new_user = Users("Simon","Gatheru","W3w3n!mkenya")
		self.new_user.create_user()
		another_user = Users("Twende","Kazi","mkenya")
		another_user.create_user()
		
		for cred in Users.user_info:
			if cred.first == another_user.first and cred.password == another_user.password:
				identity = another_user.first
		return identity
		
		self.assertEqual(identity, Credentials.user_check(another_user.first,another_user.password))
		
	def test_setup(self):
		"""
		test_setUp to create a new Credentials object to begin tests
		"""
		
		self.new_cred = Credentials("Simon","SPG","Instagram","W3w3n!mkenya")
	
	def test_init(self):
		"""
		test_init to check if the Credentials objects are initialized correctly
		"""
		self.new_cred = Credentials("Simon","SPG","Instagram","W3w3n!mkenya")
		self.assertEqual(self.new_cred.name, "Simon")
		self.assertEqual(self.new_cred.username, "SPG")
		self.assertEqual(self.new_cred.platform, "Instagram")
		self.assertEqual(self.new_cred.pwd, "W3w3n!mkenya")
		

		
		
		
if __name__ == '__main__':
	unittest.main()