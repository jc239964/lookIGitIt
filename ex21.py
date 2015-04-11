def add(a, b): # defining function add, 2 args to be passed (a, b)
	print "ADDING %d + %d" % (a, b) # print statement, pass numbers 
	return a + b # return value from equation.

def subtract(a, b): # def function subtract, 2 args passed (a, b)
	print "Subtracting %d - %d" % (a, b)
	return a - b 

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b): 
	print "Dividing %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(20, 4)
height = subtract(60, -8)
weight = multiply(77, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

what2 = divide(iq, multiply(weight, subtract(height, add(age, 20))))

print "Look, another potential function to figure out. The output is: ", what2


