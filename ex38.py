ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not ten things in that list. Let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

# Below are some of the things you can do to lists.

print stuff[1]

print stuff[-1]

print stuff.pop()

print ' '.join(stuff)

print "#".join(stuff[3:5])


