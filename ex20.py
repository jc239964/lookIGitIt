from sys import argv
script, inputFile = argv

# argv is imported from cmd line; file that will be used in functions

# defining functions
def printAll(f):
    print f.read() # reading the input (f) of the function

def rewind(f):
    f.seek(0) # moves to the beginning of the file (byte 0)

def printLine(lineCount, f):
    print lineCount, f.readline(), # comma is here to prevent extra \n's 

# f is the argument that is inputted to each function

currentFile = open(inputFile) # opens the inputFile (argv)

print "First let's print the whole file:\n"

printAll(currentFile) # runs the printAll function with currentFile as 
		      # the input

print "Now let's rewind! Kind of like a tape..."

rewind(currentFile) # the rewind function is defined above

print "Let's print three lines:"

currentLine = 1
printLine(currentLine, currentFile)

currentLine += 1 # this is synonomous the ++ in javascript, incrementing.
printLine(currentLine, currentFile)

currentLine += 1
printLine(currentLine, currentFile)


