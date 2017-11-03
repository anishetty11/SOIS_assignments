#!/bin/sh

############################################################
#
#Program to rename .doc file to .docx
#
############################################################
echo " Enter the path where the files are to be renamed"
read  path

cd $path

# split the filename into its name and extension
# check if the extension is doc
for i in *
	do
		temp_file_name=`echo $i | cut -f1 -d.`
		temp_file_extn=`echo $i | cut -f2 -d.`
		if [ $temp_file_extn = "doc" ]
			then
				# rename to .docx
				mv $i $temp_file_name.${temp_file_extn}x
			fi
	done
