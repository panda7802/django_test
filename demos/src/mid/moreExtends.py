# coding=utf-8

# +-Person
#   +- Student
#   +- Teacher
# 
# 是一类继承树；
# 
# +- SkillMixin
#    +- BasketballMixin
#    +- FootballMixin
# 
# 是一类继承树。
# 
# 通过多重继承，请定义“会打篮球的学生”和“会踢足球的老师”。

class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student,BasketballMixin):
    pass

class FTeacher(Teacher,FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()
