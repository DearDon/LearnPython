#########################################################################
# File Name: typeCheckAndTransfer.py
# Purpose:
# 	This program is to test data type and transfer data type
# History:
# 	Created Time: Mon 20 Jun 2016 10:03:43 AM CST
# Author: Don	E-mail: dpdeng@whu.edu.cn
#########################################################################
#!/bin/python
import types

##################Transfer
#string to integer
num=int('10')
print(num)

#string to float
flo=float("10.2")
print(flo)

#others to string
string=str("2.5")
print(string)

#####################Type check
num=10
flo=10.1
if type(num) is types.IntType:
	print(str(num)+" is a integer)")
print(type(flo))
