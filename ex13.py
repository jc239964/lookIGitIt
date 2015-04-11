from sys import argv

script, first, second, third = argv # creates variables that are defined
				    # by cmd line input

print "The script is called:", script # the first variable is always the script's name

print "The first variable is:", first # prints input immediately after the script name on the command line

print "The second variable is:", second #

meep = raw_input("The third variable is: ") # asks for input, which defines var meep

print meep + " " + third # prints var meep, space, and the third input from the cmd line

