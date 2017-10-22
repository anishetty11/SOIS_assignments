#############################################################################
#
# Program to generate xml file
#
# Assumption: User input is taken as dictioanry, and then converted to XML
#
##########################################################################


import logging

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


def create_xml(dicts,no_of_tabs):
	''' Generate the xml file for the given library '''
	no_of_tabs+=1
	global xml_string
	
	# get all the keys from the dictionary
	keys=dicts.keys()

	# for each of the keys append the xml data in a string call "xml_string"
	for i in keys:

		# append the opening tag
		xml_string+=('%s<%s>\n'%(tabs*no_of_tabs,i))
		logger.info("XMLSTRING1:%s"%xml_string)

		# if the value corresponding to the tag is a dictionary
		# i.e. another tag needs to be enclosed in this tag
		# recursively call the function "create_xml"
		if isinstance(dicts[i],dict):
			logger.info('here')
			create_xml(dicts[i],no_of_tabs)

		# if not a dictionary
		else:
			logger.info('i'+tabs*no_of_tabs+'i')
			logger.info("No of tabs:%s"%no_of_tabs)

			# append the value (data) o
			xml_string+=tabs*no_of_tabs+'\t'+(str(dicts[i]))+'\n'
			logger.info("XMLSTRING2:%s"%xml_string)

		# finally append the closing tag
		xml_string+=('%s<%s\\>\n'%(tabs*no_of_tabs,i))
		logger.info("XMLSTRING3:%s"%xml_string)


xml_string=''
tabs='\n'


dicts=create_dicts()
create_xml(dicts,-1)
print (xml_string)

# write the string in a file "ex.xml"
with open("ex.xml",'w') as xm:
	xm.write(xml_string)
