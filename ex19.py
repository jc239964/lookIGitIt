def cheeseAndCrackers(cheeseCount, boxesOfCrackers): 
    # function is defined, args are defined (cheese/crackers)
    print "You have %d cheeses!" % cheeseCount 
    # prints the amount of cheese
    print "You have %d boxes of crackers." % boxesOfCrackers
    # prints the crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    # prints the line and then a line break is added for the next fn

print "We can give the functions numbers directly:"
cheeseAndCrackers(20, 30) # 2 numbers are fed directly

print "Or, we can use variables from our script."
amountCheese = 10 # defines variables
amountCrackers = 50

cheeseAndCrackers(amountCheese, amountCrackers) # 2 variables are used as args

print "We can even do math inside too:"
cheeseAndCrackers(10 + 6, 20 + 5) # args are directly defined

print "And we can combine the two, variables and math."

cheeseAndCrackers(amountCheese + 20, amountCrackers + 100)

# testing for raw input

partyCheese = int(raw_input("How much cheese would YOU bring to the party? "))
partyCrackers = int(raw_input("And how many crackers would you bring? "))

cheeseAndCrackers(partyCheese, partyCrackers) 
# uses raw_input for args
