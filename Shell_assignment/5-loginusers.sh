#!/bin/sh

############################################################
#
#Program to list the loggen in users
#
############################################################


# get the username of logged in users
who -u | cut --fields=1 --delimiter=' '
