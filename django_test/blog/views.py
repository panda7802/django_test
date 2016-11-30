# coding=utf-8
from blog.base import base_pages
from blog.db import ctrl_db
from django.template.base import Template
from django.template.context import Context
from django.http.response import HttpResponse

# Create your views here.
def index(req, id):
    return base_pages.index(req, id)

# Create your views here.
def index1(req, id):
    return base_pages.index1(req, id)

# Create your views here.
def index2(req, id):
    return base_pages.index2(req, id)

def db_ctrl(req, type):
    if type == '1' :
        res = ctrl_db.db_ins()
    if type == '2' :
        res = ctrl_db.db_n2_1()
    elif type == '4' :
        return ctrl_db.db_sel()
    else : 
        return HttpResponse('<h1>Input error</h1>')

    return res
