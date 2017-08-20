#using test.txt as input file, and storing output in output.txt

def main():
	with open("test.txt") as file:
		data=file.read()	
	print ('characters=',len(data),"words=",len(data.split()),'lines=',len(data.split('\n')))
	with open("output.txt",'w') as file:
		file.write("Characters:%s"%str(len(data)))
		file.write("Words:%s"%str(len(data.split())))
		file.write("Lines:%s"%str(len(data.split(' '))))
		
		
		
main()
		