from sys import argv
from os.path import exists
# importing "exists()" function into script from os.path

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# creates variable in_file that opens the original file (imported from
# cmd line) and reads it. the file automatically closes after the line.

in_file = open(from_file).read()
# indata = in_file.read()

print "The input file is %d bytes long." % len(in_file)
# len function determines the length of a file that was previously read.

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print "Alright, all done."

out_file.close()
# in_file.close()

