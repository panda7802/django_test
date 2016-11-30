# coding=utf-8

'''

@author: pangt
'''

from blog.models import Person, Employee, Entry
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
     
    p1 = Person(name='panda_fly', addr='张府园')
    p1.save()
    
    t = Template("<h1>增 ： res {{s_res}}</h1>")
    c = Context({"s_res":"Ins success"})
    res = HttpResponse(t.render(c))
    return res

def db_n2_1():
    entry1 = Entry.objects.create(name="e1")
    entry2 = Entry.objects.create(name="e2")
    emp1 = Employee.objects.create(name="emp1",entry=entry1)
    emp2 = Employee.objects.create(name="emp2",entry=entry2)
    emp3 = Employee.objects.create(name="emp3",entry=entry2)
    
    print "emp1 id : ", emp1.entry
    print "e2 ins : " , entry2.employee_set.all()
    print "e1 ins : " , entry1.employee_set.all()
    
    t = Template("<h1>多对一 ： res {{s_res}}</h1>")
    c = Context({"s_res":"More 2 one success"})
    res = HttpResponse(t.render(c))
    return res

def db_sel():
    persons = Person.objects.all()
    parm = {'persons':persons, "len":len(persons)}
    res = render_to_response("sel_res.html", parm)
    return res
   


