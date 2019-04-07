from user_cred_classes import Users, Credentials

def create_user(first,last,pwd):
	'''
	Creates a new user account
	'''
	user_mpya = Users(first,last,pwd)
	return user_mpya

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
		print("................\n"*10)
		print("Please use the following short codes to interface with the app\n ln - Login\n rg - Register\n lo - Logout")
		user_input = input("Enter input here: ")
		
		if user_input == 'rg':
			print("Enter your registration details below")
			fname = input("Enter your first name: ")
			lname = input("Enter your last name: ")
			pwd = input("Enter your desired password: ")
			register_user(create_user(fname, lname, pwd))
			print(f"Your account is registered as follows, {fname} {lname} and {pwd} is your password")
			
		elif user_input == 'ln':
			print("Enter your username and password below to log in to your account")
			username = input("Enter your username here:		")
			password = input("Enter your password here:		")
			if user_check(username, password) == username:
				print(f"You have sucessfully logged in {username}!")
				
				while True:
					print("................\n"*10)
					print("Please use the following short codes to interact with the app")
					user_input = input("sn - Save new credentials\n snp - Save new credentials with own password\n sc - Show credentials")
					
					if user_input == 'sn':
						print("Enter the account details you want saved below")
						username = input("Enter your username:		")
						platform = input("Enter the platform:		")
						pwd = input("Enter your password:		")
						create_cred(fname,username,platform,pwd)
						print(f"Your credentials for site: {platform}, with username: {username} and password: {pwd} has been saved!")







	
	
		elif user_input == 'lo':
			print("Thank you for using password locker")
			break
			
		else:
			print("Kindly enter a correct input!")
	
if __name__ == '__main__':
	main()		