formatter = "%r %r %r %r" # defines variable formatter, with 4 raw input 
			  # formatters

print formatter % (1, 2, 3, 4) # prints var formatter with these assigned values
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could tpe up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# first, defined variable, then inputed values into the variable (since the 
# variable was a bunch of %r raw inputs)

