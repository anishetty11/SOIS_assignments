#!/bin/sh

############################################################
#
#Program to set the path vairbale
#
############################################################


echo "Enter the Path manually, or choose pwd? 1/2"
read choice

# if path has to be taken manually
if [ $choice -eq 1 ]
	then
	echo "Enter the path"
	read path

# if pwd has to be taken as path
else
	path=`pwd`
fi

echo $path
path=$PATH:$path

# export path variable
export path


# add the path to the bashrc file
cat /etc/bash.bashrc | sed "s@PATH=\(.*\)@PATH=$path@g" | cat > /etc/bash.bashrc

