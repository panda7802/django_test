# coding=utf-8

class Person(object):

    __name = ""
    __score = 0

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        res = ""
        if(self.__score >= 90):
            res = self.__name + " 优秀"
        elif  (self.__score >= 60):
            res = self.__name + " 及格"
        else :
            res = self.__name + " 不及格"
        return res

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

print "test method---------"
class Person1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person1('Bob', 90)
print p1.get_grade
print p1.get_grade()


print "test class method---------"
class Person2(object):

    
    __count = 0

    def __init__(self, name):
        Person2.__count = Person2.__count + 1
        
    @classmethod
    def how_many(self):
        return Person2.__count

print Person2.how_many()

p1 = Person2('Bob')

print Person2.how_many()

