#!/bin/env python
'makeTextFile.py -- create a text file'

import os
ls=os.linesep

#get filename:
while True:
	fname=raw_input("please input the file name:\n")
	if os.path.exists(fname):
		print("ERROR: '%s' already exists\n" % fname)
	else:
		break

#get file content
all =[]
print("\nEnter file content('.' to quit)")

#loop input
while True:
	entry=raw_input('>')
	if entry=='.':
		break
	else:
		all.append(entry)

#write into file
fobj=open(fname,'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print("Done")
