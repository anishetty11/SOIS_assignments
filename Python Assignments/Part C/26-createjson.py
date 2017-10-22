#############################################################################
#
# Program to generate xml file
#
# Assumption: User input is taken as dictioanry, and then converted to XML
#
##########################################################################


import logging
import json

# creating the logging object
logging.basicConfig(level=logging.WARNING)
logger=logging.getLogger()


print(" This is a program to create XML file\n Data will be saved as a dictionary \
	and then converted as an XML.\n Keys = Tags along with the attributes \n \
	 Values= Data to be enclosed in the tags\n")

dicts={}

def create_dicts():
	''' This program generates the dictionary '''

	temp={}
	while(1):
		# get the tag from the user
		key=input("Enter the key: ")

		# ask the user whether he wants to enclose another tag within this tag
		print("Do you want to enter a single value, or do you want you nest another tag within this tag S/D?: ")
		choice=input()

		# if another tag is not needed to be enclosed
		if choice=='S':
			value=input("Enter the value: ")

		# if another tag is to be enclosed within this tag
		else:
			value=create_dicts()

		# add the key and value pair to the dictionary
		temp[key]=value
		print ("Tag '%s' closed"%key)

		# ask the user if he wants to continue adding more tags
		# (not enclosed tags)
		cont=input("Add another key value pairs in this tag ? Y/N?: ")


		if cont=='N':
			break;
	return temp


def create_json(dicts):
	''' To generate json from a given dictionary '''

	json_string=json.dumps(dicts)
	return json_string
	
	






dicts=create_dicts()
json_string=create_json(dicts)
print (json_string)

# write the string in a file "ex.json"
with open("ex.json",'w') as xm:
	xm.write(json_string)
