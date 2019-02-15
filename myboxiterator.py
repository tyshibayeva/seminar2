class MyBoxIterator:
	def __iter__(self):
		return self
		
	def __init__(self, myList):
		self.myList = myList
		self.counter = 0
		
	def __next__(self):
		if self.counter < len(self.myList):
			it = self.myList[self.counter]
			self.counter += 1
			return it
		else:
			raise StopIteration
	
