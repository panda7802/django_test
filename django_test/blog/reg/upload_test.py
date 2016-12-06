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


class UserForm(forms.Form):
    name = forms.CharField(label='姓名',initial='panda')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField()
    
@csrf_exempt
def upfile(req):
    if req.method == 'POST' :
        uf = UserForm(req.POST, req.FILES)
        if uf.is_valid():
            print uf.cleaned_data , uf.cleaned_data['name']
            print uf.cleaned_data['img'].size
            sDir = PROJECT_PATH + '/recv/';
            if False == os.path.exists(sDir) :
                os.mkdir(sDir)
            fp = file(sDir + uf.cleaned_data['img'].name, 'wb')
            sData = uf.cleaned_data['img'].read()
            fp.write(sData)
            fp.close()
            return HttpResponse('OK')
#             return render_to_response('OK')
    elif req.method == 'GET' :
        uf = UserForm()
        return render_to_response('reg.html', {'uf':uf})
    else :
        return HttpResponse('ERR')

#用数据库存表单
@csrf_exempt
def upfile1(req):
    if req.method == 'POST' :
        uf = UserForm(req.POST, req.FILES)
        if uf.is_valid():
            print "pre 2 save db"
            print uf.cleaned_data , uf.cleaned_data['name']
            print uf.cleaned_data['img'].size
            db_uf = models.UserForm()
            db_uf.age = uf.cleaned_data['age']
            db_uf.name = uf.cleaned_data['name']
            db_uf.img = uf.cleaned_data['img']
            db_uf.save()
            return HttpResponse('OK 2 DB')
#             return render_to_response('OK')
    elif req.method == 'GET' :
        uf = UserForm()
        return render_to_response('reg1.html', {'uf':uf})
    else :
        return HttpResponse('ERR')    


