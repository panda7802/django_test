from __future__ import unicode_literals

from django.db import models

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
     
    def __unicode__(self):
        return self.name + "\t" + self.addr + "\t" + self.age
