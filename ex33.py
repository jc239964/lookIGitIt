# i = 0
numbers = [ ]

#def whilefunc(x, y):
#	i = 0
#	while i < x:
#		print "At the top i is %d" % i 
#		numbers.append(i)
#	
#		i += y
#		print "Numbers now: ", numbers
#		print "At the bottom i is %d" % i
#		
#		while i < 6:
#			print "i is between 0 and 6"
#			print "i is %d, so we'll increment an additional 1" % i	
#			i += 1	
#
#	print "The numbers: "
#
#	for num in numbers:
#		print num
#
#whilefunc(15, 2)

for i in range(0, 6):
	print "At the top, i is %d" % i
	numbers.append(i)

#	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
