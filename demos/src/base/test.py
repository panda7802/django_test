# coding=utf-8
from zhishuSum import isZhishu

print 'PANDA'
a = 45678
b = 0x12fd2
c = a + b
print c
print 'Learn Python in imooc', c
b1 = 100 < 99
b2 = 0xff == 255
print b1 
print b2 

print 'hello, python.'
print 'hello,', 'python.'

x1 = 1
d = 3
n = 100
x100 = x1 + (n - 1) * d
s = (x1 + x100) * n / 2
print s

print 'Python was started in 1989 by "Guido".'
print 'Python is free and easy to learn.'


print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''

print u'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''

print 2.5 + 10.0 / 4

a = 'python'
print 'hello,', a or 'world'

b = ''
print 'hello,', b or 'world'

"""
L = [95.5,85,59]
print L[0]
print L[1]
print L[2]
#print L[3]
"""

L = ['Adam', 'Lisa', 'Bart']
L.insert(2, 'Paul')
L.insert(-0, 'Panda')
print L

print isZhishu(5)

print reduce(lambda x, y:x * y, range(1, 6))

print hex(45)

str = "panda will fly.fly"
print str.capitalize()
print str.replace("fly", "123")
print str.split(" ")

r1 = (1, 2, 3)
print r1[0]

print "test re------------"
import re
re_t = re.compile("1\d{10}x\nabc", re.I)
str = '''13951965720X
abc'''
print  str
res = re_t.findall(str)
print res
