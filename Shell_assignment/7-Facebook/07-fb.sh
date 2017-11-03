

wget www.facebook.com 


cat index.html |grep -o 'https:[^"]*png' | tr -s " " " ">images.txt

while read line
do
	wget $line
done < images.txt
