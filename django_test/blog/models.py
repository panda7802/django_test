from __future__ import unicode_literals

from django.db import models
from random import choice

sex_choices = (
    ('f','famale'),
    ('m','male'),
)

class Entry(models.Model):
    name = models.CharField(max_length=128)
#     data = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.name
    
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=128)
    entry = models.ForeignKey(Entry)
    
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=128)
    addr = models.CharField(max_length=256)
    age = models.CharField(max_length=4)
    sex = models.CharField(max_length=4,choices=sex_choices)
     
    def __unicode__(self):
        return self.name + "\t" + self.addr + "\t" + self.age + "\t" + self.sex

class Author(models.Model):
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=128)
    autours = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name
    
