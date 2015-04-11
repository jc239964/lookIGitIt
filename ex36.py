from sys import exit

key = False

def start():
	print "THE GAME"
	print "Are you a bad enough dude to play? Enter START to begin."
	start = raw_input("> ")
	if "start" in start:
		story1()
	else:
		dead("Well, I guess you're not a bad enough dude.")

def dead(statement):
	print statement, "Isn't that too bad?"
	exit(0)

def back():
	print "You go back to the first room."
	print "Do you continue through the moldy door or the iron door?"
	room1()

def story1():
	print "In this dank, musty room, you find two doors." 
	print "One door is covered in mold, but should open easily."
	print "The other is an iron door with a small key hole." 
	print "What door do you try to open?"
	room1()	
	
def room1():
	door = raw_input("> ")
	if "mold" in door:
		room2()
	elif "iron" in door and key == False:
		print "You are unable to open the door."
	elif "iron" in door and key == True:
		print "The door unlocks and leads down a dark passageway."
		endroom()
	else:
		print "That doesn't work."

def room2():
	print "You enter a room built of old cobblestone."
	print "A crowd of small hobgoblins look up and ready their weapons!"
	print "What do you do?"
	action = raw_input("> ")
	if "fight" in action:
		print "You draw your sword and slice the goblins in half."
		chancekey()	
	elif "run" or "flee" in action:
		print "You run back to the first room and slam the door behind you."
		back()
	else:
		dead("The goblins cut you up, skewer you, and eat you for dinner.")

def chancekey():
	print "You see a small yet shiny object on the ground."
	print "It's a key! You pick it up and put it in your pocket."
	print "Maybe it will let you open that iron door..."
	key = True
	back()

def endroom():
	print "There is a small treasure chest in the center of the room."
	print "Do you try to open it? Yes or no."
	choice = raw_input("> ")
	if "yes" in choice:
		print "Your heart pounds as you open the treasure chest."
		

start()
