#########################################################################
# File Name: jobmanager_unittest.py
# Introduction:
# 	This program is to do unittest for jobmanager
# History:
# 	Created Time: 2016-10-15
# Author: ddeng 	E-mail: dongping.deng@asml.com
#########################################################################
import unittest
import jobmanager

class JobManager_Unittest(unittest.TestCase):

    def test_setTasks(self):
        jm = jobmanager.JobManager(max_processes_num=6)

        jm.add_task("echo 1")
        jm.add_tasks(["echo 2", "echo 3"])
        self.assertEqual(jm.get_tasks(), ["echo 1", "echo 2", "echo 3"])

        jm.submit_tasks()
        self.assertEqual(jm.get_tasks(), [])

        jm.add_task("echo 4")
        self.assertEqual(jm.get_tasks(), ["echo 4"])

    def test_submitTasks(self):
        jm = jobmanager.JobManager(max_processes_num=6)

        jm.add_task("echo 1")
        self.assertEqual(jm.submit_tasks(), 0)

        jm.add_tasks(["echo 2", "echo 3"])
        self.assertEqual(jm.submit_tasks(), 0)

    def test_getResult(self):
        jm = jobmanager.JobManager(max_processes_num=6)
        tasks=[]

        jm.add_task("echo 0")
        for task in jm.get_tasks():
            tasks.append(task)
        jm.submit_tasks()

        jm.add_tasks(["echo 2", "echo 3"])
        for task in jm.get_tasks():
            tasks.append(task)

        jm.submit_tasks()
        jm.block()

        result_dic={}#merge all result dic to one dic
        map(lambda x: result_dic.update(x), [result for result in jm.get_result()])

        self.assertEqual(result_dic.keys().sort(), tasks.sort())#sort need as order is random

def fullSuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(JobManager_Unittest))
    return suite

def partSuite():
    suite=unittest.TestSuite()
    suite.addTest(JobManager_Unittest("test_getResult"))
    return suite

if __name__ == '__main__':
    unittest.main()

