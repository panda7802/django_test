# coding=utf-8

def isZhishu(i):
    res = True
    tmp = 2
    while True :
        if i <= tmp :
            break
        if (0 == i % tmp) :
            res = False
            break
        else :
            tmp += 1
    return res

i = 1
res = 0
while True :
    i += 1
    
    if i >= 100 :
        break;
    
    #判断是否是质数
    flag = isZhishu(i)
    
    if (True == flag) :
        res += i

print "res : " , res
    
    


