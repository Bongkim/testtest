class Calculator:                       
	def __init__(self, first, second):    
		self.first = first
		self.second = second
	def setdata(self, first, second):
		self.first = first
		self.second = second
	def add(self):                        
		result = self.first + self.second
		return result


class NewCalculator(Calculator):
	def setdata(self, first, second):
		self.first = first + 1
		self.second = second + 2
	def sub(self, first, second):
		result = self.first - self.second
		return result