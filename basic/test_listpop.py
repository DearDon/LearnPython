#########################################################################
# File Name: test_listpop.py
# Introduction:
# 	This program is to
# History:
# 	Created Time: 2016-09-20
# Author: ddeng 	E-mail: dongping.deng@asml.com
#########################################################################

alist=[1,3,5,2,6]
print alist
print "alist, ", alist.pop()
print "alist, ", alist.pop(1)
print alist
while alist:
    print alist.pop(0)
