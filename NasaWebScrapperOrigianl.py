from bs4 import BeautifulSoup
import urllib.request
import re
import os
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
os.system('cls')

url = 'https://apod.nasa.gov/apod/'
page = 'archivepix.html'
response = urllib.request.urlopen(url+page)
html = response.read()

soup = BeautifulSoup(html, 'lxml').findAll('a')
#user_input = input('Enter date. Format YYMMDD\n')

while True:
	first_date = input('Enter first date. Format YYMMDD\n')
	if(is_number(first_date)):
		break
while True:
	second_date = input('Enter second date. Format YYMMDD\n')
	if is_number(second_date):
		break
		
counter=1
for i in soup:
	if('href="ap' in str(i)):
		x = re.search('href=\"(.*?)\"', str(i)).group(1)
		#ap1704 = Astronomy Picture 2017 April
		#if(str(user_input) in str(x)):
		if(int(first_date) <= int(x[2:-5]) and int(second_date) >= int(x[2:-5])):
			response = urllib.request.urlopen(url+x)
			html = response.read()
			subSoup = BeautifulSoup(html, 'lxml').findAll('img')
			for line in subSoup:
				if('src' in str(line)):
					subX = re.search('src=\"(.*?)\"',str(line)).group(1)
					fname = str(counter)+'.jpg'
					urllib.request.urlretrieve(url+subX,fname)		
					print('Date: ',x[2:-5],' File: ',str(fname),' downloaded.')
					counter+=1