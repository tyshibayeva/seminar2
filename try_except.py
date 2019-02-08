my_dictionary = {"t":1, "a":2, "b":3}

try:
	value = my_dictionary["D"]
except KeyError:
	print("Hahaha")

try:
	g=open ("no-file")
except IOError:
	print ("ok")


try: 
	400/0
except ArithmeticError:
	print("uvi, no net")

	
