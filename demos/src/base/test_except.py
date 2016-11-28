#coding=utf-8

'''
Created on 2016年11月23日

@author: pangt
'''
from _csv import Error

try :
    res = 3 / 0
except Error, e :
    print e
finally:
    print "finally"
    
print "a"