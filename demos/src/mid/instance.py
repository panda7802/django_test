
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)


import json

class Students1(object):
    def read(self):
        return  r'["Tim", "Bob", "Alice"]'

s = Students1()

print json.load(s)


class Person2(object):

    age = 0
    course = ""

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)
        
        

p = Person2('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

