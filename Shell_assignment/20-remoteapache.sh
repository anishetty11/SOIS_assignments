#!/bin/sh

############################################################
#
#Program to install apache server remotely
#
############################################################

# connect to remote server through SSH
echo "Enter the ip address where apache server has to be installed"
read ip
# execute 19-apache.sh remotely
ssh -t $ip 'sudo bash  '< 19-apache.sh


# contents of 19-apache.sh
#sudo apt-get update
#sudo apt-get install apache2
#echo "ServerName 127.0.0.1"
#sudo apache2ctl configtest
#sudo systemctl restart apache2
#sudo ufw allow in "Apache Full"
