####################################################################################
#
# Program to install and create a VM 
#
# Assumptions: VirtualBox and Vagrant are installed
#              Same VM shoudn't be provisioned before
#
##################################################################################### 

import subprocess
import os




def get_vm_name():
	''' Get the Name of the Vagrant box to be installed '''

	# ask the user to enter the choice of OS for VM
	choice=input("Select the VM to be installed\n1:Ubuntu\n2:Windows \
		\n3:CentOS\n4:Others: ")
	choice=int(choice)

	# get the corresponding name of Vagrant Box
	if choice==1:
		vm_name='ubuntu/trusty64'
	elif choice==2:
		vm_name='senglin/win-10-enterprise-vs2015community'
	elif choice==3:
		vm_name='centos7'

	# if user wants to specify the name of vagrant box himself
	else:
		vm_name=input("Enter the Vagrant Box to be installed: ")

	# return the name of vagrant box
	return vm_name


	

def create_vm():

	# get the name of vagrant box
	vm_name=get_vm_name()

	# create and enter the directory where the Vagrantfile will be stored
	os.makedirs("%s"%vm_name)
	os.chdir("%s"%vm_name)

	#call a shell script to initalize and create the VM
	create=subprocess.Popen(" vagrant init %s "%(vm_name), \
		shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	create=subprocess.Popen(" vagrant up ", \
		shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)	

	# display the progress
	for i in create.stdout.readlines():
		print (i)

create_vm()
