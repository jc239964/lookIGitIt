from sys import argv

script, userName, action = argv
prompt = "Please answer after colon: "

print "Hello %s, I'm the %s script." % (userName, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % userName
likes = raw_input(prompt)

print "Where do you live %s?" % userName
lives = raw_input(prompt)

print "What kind of computer do you have?"
comp = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, not sure where that is!
And you have an %r computer. Noice!
With this, we conclude the %r %s.
""" % (likes, lives, comp, action, script)
