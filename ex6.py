# defines variable x, sets 10 as formatter 
x = "There are %d types of people." % 10

# defines variables binary and do_not
binary = "binary"
do_not = "don't"

# defines variable y and sets variables binary and do_not as formatters
y = "Those who know %s and those who %s." % (binary, do_not)

# prints variables x and y on 2 lines
print x
print y

# prints 2 lines using variables x and y as formatters
print "I said: %r." % x
print "I also said: '%s'." % y

# sets variable 'hilarious' as a boolean, and variable 'joke_evaluation' as string with a formatter.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r."

# prints joke_evaluation with hilarious as the formatter.
print joke_evaluation % hilarious

# defines two variables, w and e
w = "This is the let side of..."
e = "a string with a right side."

# combines w and e on the same line
print w + e

# formatter practice in a string, inputting strings to the formatters
print "I want %s, %s, %s, and %s." % ("milk", "eggs", "bread", "soup")


