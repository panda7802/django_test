# coding=utf-8
import math
from __builtin__ import reduce
def pow2(d) :
    res = pow(d, 2);
    return res

# 平方和
def pfh(a, b, f):
    res = f(a) + f(b)
    return res

func = pow2
res = pfh(4, 9, math.sqrt)
print res


def format_name(s):
    return s[0].upper() + s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])

print "------reduce"
def prod(x, y):
    res = x * y
    return res

print reduce(prod, [2, 3, 4, 5, 6])

print "1~100平方根是整数的"
lAll = range(1, 101)
def isSqrtInteger(x):
    res = False
    tmp = math.sqrt(x)
    iTmp = int(tmp)
    if tmp == iTmp :
        res = True
    return res
print filter(isSqrtInteger  , lAll)
        
print "比较"
def cmp_ignore_case(s1, s2):
    x = s1.lower()
    y = s2.lower()
    if x > y:
        return 1
    if x < y:
        return -1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

print  "返回乘积函数"
def getFuncMu(L):
    
    def f(L1):
        res = 1;
        for t in L1:
            res *= t;
        return res
    
    return f

L = [1, 2, 3, 4]
# L = []
f = getFuncMu(L)

print f(L)
    
    
    
print "闭包"
def count():
    fs = []
    L = [] ;
    for i in range(1, 4):
        def f(i):
            def g():
                print "call " + g.__name__ 
                return i * i
            return g
        fs.append(f(i))
    
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()


print "匿名函数"
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
myabs = lambda x:-x if x < 0 else x 
print myabs(-4)

print "简化"
def is_not_empty(s):
    return s and len(s.strip()) > 0
# print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
print filter(lambda s : s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
