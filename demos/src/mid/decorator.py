# coding=utf-8
import time

print "-----------log------------"

def log(f):
    def fn(*args, **kw):
        print 'call ', f.__name__ + '()...'
        return f(*args, **kw)
    return fn

def f(a):
    print "in f : " , a
    
f = log(f);
f(4)

def g(a, b):
    print "in g : " , a , b
    
g = log(g);
g(4, 5)

@log
def factorial1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print factorial1(10)

print "-----------time------------"

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in , result : %s, in %fs' % (f.__name__, r, (t2 - t1))
        return f(*args, **kw)
    return fn

@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

factorial(10)

