#Opens connection to file to be read.
import os
script_dir = os.path.dirname(__file__)
rel_path = "data/Countries-Currencies.csv"
abs_file_path = os.path.join(script_dir, rel_path)

p = open(abs_file_path, 'r')
list =[]
#Loops through file line by line
for line in p:
	if(line[0] != ','):
		list.append('\n',)
		list.append(line.replace('\n',''))
	if(line[0] == ','):
		list.append(line.replace('\n',''))	
str = ''.join(list)
#Because I append a newline to every line not containing ',' I 
#remove the very first line from the string with str[1:]
str = str[1:]
print(str)
#Opens connection to file to be written too.	
script_dir = os.path.dirname(__file__)
rel_path = "data/Clean-Countries-Currencies.csv"
abs_file_path = os.path.join(script_dir, rel_path)
newfile = open(abs_file_path,'w')
newfile.write(str)
#Is it better to write line by line or all at once? Size of data?
p.close()
newfile.close()
input('press enter to close')