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