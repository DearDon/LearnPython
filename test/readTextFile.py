#!/bin/env python
'readTextFile -- read the content of a file'

#get filename
fname=raw_input("please input the file name:\n")

try:
	fobj=open(fname,'r')
except IOError, e:
	print "*** file open error:", e
else:
	for line in fobj:
		print line,
	fobj.close()

print "test",
print "test"
