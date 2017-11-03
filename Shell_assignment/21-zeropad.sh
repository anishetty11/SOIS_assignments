#!/bin/sh

############################################################
#
#Program to pad zeroes to beginning of filename
############################################################

echo "Enter the name of the file"
read fname

# if the given name is a file, pad zero
if [ -f $fname ]
	then 
	#echo "File exists"

	# split out filename and extension, and
	# append zero to beginning of filename
	extension=`echo $fname | cut -f2 -d "."`
	fname=`echo $fname | cut -f1 -d "."`
	echo $extension
	cp $fname.$extension 0$fname.$extension
	exit
fi

echo "File doesn't exist"
