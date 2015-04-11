people = 16
cars = 15
trucks = 17

# determines whether there are more cars than people
if cars > people: 
	print "We should take the cars."
elif cars < people: 
	print "We should not take the cars."
else: 
	print "We can't decide."

# determines whether there are more trucks than cars
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else: 
	print "We still can't decide."

# determines whether there are more people than trucks
if people > trucks: 
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

# determines whether there are more trucks than people, and more people
# than cars
if people < trucks and cars < people:
	print "There are less people than trucks and less cars than people."
elif people > trucks and cars > people:
	print "There are more people than trucks and more cars than people."
else:
	print "Wtf is going on!!!" 
