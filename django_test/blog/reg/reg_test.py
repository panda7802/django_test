# coding=utf-8

'''
Created on 2016年12月1日

@author: pangt
'''
import os
from random import choice

from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

from blog import models
from blog.models import Person, sex_choices
from ptools.global_data import tGlobalData


class PersonForm(forms.Form):
    name = forms.CharField(label='姓名', initial='panda')
    age = forms.CharField(label='年龄', initial=18)
    addr = forms.CharField(label='地址', initial='跑马巷')
    sex = forms.CharField(label='性别')
    passwd = forms.CharField(label='密码', initial=1, widget=forms.PasswordInput)
    
#     def __unicode__(self):
#         print self.name + "\t" + self.age + "\t" + self.addr + "\t" + self.sex + "\t" + self.passwd 
    
def reg(req):
    plam = "win"
    if req.method == 'POST' :
        pf = PersonForm(req.POST)
        if pf.is_valid():
            db_pf = models.Person()
            db_pf.age = pf.cleaned_data['age']
            db_pf.name = pf.cleaned_data['name']
            db_pf.addr = pf.cleaned_data['addr']
            db_pf.sex = pf.cleaned_data['sex']
            db_pf.passwd = pf.cleaned_data['passwd']
            print "db_pf:", db_pf
            return HttpResponseRedirect("/login", {'db_pf':db_pf})
    elif req.method == 'GET' :
        pf = PersonForm()
        return render_to_response('reg_user.html', {'pf':pf})
    else :
        return HttpResponse('ERR')    
    
def login(req):
    print tGlobalData.PROJECT_PATH
    if req.method == 'POST' :
        pf = PersonForm(req.POST)
        if pf.is_valid():
            db_pf = models.Person()
            db_pf.age = pf.cleaned_data['age']
            db_pf.name = pf.cleaned_data['name']
            db_pf.addr = pf.cleaned_data['addr']
            db_pf.sex = pf.cleaned_data['sex']
            db_pf.passwd = pf.cleaned_data['passwd']
            persons = Person.objects.filter(name=db_pf.name, addr=db_pf.addr, sex=db_pf.sex, passwd=db_pf.passwd)
            if None != persons :
                resp = HttpResponseRedirect("/showUser", {'db_pf':db_pf})
                resp.set_cookie("db_pf", str(db_pf))
                req.session['name'] = db_pf.name
                return resp
            else :
                return HttpResponseRedirect("/login", {'db_pf':db_pf})
    elif req.method == 'GET' :
        pf = PersonForm()
        return render_to_response('login.html', {'pf':pf})
    else :
        return HttpResponse('ERR')

def showUser(req):
    s_db_pf = req.COOKIES.get('db_pf', "")
    name = req.session.get('name', '')  
    print  "s_db_pf" , s_db_pf
    print  "name" , name
    return render_to_response('show_user.html', {'s_db_pf':s_db_pf, 'name':name}, context_instance=RequestContext(req));

def logout(req):
    resp = HttpResponse('logout')
    resp.delete_cookie("db_pf")
    del req.session['name']
    return resp



