# use argv to get the script's name and user input
from sys import argv

script, filename = argv

# defines variable 'txt' with the open function and 
# the filename which user inputs via argv
txt = open(filename)

# prints the name of the file, then uses the read function to 
# print it to the command line
print "Here's your file %r:" % filename
print txt.read()

# user inputs the file name, via the raw input function
# the variable "file_again" is defined with user input from 
# raw_input function
print "Type the filename again:"
file_again = raw_input("> ")

# defines txt_again variable with the open function filled with the 
# file_again variable
txt_again = open(file_again)

# reads the file, which was inputted before
print txt_again.read()

txt.close()
txt_again.close()

