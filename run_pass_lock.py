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

def password_gen(size):
	'''
	Generates a random password_gen
	'''
	random = Credentials.password_gen(size)
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
			print("Enter your username and password below to log in to your account\n*Your first name is your default username*")
			username = input("Enter your username here:		")
			password = input("Enter your password here:		")
			if user_check(username, password) == username:
				print(f"You have sucessfully logged in {username}!")
				
				while True:
					print("................\n"*10)
					print("Please use the following short codes to interact with the app")
					user_input = input("sn - Save new credentials\nsnp - Save new credentials with own password\n sc - Show credentials\n dc - Delete credentials\n ex - Exit")
					
					if user_input == 'sn':
						print("Enter the account details you want saved below")
						username = input("Enter your username:		")
						platform = input("Enter the platform:		")
						pwd = input("Enter your password:		")
						create_cred(fname,username,platform,pwd)
						print(f"Your credentials for site: {platform}, with username: {username} and password: {pwd} has been saved!")
					
					elif user_input == 'snp':
						print("Enter the account details you want saved below")
						username = input("Enter your username:		")
						platform = input("Enter the platform:		")
						len = input("Enter the length of your desired password in numbers:		")
						pwd = password_gen(int(len))
						create_cred(fname,username,platform,pwd)
						print(f"Your credentials for site: {platform}, with username: {username} and password: {pwd} has been saved!")
						
					elif user_input == 'sc':
						print("Your saved credentials are as below")
						show_cred(username)
						 
					elif user_input == 'dc':
						print("Enter the platform's name and username whose credentials you want deleted below")
						platform = input("Enter the name of the platform here:		")
						username = input("Enter the username here:			")
						show_cred(username)
						print("Your credentials have been deleted!")
						
					elif user_input == 'ex':
						print("Goodbye! come again!")
						break
	
		elif user_input == 'lo':
			print("Thank you for using password locker")
			break
			
		else:
			print("Kindly enter a correct input!")
	
if __name__ == '__main__':
	main()		