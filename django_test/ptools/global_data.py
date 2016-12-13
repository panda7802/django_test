# coding=utf8

'''
Created on 2016年12月5日

@author: pangt
'''

from sys import platform

class TGlobalData :
    plam = "unix"
    PROJECT_PATH = "PROJECT_PATH"
    
    def init(self):
        print "-------Global_data init" , self.plam
        self.plam = platform
        print "-------Global_data init", self.plam
        print "PROJECT_PATH" , self.PROJECT_PATH
        if "win" in self.plam:
            self.PROJECT_PATH = "F:\pythonCode\project"
        else :
            self.PROJECT_PATH = "/opt/upload"
       
              
tGlobalData = TGlobalData() 

# plam = "unix"
# PROJECT_PATH = "PROJECT_PATH"
# 
# def tsettings(request):
#     print "---settings"
#     init()
#     content = {"PROJECT_PATH": PROJECT_PATH}
#     return content
# 
# def init():
#     print "-------Global_data init" , plam
#     plam = platform
#     print "-------Global_data init",plam
#     print "PROJECT_PATH" , PROJECT_PATH
#     if "win" in plam:
#         PROJECT_PATH = "F:\pythonCode\project"
#     else :
#         PROJECT_PATH = "/opt/pack"
# 
# if "__main__" == __name__ :
#     init();
