
# this one is like your scripts with argv
def print_many(*args):
# tells python we are --def--ining a function named print_many
# the print_many function will accept arguments fed into it hence the *args
    arg1, arg2, arg3, arg4 = args 
    # defines what args will be passed into function
    print "arg1: %r, arg2: %r, arg3: %r, arg4: %r" % (arg1, arg2, arg3, arg4) 
	# prints the results of the function 

# ok, that *args is actually pointless, we can just do this
# unless you don't know how many args will be passed into function
def print_two_again(arg1, arg2):
	# defines arguments that will be passed in
	# i.e. arg1 and arg2 are the only args that can be passed in
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this takes no arguments
def print_none(): 
	print "I got nothin'."

print_many("Joe", "Celentano", "loves", "cheese.")
print_two_again("Poop", "Balls")
print_one("First!")
print_none()

