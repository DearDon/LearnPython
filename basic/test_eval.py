from math import *

user_func = raw_input("input a function: y= ")

for x in range(1,10):
    print "x = ", x, ", y=", eval(user_func)
