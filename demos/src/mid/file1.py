# coding=utf-8

'''
Created on 2016年11月23日

@author: pangt
'''
import os

root_path = u"F:\迅雷下载\linux"
# root_path = "E:\Project_info\demo"

def getFiles(tmp_root_path, res):
    file_list = os.listdir(tmp_root_path)
    for tmp_f in file_list :
        tmp_path = os.path.join(tmp_root_path, tmp_f)
        if os.path.isdir(tmp_path) :
            getFiles(tmp_path, res)
        else :
            res.append(tmp_path)
    return res


L_files = []

getFiles(root_path, L_files)
sum = 0
for s in L_files:
    sum += os.path.getsize(s)
print sum

rw = os.walk(root_path)
print rw.next()

