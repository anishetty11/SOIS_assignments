####################################################################
#
# Program to parse the files files "countries.xml" and "sample.json"
#
###################################################################


import xml.etree.ElementTree as ET
import json


#function to parse an xml file "countries.xml"
def xml_parse():

	#create a parsable object, and extract the root
	tree = ET.parse('countries.xml')
	root = tree.getroot()

	# displaying the headings 
	print ("\n","Country".ljust(13),"Rank".ljust(5),"Year".ljust(5),"gdppc".ljust(6),
		"Neighbors".ljust(13),"Neighbor Direction".ljust(15),"\n")

	# for each "country" tag in root
	for country in root.findall('country'):
		
		# assign the values to rank,year,gdppc,neightbor o corresponfing variables
		rank = country.find('rank').text
		year = country.find('year').text
		gdppc = country.find('gdppc').text
		neighbor = country.find('neighbor').attrib
		
		# print the country name and variables
		print (country.attrib['name'].ljust(13),end=' ')
		print (rank.ljust(5),year.ljust(5),gdppc.ljust(6),
			neighbor['name'].ljust(15),neighbor['direction'].ljust(2),'\n')


#function to parse json file "sample.json"

def json_parse():

	# copy he contents of file to "parsed_json"
	with open('sample.json') as data:

		#json.load() return a dictionary 
		parsed_json = json.load(data)

	#display the contents of "parsed_json"
	print (json.dumps(parsed_json,indent=4))



print ('***********XML******************')
xml_parse()
print('************json***************')
json_parse()
