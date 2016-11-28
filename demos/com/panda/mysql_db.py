# coding=utf-8
'''
Created on 2016年11月17日

@author: pangt
'''

import MySQLdb
from warnings import catch_warnings
from symbol import except_clause

print MySQLdb
conn = MySQLdb.Connect(host='192.168.3.224', port=3306, user='root', passwd='12345678', db='panda', charset='utf8')
cursor = conn.cursor()

print conn
print cursor

sql = "select * from t_user;"
cursor.execute(sql)

print "总行数: " , cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs


rs = cursor.fetchall()
print rs

for row in rs :
    print "id=%s,name=%s,age=%s" % row

conn.autocommit(False)

print "----------开始修改"
sql_ins = "insert into t_user (name,age) values ('panda100',118)"
sql_upd = "update t_user set age = 100 where id > 4"
sql_del = "delete from t_user where id = 4"

try :
    cursor.execute(sql_ins)
    cursor.execute(sql_upd)
    cursor.execute(sql_del)
except Exception as e :
    print e
    conn.rollback()
conn.commit()

cursor.close()
conn.close
