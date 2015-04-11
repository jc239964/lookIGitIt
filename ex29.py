people = 20
cats = 30
dogs = 15

if people < cats: 
	print "Too many cats! The world is doomed!"

if people > cats: 
	print "Not many cats! The world is saved!"

if people < dogs: 
	print "The world is drooled on!"

if people > dogs: 
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs: 
	print "People are less than or equal to dogs."

if people == dogs: 
	print "People are dogs."

cats -= 5

if people == cats:
	print "Well, looks like the cat menace is avoided."

# def catsFucked():
#	cats = cats - 1
#	people = 1
#	if people != cats:
#		print "People are not equal to cats."
#		print "There are only", cats, "cats left."
#		cats -= 1
#		catsFucked()

# catsFucked()
