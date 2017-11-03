#!/bin/sh

############################################################
#
#Program to copy specific file types
#
############################################################

echo " Enter the path from where the files are to be copied"
read  path

echo " Enter the file types which are to be copied"
read filetype

echo " Enter the path where to file have to be copied"
read dest_path

cd $path

# for each file in the given path,
# check if it matches the given extensio, and
# then move
for i in *
	do
		temp_file_extn=`echo $i | cut -f2 -d.`
		if [ $temp_file_extn = $filetype ]
			then
				mv $i $dest_path
			fi
	done
