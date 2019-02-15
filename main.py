from myclass import Car 
from myboxiterator import MyBoxIterator
from mybox import MyBox

car1 = Car()   

car2 = Car()
types = "sedan" 
label = "nissan"
color = "red"
car2.change_inf(types, label, color) 

car3 = Car()
types = "crossover" 
label = "volvo"
color = "white"
car3.change_inf(types, label, color) 

car4 = Car()
types = "crossover" 
label = "jaguar"
color = "white"
car4.change_inf(types, label, color) 

my_box = MyBox()
my_box.add(car1) 
my_box.add(car2) 
my_box.add(car3) 
my_box.add(car4) 
print("The contents of my_box after adding 4 machines to it:")
it = my_box.iterator()
for elem in it:
	elem.disp_inf()
	print("")
	
my_box.remove(car1)
print("Size of my_box after removing one machine:")
print(my_box.len())
print("Contents of my_box after removing one machine:")
it = my_box.iterator()
for elem in it:
	elem.disp_inf()
	print("")
	
print("Check if there is a recently deleted machine in the container:")
print(my_box.contains(car1))



 
