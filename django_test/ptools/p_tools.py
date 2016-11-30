# coding=utf-8
'''
Created on 2016��11��25��
@author: pangt
'''

import traceback 

class Test_Print :
    def __init__(self, name, age):
        self.name = name
        self.age = age

def print_obj(obj):
    if None is obj :
        return "None"
    
    res = str(obj.__class__) + " ["
    L_attrs = dir(obj)
    for t in L_attrs:
        if None is t :
            continue
        if str(t).endswith("__") :
            continue
        try :
            tmp = getattr(obj, t);
            if None is tmp :
                tmp = "None"
            res += t + " = " + str(tmp) + ","
        except :
            pass
#             print "print Err : " , str(t) , ":", obj 
#             traceback.print_exc()
    end_pos = len(res) - 1 
    res = res[0:end_pos]
    res += "]"
    return res
    
if "__main__" == __name__ :
    p = Test_Print('a', 18)
    p.sex = 'male'
    print "p = " , print_obj(p)
    # print "p = " , print_obj(188)
