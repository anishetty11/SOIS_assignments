##########################################################
#
# Program to check whether VMs are up, and find their IP
# address if they are up
#
# Assumption: Virtual Machines are set up in VirtualBox
# 			  
#########################################################


import sys
import subprocess
import re
import logging


# creating a logger object
logging.basicConfig(level=logging.WARNING)
logger=logging.getLogger()

# vm details stores all the details of the running VMs
# vm_names extract and saves the names of Running VMs
vm_details=''
vm_names=[]

def running():
	''' Saves the names of running VMs in "vm_names" '''

	global vm_details,vm_names

	# call a shell script to get details of all the running VMs
	# and save it in "config"
	config=subprocess.Popen('vboxmanage list vms --long | \
	 grep -e "State:" -e "Name:" | grep -B1 "running"',\
	 shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

	# copy the contents of config (converting to string) to vm_details
	for i in config.stdout.readlines():
		vm_details+=str(i)+'\n'

	# if vm_details is blank, no VMs are running
	if vm_details=='':
		print ("None of the VMs are running")
		sys.exit(0)

	# else, extract names and save it is vm_names
	for i in vm_details.split('\n'):
		if (i[2:6]=="Name"):
			logger.debug(i.split())
			vm_names.append((i.split()[1])[0:-3])

	logger.info(vm_names)


############################################

def ips():
	''' Program to get the IP addresses of all running VMs'''


	vm_ips=[]

	# for each Running VMs ( saved in vm_names), store details 
	# details in "config"
	for i in vm_names:
		config=subprocess.Popen('vboxmanage guestproperty enumerate %s | grep "IP" '%i,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		# convert to string and copy contents to vm_ips
		for i in config.stdout.readlines():
			vm_ips.append(i)

	# for each running VM, print VM name and VM ip address
	for i in range(len(vm_ips)):
		print ("\n\nVM Name:",vm_names[i],"\nIP addr:",re.findall('(...\..*\....)'[1:-2],str(vm_ips[i])[2:-2]))
		logger.debug(str(vm_ips[i])[2:-2])

running()
ips()
