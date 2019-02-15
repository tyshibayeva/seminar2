class Car:
	def __init__(self):    
		self.types = "liftback"
		self.label = "skoda"
		self.color = "black"
	
	def disp_inf(self):
		print ("types", self.types)
		print ("label", self.label)
		print ("color", self.color)
             
	def change_inf(self, type_new, label_new, color_new):    
		self.types = type_new
		self.label = label_new
		self.color = color_new
		

          
