########################################################
#
# Program to perform CRUD operation on a table named 
# "registration" in the database "student"
#
#######################################################


import mysql.connector
from mysql.connector import Error
import logging

# create the logging object
logging.basicConfig(level=logging.WARNING)
logger=logging.getLogger()


def connect():
	''' To connect to the database '''

	# conn to the database
	conn = mysql.connector.connect(host='localhost',
									database='student',
									user='root',
									password='wireless')
	if conn.is_connected():
		print('Connected to database')

	# ask user for a choice of operations
	choice=int(input("Enter your choice:\n1.Create\n2.Retrive\n3.Update\n4.Insert\n5.Delete\n6.Exit: "))
	while(1):
		if choice==1:
			create(conn)
		elif choice==2:
			retrieve(conn)
		elif choice==3:
			update(conn)
		elif choice==4:
			insert(conn)
		elif choice==5:
			delete(conn)
		else:
			conn.close()
			break
		choice=int(input("\nEnter your choice:\n1.Create\n2.Retrive\n3.Update\n4.Insert\n5.Delete: "))



def retrieve(conn):
	''' To get all the details in the table '''

	#get the cursor object from the conn object
	cursor=conn.cursor()

	# create the query
	query="select * from registration"

	# execute the query and print
	cursor.execute(query)
	print (cursor.fetchall())


def update(conn):
	''' To update the values in the table '''
	# get the cursor object
	cursor=conn.cursor()

	# Ask the user for the Reg No whose data is to be changed
	# and the changes to be made
	choice='y'
	while(choice=='y'):
		reg_no=input("Enter reg.no whose value is to be updated: ")
		value_to_be_updated=input("Enter the value to be updated , Fname,Lname or DOB")
		new_value=input("Enter the new value")

		# write the query as per the values as given by the user
		if value_to_be_updated=='Fname':
			query='update registration set Fname = %s where Reg_no= %s'
		elif value_to_be_updated=="Lname":
			query='update registration set Lname = %s where Reg_no= %s'
		elif value_to_be_updated=="DOB":
			query='update registration set DOB = %s where Reg_no= %s'
		else:
			print("\nYou have entred an invalid option\n")

		
		args=(new_value,reg_no)
		logger.info(query%args)
		

		# execute the query and commit it
		try:
			cursor.execute(query,args)
			conn.commit()
			print ("\nValues updated")
			choice=input("\nUpdate more values? y: ")
		except Error as e:
			print (e)



def delete(conn):
	''' To delete the table '''

	# get the cursor object
	cursor=conn.cursor()

	# write a query to delete the table
	query="drop table registration"
	logger.info(query)

	# execute the query and commit it
	try:
		cursor=conn.cursor()
		logger.debug("1")
		cursor.execute(query)
		conn.commit()
		print("\nTable deleted\n")
	except Error as e:
		print (e)
	finally:
		cursor.close()
		#conn.close()



def insert(conn):
	''' To insert the values '''

	# get the cursor object
	cursor=conn.cursor()

	# get the details of values to be added from the user
	choice='y'
	while(choice=='y'):
		reg_no,fname,lname,dob=input("Enter Reg-no, fname, lname and dob: ").split()
		
		try:
			# write a query based on the values given by the user
			query="insert into registration values(%s,%s,%s,%s)"
			args=(reg_no,fname,lname,dob)

			cursor.execute(query,args)
			conn.commit()
			print ("\nValues inserted\n")
			choice=input("Add more values? y: ")
		except Error as e:
			print (e)
		




def create(conn):
	''' Create the table '''

	try:

		# write the query
		query="create table registration (Reg_no varchar(10),Fname varchar(10),Lname varchar(20),DOB varchar(20), PRIMARY KEY(Reg_no))"
		logger.info(query)

		# execute and commit the changes
		cursor=conn.cursor()
		cursor.execute(query)
		print("Table created")
		conn.commit()
		
	except Error as e:
		print (e)
	finally:
		cursor.close()
		#conn.close()




connect()