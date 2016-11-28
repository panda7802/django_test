# coding=utf-8
from __future__ import division
from __future__ import unicode_literals

from os.path import isdir
from genericpath import isfile

print isdir(r'E:\Project_info\CallApp')
print isfile(r'E:\Project_info\CallApp\callTaxi1')

try:
    print "import json"
    import json
except ImportError:
    print "import simplejson"
    import simplejson as json
print json.dumps({'python':2.7})

print 10 / 3

s = 'am I an unicode?'
print isinstance(s, unicode)
