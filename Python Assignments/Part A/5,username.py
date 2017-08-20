import getpass

def main():
	dict={}
	i=0
	while(i<5):
		print ("Enter username")
		username=input()
#checking whether the username already exists
		if username in dict.keys():
			print ("Username already exists")
			continue
		print ("Enter password")
		password=getpass.getpass()
		#print ("Username : ",username,"password:",password)
		dict[username]=password
		i=i+1
	print (dict)
	
main()