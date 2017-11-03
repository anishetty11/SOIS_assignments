#!/bin/sh

############################################################
#
# Program to rename all files 
#
############################################################

echo "Enter the path where files have to be renamed"
read path

cd $path


# for all files in specified path, ask user for a new name
# and rename the file
for i in *
do 
	extension=` echo $i | cut -f2 -d . `
	echo "Enter the new filename for $i"
	read temp_name
	mv $i $temp_name.$extension
done






