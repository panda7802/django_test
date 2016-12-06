# coding=utf-8

'''
Created on 2016年12月1日

@author: pangt
'''
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
import os
from ptools.global_data import PROJECT_PATH
from blog import models
from blog.models import Person


class PersonForm(forms.Form):
    name = forms.CharField(label='姓名',initial='panda')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField()

def reg(req):
    if req.method == 'POST' :
        pf = PersonForm(req.POST)
        if pf.is_valid():
            db_uf = models.Person()
            db_uf.age = pf.cleaned_data['age']
            db_uf.name = pf.cleaned_data['name']
            db_uf.addr = pf.cleaned_data['addr']
            db_uf.sex = pf.cleaned_data['sex']
            db_uf.passwd = pf.cleaned_data['passwd']
            print db_uf
            return HttpResponse('OK 2 reg')
    elif req.method == 'GET' :
        pf = PersonForm()
        return render_to_response('reg_user.html', {'pf':pf})
    else :
        return HttpResponse('ERR')    


