import argparse
import os
from subprocess import call

text_editor='subl'

parser=argparse.ArgumentParser()
group=parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c",help="Create skelton for C program")
group.add_argument("-s",help="Create skelton for Shell program")
args=parser.parse_args()

if args.c:
	if os.path.exists('%s.c'%args.c):
		print ("FIle already exists")
	else:
		with open("%s.c"%args.c,'w') as cf:
			with open("c_skull.c") as cs:
				data=cs.read()
			cf.write(data)
			os.system("%s %s.c"%(text_editor,args.c))


if args.s:
	if os.path.exists('%s.sh'%args.s):
		print ("FIle already exists")
	else:
		with open("%s.sh"%args.s,'w') as cf:
			with open("shell_skull.sh") as cs:
				data=cs.read()
			cf.write(data)
			os.system("%s %s.sh"%(text_editor,args.s))
	