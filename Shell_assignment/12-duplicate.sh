#!/bin/sh

############################################################
#
# Program to check and delete duplicate files
#
# The path where the files have to checked for duplicates
# is prompoted by the user, and then all the copies are deleted
# from other directories as well
#
############################################################

updatedb

remove()
{
	# get all the paths where the duplicates are present
	paths=`locate $i`
	for line in $paths
		do 
			echo $line : $2
			echo
			# delete all files except the one in pwd
			if [[ $line =~ "$2"*  ]]
				then
					echo "Duplicates for $line  have been delted"			 
			else
				#echo "Going to be deleted: $line "
				rm -r $line
			fi
		done
}





echo "Enter the path wehre duplicates are to be checked"

read path

# for each file in specified path, check if there are duplictes
# in other folders
cd $path
for i in *
do
	no=`locate $i | wc -l`
	if [ $no -gt 1 ]
		then
			# if there are duo=plicates,remove them
			remove $i `pwd`
		fi
done
