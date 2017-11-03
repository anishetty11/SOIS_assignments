#!/bin/sh

############################################################
#
#Program to download kernel
#
############################################################
current=`uname -r`

page=`cat index.html`

# scrap the table containing version details
re="stable:</([^/]*)"
if [[ $page =~ $re ]]
	then
	temp_match=${BASH_REMATCH[1]}
	re1="strong>(.*)<"
fi

# extract the newest version from the table
if [[ $temp_match =~ $re1 ]]
		then
		updated=${BASH_REMATCH[1]}
		echo $updated
fi



# check if the available versio is newer than current version
flag=0
check_version()
{
	# compare the versions as well as sub versions
	while [ $# -gt 0 ]
	do
		current_v=`echo "$current" | cut -f$1 -d. `
		update_v=`echo "$updated" | cut -f$1 -d. `
		shift
		if [ $update_v -gt $current_v ]
			then
			echo "Available version is newer that existing version"
			flag=1
		fi
		
	done
}
check_version 1 2 

# if newer versio not found
if [ $flag -eq 0 ]
then
 	echo " New version not found"
	exit
fi

# if newer version found, scrap the download link and download
re="$temp_match(.*)"
echo 
if [[ $page =~ $re ]]
	then
	temp_match2=${BASH_REMATCH[1]}
fi
re="href=\"([^\"]*)"
echo 
if [[ $temp_match2 =~ $re ]]
	then
	link=${BASH_REMATCH[1]}
fi

wget $link 


