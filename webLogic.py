from bs4 import BeautifulSoup
import urllib.request
import re
import random
import time
class Logic(object):
	def __init__(self,baseurl):
		self.baseurl = str(baseurl)
		self.links = []
	def returnList(self):
		return self.links
	def appendLink(self,newLink):
			self.links.append(self.baseurl+str(newLink))
	def checkLink(self,newLink):
		if(self.baseurl+str(newLink) not in self.baseurl+str(self.links)):
			return True
		else:
			return False
	def webScrapper(self,url):
		response = urllib.request.urlopen(str(url))
		html = response.read()
		soup = BeautifulSoup(html,'lxml').findAll('a')
		for line in soup:
			#Being generic significantly increases run time and grabs alot of garbage.
			if('href="' in str(line) and '#' not in str(line) and 'user' not in str(line)):
				if('view' in str(line) or 'index' in str(line)):
					x = re.search('href=\"(.*?)\"', str(line)).group(1)
					#The site I'm using for testing will block you if you ping it to many times in a short period of time.
					if(self.checkLink(x)):
						self.appendLink(x)
						if('index' not in str(line)):
							print(self.baseurl + x)
							#######################################
							items = list(range(0, 57))
							i = 0
							l = len(items)
							# Initial call to print 0% progress
							self.printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
							for item in items:
								# Do stuff...
								time.sleep(random.uniform(0.01,0.05))
								# Update Progress Bar
								i += 1
								self.printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
							########################################	
						#time.sleep(random.uniform(.5,.9))
						self.webScrapper(self.baseurl + x)
						
	def printProgressBar (self,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
		"""
		Call in a loop to create terminal progress bar
		@params:
			iteration   - Required  : current iteration (Int)
			total       - Required  : total iterations (Int)
			prefix      - Optional  : prefix string (Str)
			suffix      - Optional  : suffix string (Str)
			decimals    - Optional  : positive number of decimals in percent complete (Int)
			length      - Optional  : character length of bar (Int)
			fill        - Optional  : bar fill character (Str)
		"""
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
		# Print New Line on Complete
		if iteration == total: 
			print()