#!/bin/sh

############################################################
#
#Program to install NS3
#
############################################################

# installing dependencies
sudo apt-get install gcc g++ python
sudo apt-get install  python-dev
sudo apt-get install qt4-dev-tools
sudo apt-get install mercurial
sudo apt-get install cmake libc6-dev libc6-dev-i386 g++-multilib
sudo  apt-get install gdb valgrind
sudo apt-get install gsl-bin libgsl0-dev libgsl0ldbl
sudo apt-get install flex bison libfl-dev
sudo apt-get install tcpdump
sudo apt-get install sqlite sqlite3 libsqlite3-dev
sudo apt-get install libxml2 libxml2-dev
sudo apt-get install libgtk2.0-0 libgtk2.0-dev
sudo apt-get install vtun lxc
sudo apt-get install uncrustify
sudo  apt-get install doxygen graphviz imagemagick
sudo  apt-get install texlive texlive-extra-utils texlive-latex-extra texlive-font-utils dvipng
sudo apt-get install python-sphinx dia
sudo apt-get install python-pygraphviz python-kiwi python-pygoocanvas libgoocanvas-dev
sudo apt-get install libboost-signals-dev libboost-filesystem-dev
sudo apt-get install openmpi-bin openmpi-common openmpi-doc libopenmpi-dev


#Create a directory for downloading files

mkdir NS3repo
cd NS3repo

#Clone the files to this directory

hg clone http://code.nsnam.org/ns-3-allinone

# run the python code to downloaad

 cd ns-3-allinone
 ./download.py

# run the python code to build
 
./build.py

#Configure it using waf.

cd ns-3-dev
CXXFLAGS="-O3" ./waf configure 
./waf -d optimized configure; ./waf 
./waf --enable-examples configure 
./waf --enable-tests configure

#check installation by running python test file

 ./test.py
