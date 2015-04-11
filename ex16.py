from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# user presses enter to cont or ctrl-c to cancel
raw_input("?")

# variable target is defined with open function, filename (input) and 
# the extra parameter w to truncate the file and open it in write mode
print "Opening the file..."
target = open(filename, 'w+')

# this is unnecessary but can be used if parameter 'a' is used in the 
# function above. that way the file is cleared before new input is added
# print "Truncating the file. Goodbye."
# target.truncate()

print "Now I'm going to ask you for three lines."

# asks user for input to write into file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")


# var target is called, file is written with input provided by user above
# each line variable has a line break after it to ensure each line is separated

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# closes the file
print "And finally, we close it."
target.close()

