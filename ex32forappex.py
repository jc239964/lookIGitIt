# this is an example for lists, appending, and for loops

veggies = ["tomato", "cabbage", "eggplant", "broccoli"]

yummy = []
for v in veggies:
	print "Adding %s to the yummy list." % v
	yummy.append(v)

print "Let's see what we have in each list."

print '-' * 10
print "Veggies"
print veggies

print '-' * 10
print "Yummy List"
print yummy

print "Below is further practice on for-loops."
print '-' * 10
print "Let's use the range function to append a list."

numbers = []
for n in range(0, 10): 
	print "Adding %d to the numbers list." % n 
	numbers.append(n) 

print "Let's see what the numbers list looks like now."
print numbers
print "Remember that the range function begins at 0 and ends in before the number placed in the range function!"
print "i.e. range(0, 10) is the number range from 0 to 9, not 0 to 10."
print '-' * 10

""" 
variables in for loops can basically be anything. 
you don't need to worry about naming them, just make sure that
they are consistent in the loop
"""
