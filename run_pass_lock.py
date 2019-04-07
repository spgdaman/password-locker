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
	
def main():
	print("Welcome to the password locker app")
	while True:
		print("................"*10)
		print("Please use the following short codes to interface with the app\n ln - Login\n rg - Register\n lo - Logout")
		user_input = input("Enter input here: ")
		
		if user_input == 'rg':
			print("Enter your registration details below")
			fname = input("Enter your first name: ")
			lname = input("Enter your last name: ")
			pwd = input("Enter your desired password: ")
			register_user(create_user(fname, lname, pwd))
			print(f"Your account is registered as follows, {fname} {lname} and {pwd} is your password")
			
		#elif 









	
	
		elif user_input == 'lo':
			print("Thank you for using password locker")
			break
			
		else:
			print("Kindly enter a correct input!")
	
if __name__ == '__main__':
	main()		