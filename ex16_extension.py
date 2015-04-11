from sys import argv

script, filename = argv

txt = open(filename)

print "Here is the file %r: \n" % filename
print txt.read()

txt.close
