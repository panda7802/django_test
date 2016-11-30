# coding=utf-8

'''
Created on 2016年11月25日

@author: pangt
'''


from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.template import loader
from django.template.context import Context
from django.template.base import Template

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def say(self):
        return "I'm " + self.name , "in"
    
    
# Create your views here.
def index(req, id):
#     res = HttpResponse('<h1>Fly Panda</h1>')
    user = {"name":"tom", "age":23, "sex":"male"}
    p = Person("panda", 18, 'male')
    book_list = ['python', 'java', 'c']
    parm = {'title':'my_page', 'book_list':book_list, "user" : user, "id":id, "user1":p}
    res = render_to_response('index.html', parm)
    return res

# Create your views here.
def index1(req, id):
    t = loader.get_template("index.html")
    user = {"name":"tom", "age":23, "sex":"male"}
    p = Person("panda1", 18, 'male')
    book_list = ['python', 'java', 'c']
    parm = {'title':'my_page', 'book_list':book_list, "user" : user, "id":id, "user1":p}
    c = Context(parm)
    res = HttpResponse(t.render(c))
    return res


# Create your views here.
def index2(req, id):
    t = Template("<h1>hello {{id}}</h1>")
    c = Context({"id":id})
    res = HttpResponse(t.render(c))
    return res
 