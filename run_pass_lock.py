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
	
