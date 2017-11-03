#!/bin/sh

############################################################
#
#Program to install apache server locally
#
############################################################

sudo apt-get update
sudo apt-get install apache2
# set up the server
echo "ServerName 127.0.0.1" | cat > /etc/apache2/apache2.conf
sudo apache2ctl configtest
#restart apache service
sudo systemctl restart apache2
sudo ufw allow in "Apache Full"
