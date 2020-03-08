import os
# 当前文件路径
proDir = os.path.split(os.path.realpath(__file__))[0]
print(os.path.realpath(__file__))
print("proDir:"+proDir)
print(type(proDir))


# 在当前文件路径下查找.ini文件
configPath = os.path.join(proDir, "config.ini")
print(type(os.getcwd()))
mydir=os.getcwd()
# for root,dir,file in os.walk(mydir):
#     print(type(root))
#     print(type(dir))
#     print(file)
root,dir,file = next(os.walk(mydir))
print(file)
csv=[]
for i in file:
    if i.split(".")[-1]=="csv":
        csv.append(i)
print(csv)