# coding=utf-8
import time
import functools

print "-----------log------------"

def log(tag):
    def logFunc(f):
        def fn(*args, **kw):
            print 'call [' + tag + "]" , f.__name__ + '()...'
            return f(*args, **kw)
        return fn
    return logFunc

@log("debug")
def f(a):
    print "in f : " , a

f("a")


def performance(tag):
    def performanceIn(f):
        @functools.wraps(f)
        def fn(*args, **kw):
            t1 = time.time();
            r = f(*args, **kw)
            time.sleep(0.5)
            t2 = time.time()
                
            if 0 == cmp("ms", tag) and (1 == 1) :
                print t1 , t2
                t1 = t1 * 1000
                t2 = t2 * 1000
            
            print 'call %s() , result : %s, in %.3f%s' % (f.__name__, r, (t2 - t1), tag)
            return r
        return fn
    return performanceIn;

@performance("ms")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print "func name : ", factorial.__name__
factorial(10)

