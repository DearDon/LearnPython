#########################################################################
# File Name: test_copy.py
# Purpose:
#	This file is to test shutil.copys
# History:
#	Created Time: 2016-12-11
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
import shutil

def main():
    srcfolder='./test_folder/SRC'
    src='./test_folder/SRC/a'
    dst='./test_folder/DST/a'
    dstfolder='./test_folder/DST/'
    # shutil.copy(src, dstfolder)
    # shutil.copy2(src, dst)
    # shutil.copyfile(src, dst)
    shutil.copytree(srcfolder, dstfolder)
    # shutil.copymode(srcfolder, dstfolder)

if __name__ == '__main__':
    main()
