import string
import random

class Users:

	'''
		Class that contains the users methods and attributes
	'''
	
	user_info = []
	
	def __init__(self,first,last,password):
		"""
			Information needed to create a password saving object
		"""
		self.first = first
		self.last = last
		self.password = password
	
	def create_user(self):
		"""
			Create an instance of a new user
		"""
		
		self.user_info.append(self)

class Credentials(Users):
	"""
		Class that holds credential information and associated methods eg. add, remove and view creadentials
	"""
	
	credentials_info = []
	user_cred_info = []
	
	@classmethod
	def user_check(cls,first,password):
		"""
			Checks for matching credentials in user_info
		"""
		
		for cred in user_info:
			if cred.first == first and cred.password == password:
				identity = cred.first
		return identity
	
	def __init__(self,name,username,platform,password):
		"""
			Initialize new Credentials object
		"""
		
		self.name = name
		self.username = username
		self.platform = platform
		self.password = password
		
	
	
	