# coding=utf-8

'''

@author: pangt
'''

from blog.models import Person, Employee, Entry, Author, Book
from django.template.base import Template
from django.template.context import Context
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def db_ins():
    p = Person()
    p.addr = '跑马巷'
    p.age = 18
    p.name = 'panda'
    p.save()
     
    p1 = Person(name='panda_fly', addr='张府园', age=19)
    p1.save()
    
    t = Template("<h1>增 ： res {{s_res}}</h1>")
    c = Context({"s_res":"Ins success"})
    res = HttpResponse(t.render(c))
    return res

def db_n2_1():
    entry1 = Entry.objects.create(name="e1")
    entry2 = Entry.objects.create(name="e2")
    emp1 = Employee.objects.create(name="emp1", entry=entry1)
    emp2 = Employee.objects.create(name="emp2", entry=entry2)
    emp3 = Employee.objects.create(name="emp3", entry=entry2)
    
    print "emp1 id : ", emp1.entry
    print "e2 ins : " , entry2.employee_set.all()
    print "e1 ins : " , entry1.employee_set.all()
    
    t = Template("<h1>多对一 ： res {{s_res}}</h1>")
    c = Context({"s_res":"More 2 one success"})
    res = HttpResponse(t.render(c))
    return res

def db_n2_n():
    Author.objects.create(name="a1")
    Author.objects.create(name="a2")
    Author.objects.create(name="a3")    
    
    book1 = Book.objects.create(name="b1")
    book2 = Book.objects.create(name="b2")
    
    # 对应关系
    a1 = Author.objects.get(name__exact='a1')
    a2 = Author.objects.get(name__exact='a2')
    if None != a1 and None != a2 :
        book1.autours.add(a1)
        book1.autours.add(a2)
    
    authors = Author.objects.all()
    print "All authors : " , authors
    print "book1 authors : " , book1.autours.all()
    
    a1.book_set.create(name="b3")
    a1.book_set.add(book1)
    a1.book_set.add(book2)
    print "All book : " , Book.objects.all()
    print "A1 books : " , a1.book_set.all()
    a1.book_set.remove(book2)
    print "A1 books after remove : " , a1.book_set.all()    
    
    t = Template("<h1>多对多 ： res {{s_res}}</h1>")
    c = Context({"s_res":"More 2 More success"})
    res = HttpResponse(t.render(c))
    return res



def db_sel():
    persons = Person.objects.all()
    parm = {'persons':persons, "len":len(persons)}
    res = render_to_response("sel_res.html", parm)
    return res
   


def db_del():
    obj_name = 'panda_fly'
    ps = Person.objects.filter(name=obj_name)
    if (len(ps) > 1):
        #         删整行
        # Person.objects.filter(name=obj_name).delete()
        Person.objects.filter(name=obj_name)[0].delete()
    elif (len(ps) == 1) :
        # 删一行
        Person.objects.get(name=obj_name).delete()
    
    t = Template("<h1>删： res {{s_res}}</h1>")
    c = Context({"s_res":"Del success"})
    res = HttpResponse(t.render(c))
    return res

def db_upd():
    obj_name = 'panda_fly'
    
    # 单个修改
    ps = Person.objects.filter(name=obj_name)[0]
    ps.name = 'fly_panda'
    ps.save();
    
    # 批量修改
    ps = Person.objects.filter(name=obj_name)
    ps.update(name='fly_panda1')
    
    t = Template("<h1>改： res {{s_res}}</h1>")
    c = Context({"s_res":"改 success"})
    res = HttpResponse(t.render(c))
    return res
