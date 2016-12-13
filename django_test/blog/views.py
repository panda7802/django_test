# coding=utf-8
from blog.base import base_pages
from blog.db import ctrl_db
from django.template.base import Template
from django.template.context import Context
from django.http.response import HttpResponse
import traceback
from blog.reg import upload_test, reg_test
from django.views.decorators.csrf import csrf_exempt

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
    sType = type + ''
    try :
        if 0 == cmp(sType, '1') :
            res = ctrl_db.db_ins()
        elif 0 == cmp(sType, '2') :
            res = ctrl_db.db_n2_1()
        elif 0 == cmp(sType, '3') :
            res = ctrl_db.db_n2_n()
        elif 0 == cmp(sType, '4') :
            res = ctrl_db.db_sel()
        elif 0 == cmp(sType, '5') :
            res = ctrl_db.db_del()
        elif 0 == cmp(sType, '6') :
            res = ctrl_db.db_upd()
        else :
            res = HttpResponse('<h1>Input Error</h1>')
    except :
        res = HttpResponse('<h1>Data Error</h1>')
        traceback.print_exc() 
        
    return res


@csrf_exempt
def upload(req,type):
    sType = type + ''
    try :
        if 0 == cmp(sType, '0') :
            res = upload_test.upfile(req)
        elif 0 == cmp(sType, '1') :
            res = upload_test.upfile1(req)
        else :
            res = HttpResponse('<h1>Input Error</h1>')
    except :
        res = HttpResponse('<h1>Data Error</h1>')
        traceback.print_exc() 
        
    return res

@csrf_exempt
def reg(req):
    try :
        res = reg_test.reg(req)
    except :
        res = HttpResponse('<h1>Data Error</h1>')
        traceback.print_exc() 
        
    return res

@csrf_exempt
def login(req):
    try :
        res = reg_test.login(req)
    except :
        res = HttpResponse('<h1>Data Error</h1>')
        traceback.print_exc() 
        
    return res

@csrf_exempt
def showUser(req):
    try :
        res = reg_test.showUser(req)
    except :
        res = HttpResponse('<h1>Data Error</h1>')
        traceback.print_exc() 
        
    return res

@csrf_exempt
def logout(req):
    try :
        res = reg_test.logout(req)
    except :
        res = HttpResponse('<h1>Data Error</h1>')
        traceback.print_exc() 
        
    return res


