#!/bin/sh

############################################################
#
#Program to check last access
#
############################################################

echo "Enter the name of the file"
read fname

# check if file exists
if [ -f $fname ]
	then 
	#echo "File exists"
	# if file exists print the last access date
	ls -l | grep "$fname" | tr -s " " " " | cut -f6,7,8 -d" "
	exit
fi

echo "File doesn't exist"
