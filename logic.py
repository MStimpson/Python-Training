class Logic(object):
	def __init__(self,results):
		self.results = results
		self.resultList=[]
	def returnList(self):
		return self.resultList
	def setList(self,resultList):
		self.resultList = resultList
	
	def listResult(self):
		resultList=[]
		i=0
		for items in self.results:
			x=0
			l=[]
			for item in self.results[i]:
				l.append(self.results[i][x])
				x+=1
			resultList.append(l)
			i+=1
		self.setList(resultList)
	
	def makeCategories(self,round):
		temp=''
		display='********************************\n'
		for item in self.resultList:
			if(item[4] == round):
				if(temp != item[3]):
					i=30
					display+='*'
					display+=item[3]
					while i > len(item[3]):
						display+=' '
						i-=1
					display+='*\n'
				temp = item[3]
		display+='********************************\n'
		return display
	
	def showCat(self,round):
		temp=''
		categories=[]
		for item in self.resultList:
			if(item[4] == round):
				if(temp != item[3]):
					categories.append(item[3])
		return categories
	
	def showValue(self, user_input):
		display='\n**********\n'
		for item in self.resultList:
			if(user_input.upper() == item[3]):
				i=6
				display+='* $'
				display+=str(item[1])
				while i > len(str(item[1])):
					display+=' '
					i-=1
				display+='*\n'
		display+='**********\n\n'
		return display
	
	def removeQuestion(self,index):
		rs = self.returnList()
		rs.pop(index)
		self.setList(rs)
	def findIndex(self,item):
		x=0
		while x<len(self.resultList):
			i=0
			while i<len(self.resultList[x]):
				if(item == self.resultList[x][i]):
					self.removeQuestion(x)
					break
				i+=1
			x+=1				
