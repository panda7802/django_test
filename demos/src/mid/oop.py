# coding=utf-8
from itertools import count

print "test object---------"

class Person :
    def __init__(self, name):
        print "Name is : " , name

xiaoming = Person("xiaoming")
xiaohong = Person("xiaohong")

print xiaoming
print xiaohong

print xiaohong == xiaoming

print "test object attr---------"
class Person1(object):
    pass

p1 = Person1()
p1.name = 'Bart'

p2 = Person1()
p2.name = 'Adam'

p3 = Person1()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2 : cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name


print "test object init ---------"
class Person2(object):
    def __init__(self, name, sex, birth, job):
        self.name = name
        self.sex = sex
        self.birth = birth
        self.job = job

xiaoming = Person2('Xiao Ming', 'Male', '1990-1-1', job='Student')
xiaoming1 = Person2('Xiao Ming', 'Male', '1990-1-1', job='Student')

xiaoming.money = 100

print xiaoming.name, xiaoming.job
print xiaoming.money

print "test object private---------"
class Person3(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person3('Bob', 59)

print p.name
# print p.__score

print "test object static ---------"
class Person4(object):
    __count = 0
    def __init__(self, name):
        Person4.__count = Person4.__count + 1
        self.name = name
        print "count " , Person4.__count

p1 = Person4('Bob')
p2 = Person4('Alice')
p3 = Person4('Tim')

# print Person4.__count


print "test attr ----------------"
class Person5(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person5('Bob')
p2 = Person5('Alice')

print 'Person.address = ' + Person5.address

p1.address = 'China'
print 'p1.address = ' + p1.address
del p1.address
print 'after del p1.address = ' + p1.address

print 'Person.address = ' + Person5.address
print 'p2.address = ' + p2.address
