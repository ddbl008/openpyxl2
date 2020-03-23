#调试读取INi
# import os
# import sys
# import fnmatch
# import win32com.client
#
# PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
# PATH_DATA = os.path.abspath(os.path.dirname(sys.argv[0])) + "\data"
#
#
# # 主要执行函数
# def main():
#     wordapp = win32com.client.gencache.EnsureDispatch("Word.Application")
#     try:
#         for root, dirs, files in os.walk(PATH_DATA):
#             for _dir in dirs:
#                 pass
#             for _file in files:
#                 if not fnmatch.fnmatch(_file, '*.doc'):
#                     continue
#                 word_file = os.path.join(root, _file)
#                 wordapp.Documents.Open(word_file)
#                 docastxt = word_file[:-3] + 'txt'
#                 wordapp.ActiveDocument.SaveAs(docastxt, FileFormat=win32com.client.constants.wdFormatText)
#                 wordapp.ActiveDocument.Close()
#     finally:
#         wordapp.Quit()
#     print ("well done!")
#
#
# if __name__ == '__main__':
#     main()
import pandas as pd
import re
import os
import configparser

# 当前文件路径
proDir = os.path.split(os.path.realpath(__file__))[0]
# 在当前文件路径下查找.ini文件
configPath = os.path.join(proDir, "contxt.ini")
print(configPath)

conf = configparser.ConfigParser()

# 读取.ini文件
conf.read(configPath,encoding='utf-8')
#conf.read("config.txt")
plist=str.split(conf.get("Pattern_sec","plist"),"/")
print(type(conf.options("Pattern_sec")))
dic_new={}
for i in conf.options("Pattern_sec"):
    dic_new[i]=str.split(conf.get("Pattern_sec",i),"/")

print(dic_new)









# class txtaly:
#     def __init__(self, textname):
#
#         self.df = pd.read_table(textname, header=None)
#         proDir = os.path.split(os.path.realpath(__file__))[0]
#         # 在当前文件路径下查找.ini文件
#         configPath = os.path.join(proDir, "contxt.ini")
#         print(configPath)
#         conf = configparser.ConfigParser()
#         conf.read(configPath,encoding='utf-8')
#         self.plist=str.split(conf.get("Pattern_sec","plist"),"/")
#
#         print(plist)





# data = pd.read_table('test.txt',header=None,encoding='gb2312',sep='。',index_col=0)
