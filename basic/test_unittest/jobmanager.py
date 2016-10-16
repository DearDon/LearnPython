#########################################################################
# File Name: jobmanager.py
# Introduction:
# 	This program is to manage multi-process job
# History:
# 	Created Time: 2016-09-19
# Author: ddeng 	E-mail: dongping.deng@asml.com
#########################################################################
import subprocess
import multiprocessing
from datetime import datetime

import jobmanager_unittest
import run_unittest

def execute_cmd(cmd): #this function can't be inside class as Pool don't support
    '''use to open a new subprocess to execute external command,
    usage: call_subprocess(cmdstr)'''
    starttime=datetime.now()
    subprocess.call(cmd, shell=True)
    endtime=datetime.now()
    runtime=endtime-starttime
    print "[INFO]: "+cmd+" finished, start at "+str(starttime)+", end at "+str(endtime)+", runtime is "+str(runtime)
    return {cmd:{"starttime":starttime, "endtime":endtime, "runtime":runtime}}

class JobManager(object):
    '''class to manage job with constant processes, singleton for all, max_processes_num is decide at first instance'''

    def __init__(self, max_processes_num=4):
        ''' init a Pool with defined processes, 4 is by default'''
        self.max_processes_num = max_processes_num
        self.pool=multiprocessing.Pool(processes=self.max_processes_num)
        self.cmd_list=[]
        self.result=[]

    def add_task(self, cmd):
        ''' add task, input is str '''
        self.cmd_list.append(cmd)

    def add_tasks(self, cmd_list):
        ''' add tasks, input is list '''
        self.cmd_list.extend(cmd_list)

    def get_tasks(self):
        ''' get all current tasks '''
        return self.cmd_list

    def sort_tasks(self, runtimefile):
        ''' sort tasks depend on last run time from runtimefile, long runtime task will arrange first'''
        raise NotImplementedError

    def submit_tasks(self):
        ''' sumbit tasks to pool with constant num processes '''
        while self.cmd_list:
            cmd=self.cmd_list.pop(0)
            self.result.append(self.pool.apply_async(execute_cmd, (cmd, )))
        return 0

    def block(self):
        ''' block main process till all tasks are done. This need to close pool, and can't add more task after close'''
        self.pool.close()
        self.pool.join()

    def get_result(self):
        ''' get results of subprocesses, better block before it for pretty results'''
        results=[]
        for result in self.result:
            results.append(result.get())
        return results

if __name__ == "__main__":
    #unittest
    test_suite=jobmanager_unittest.fullSuite()
    test_result=run_unittest.runTestSuite(test_suite)
    run_unittest.showResult(test_result)
