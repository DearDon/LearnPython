#!/bin/env python
#########################################################################
# File Name: test_function.py
# Introduction:
# 	This program is to
# History:
# 	Created Time: 2016-09-20
# Author: ddeng 	E-mail: dongping.deng@asml.com
#########################################################################

def f(x,y=1,z=5):
    print x
    print y
    print z
    print x+y+z

if __name__ == '__main__':
    f(1,2)
    f(1,z=2)
    f(1)
