import subprocess
import time

def test_mulcommand():
    '''test run multi comand in on process bash'''
    #cmd=' '.join(['shopt', '-s', 'extglob;', 'cp', 'test1/!(b)', 'test'])
    cmds='''
    shopt -s extglob
    cp test1/!(b) test2
    '''
    #subprocess.call(cmd, shell=True, executable="/bin/bash")
    #cp test1/!(b) test2/
    process=subprocess.Popen('/bin/bash',stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out,err=process.communicate(cmds)

def test_block():
    '''test block different between subprocess.Popen and subprocess.call'''
    subprocess.Popen(["ping","-c","5","www.baidu.com"])
    subprocess.call(["ping","-c","5","www.google.com"])
    print("parent process")

def test_Popen():
    '''test how to use Popen'''
    cmd=' '.join(["ping","-c","5","www.google.com"])
    subprocess.Popen(cmd, shell=True)
    print cmd

def test_wait():
    '''test Popen.wait()-- main procsss wait for all subprocess finish'''
    children=[]
    for i in range(0,5):
        if i==0:
            cmd=' '.join(["echo","quick!!"])
            child=subprocess.Popen(cmd, shell=True)
        else:
            cmd=' '.join(["ping","-c","1","www.google.com"])
            child=subprocess.Popen(cmd, shell=True)
        children.append(child)
    print("sleep start")
    time.sleep(15)
    print("sleep end")
    for child in children:
        print(child)
        child.wait() #what if child finish before this? will it cause a null point problem? No, that won't cause any problems in python(test by sleep)
    print("parent process finished")

    if 0: #comment following code
        cmd=' '.join(["ping","-c","1","www.google.com"])
        child=subprocess.Popen(cmd, shell=True)
        child.wait()
        print("parent process finished")


if __name__ == "__main__":
   # test_block()
   # test_Popen()
    test_wait()
