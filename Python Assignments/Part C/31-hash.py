#########################################################
#
# Progrm to maintain username and checksum of passwords
# and check the enter username and password if there is a match
#
##########################################################

import hashlib
import sys
import logging

# create a logger object
logging.basicConfig(level=logging.WARNING)
logger=logging.getLogger()


# dictionary containing username and thier passwords
#passwords are stored ash checksum calculate usinh sha256 hashing
password={'anish':'649f419b18d6d5b537ac87c71504b50867e3c8bdef87d5968963360742031075',
			'shetty':'d081ef1b4a1711069f5190d8894adaaa57e6fbefa5fb0a276017a6873a75afae'
		}


while(1):
	# store username in "user and chec if there is a match"
	user=input('Enter the username\n')

	# if there is a match, ask for password
	if user in password.keys():
		# sotre the password in "pswrd"
		pswrd=input('Ente the password\n')

		#check if the checksum of entered password is the same as
		#the one stored in the dictionary
		if hashlib.sha256(pswrd.encode('utf-8')).hexdigest()==password[user]:
			print ("login succesful")
			sys.exit(0)

		# if there passowrds aren't same
		else:
			logger.info("Password given:%s"%(hashlib.sha256(pswrd.encode('utf-8')).hexdigest()))
			logger.info("Sotred password:%s"%password[user])
			print ("Wrong password")

	#if username doesn't exist
	else:
		print("Username doesn't exist")