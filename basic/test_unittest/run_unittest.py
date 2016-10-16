#########################################################################
# File Name: run_unittest.py
# Introduction:
# 	This program is to run all unittest for whole project
# History:
# 	Created Time: 2016-10-15
# Author: Don 	E-mail: dpdeng@whu.edu.cn
#########################################################################
import unittest
import jobmanager_unittest
import argparse as arg

def getArgs():
    parser = arg.ArgumentParser(description='run unittest for the project')
    parser.add_argument("-m", "--mode", type=str, choices=["part","full"], help="set mode to run full testcase suite or part of it", default="full")
    return parser.parse_args()

def getTestSuite(mode):
    test_suite=unittest.TestSuite()
    if mode=="full":
        test_suite.addTest(jobmanager_unittest.fullSuite())
        #print "cases number: "+str(test_suite.countTestCases())
    else:
        test_suite.addTest(jobmanager_unittest.partSuite())
        #print "cases number: "+str(test_suite.countTestCases())
    return test_suite

def runTestSuite(test_suite):
    result=unittest.TestResult()
    test_suite.run(result)
    return result

def showResult(test_result):
    print "--------------------------UnitTest Report---------------------------"
    print "Run cases: "+str(test_result.testsRun)
    if test_result.failures:
        print "Fail cases: "+str(len(test_result.failures))
        for i in range(0,len(test_result.failures)):
            for j in range(0,len(test_result.failures[i])):
                print test_result.failures[i][j]
    if test_result.errors:
        print "Error cases: "+str(len(test_result.errors))
        for i in range(0,len(test_result.errors)):
            for j in range(0,len(test_result.errors[i])):
                print test_result.errors[i][j]
    print "Pass test: "+str(test_result.wasSuccessful())

if __name__=='__main__':
    args=getArgs()
    mode=args.mode

    test_suite=getTestSuite(mode)
    test_result=runTestSuite(test_suite)
    showResult(test_result)
