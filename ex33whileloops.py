pi = 3.14
eatpi = []

"""
while pi < 20:
	
	print "Pi right now is %f." % pi
	
#	eatpi.append(range(1, 21))
	eatpi.append(pi)
	
	pi = pi + 2
	print "We're eating pi now: ", eatpi
	print "Pi is currently: %f" % pi

print "Looks like we're ready to eat pi."
print eatpi

print '-' * 10
print "It's time to remove our eaten pi..."

while pi > 3.14:
	print "Pi right now is %f." % pi
 
#       eatpi.append(range(1, 21))
        eatpi.pop()
 
        pi = pi - 2.5
        print "We're removing pi now: ", eatpi
        print "Pi is currently: %f" % pi

print "Looks like we're ready to eat pi."
print eatpi
"""

# the above idea as a for loop
"""
for i in range(0, 6):
	print "i is currently: %d. Adding to list \'eatpi\'" % i
	eatpi.append(i)

print eatpi	
"""

# the above idea as a function that takes input

numlist = []
def whilefunc(low, high, inc):
	while low < high:
		print "Num is %d" % low
		numlist.append(low)
		low = low + inc
		print "Num is currently %d, and numlist is: " % (low), numlist	

whilefunc(0, 15, 2)






