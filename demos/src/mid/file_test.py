# coding=utf-8

'''
Created on 2016年11月22日

@author: pangt
'''
import re

s_path = r"C:\Users\pangt\Desktop\output.html"
fi = open(s_path, 'r+')
res = fi.readline()
# print res
# print fi.next()
# fi.seek(0,0)
# fi.write("panda\n123")
fi.close()

# 替换
fi = open(s_path, 'r+')
# tmp_seek = 0
src_str = "panda"
# for s in fi.readlines() :
#     s_len = len(s)
#     if src_str in s :
#         s_tmp = s.replace(src_str, "ddd")
#         fi.seek(tmp_seek)
#         fi.writelines(s_tmp)
#         tmp_seek += len(s_tmp)
#     else :
#         tmp_seek += s_len
s = fi.read()
s_tmp = s.replace(src_str, "ddd")
fi.seek(0)
# fi.write(s_tmp)
print s_tmp
fi.close()
