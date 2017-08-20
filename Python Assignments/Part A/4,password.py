import getpass

def main():
	print ("Enter username")
	username=input()
	print ("Enter password")
	password=getpass.getpass()
	print ("Username : ",username,"password:",password)
	
main()