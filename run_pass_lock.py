from user_cred_classes import Users, Credentials

def create_user(first,last,pwd):
	'''
	Creates a new user account
	'''
	user_mpya = Users(first,last,pwd)

def register_user(user):
	'''
	Saves the created user's account 
	'''
	Users.create_user(user)
	
def user_check(first,pwd):
	'''
	Does an authorization check prior to creating any credentials
	'''
	return Credentials.user_check(first,pwd)

def create_cred(name,username,platform,pwd):
	'''
	Creates credentials to be saved
	'''
	create_instance = Credentials(name,username,platform,pwd)
	return create_instance
	
def save_cred(cred):
	'''
	Saves created credentials
	'''
	Credentials.save_cred(cred)

def password_gen():
	'''
	Generates a random password_gen
	'''
	random = Credentials.password_gen
	return random

def show_cred(username):
	'''
	Shows credentials saved
	'''
	return Credentials.show_credentials(username)
	
	
	
	
	
	
	
	
	