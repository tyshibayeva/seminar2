from myclass import Car
from myboxiterator import MyBoxIterator

class MyBox:
	def __init__(self, my_container = None):
		if my_container == None:
			self.my_container = []
		elif type(my_container) is list:
			if len(my_container) > 0:
				fl = 0
				for item in my_container:
					if type(item) is not Car:
						print("Check inside the container for an object of the wrong type.")
						fl = 1
						break
				if fl == 0:
					self.my_container = my_container
			else:
				self.my_container = my_container
	
	
	def len(self):
		return len(self.my_container)
	
	
	def add(self, obj):
		if type(obj) is Car:
			if obj in self.my_container:
				print("The object is already contained in the container.")
			else:
				self.my_container.append(obj)
		else:
			print("An object of this type cannot be added to the container.")
	
			
	def remove(self, obj):
		if obj in self.my_container:
			self.my_container.remove(obj)
		else:
			print("This object is not in the container.")
			
	def contains(self, obj):
		if obj in self.my_container:
			return True
		return False
		
	def iterator(self):
		return MyBoxIterator(self.my_container)
