#!/bin/sh

############################################################
#
#Program to check the size of directory
#
############################################################


echo "Enter the path"
read path
echo "The size of the directory is ":
cd $path

# to check size of direcotrys
du -hs $path
