#coding=utf-8

'''
Created on 2016年11月17日

@author: pangt
'''
from test.test_threading_local import target
import sys


if __name__ == "__main__" :
    source_acctid = sys.argv[1]
    target_accid = sys.argv[2]
    money = sys.argv[3]
    print source_acctid , target_accid , money
