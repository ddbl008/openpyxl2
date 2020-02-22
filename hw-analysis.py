import Analysisxls
import re



class HwAnalysis(Analysisxls.Analysisxls):
    def simplepath(self, str_path):

        # 获得如下类型输出('423-太安开关站-6', '422-黄坪变-12'), ('422-黄坪变-14', '305-仁和开关站-7')

        pattern = r"\[(.*?)\-\d{1,2}.*?\-\>(.*?)\-\d{1,2}"

        src = str_path
        match = re.finditer(pattern, src)
        list_re = []
        try:
            for i in match:
                # print(i.group(1))
                list_re.append(i.group(1))
            list_re.append(i.group(2))
        finally:

            return list_re

    def simplepath2(self, str_path):
        # 获得如下类型输出('423-太安开关站-6', '422-黄坪变-12'), ('422-黄坪变-14', '305-仁和开关站-7')

        pattern = r"\[(.*?)\-[N|s].*\-\>(.*?)\-[N|S]"

        src = str_path
        match = re.finditer(pattern, src)
        list_re = []
        for i in match:
            list_re.append(i.groups())

        return list_re





    def __init__(self,**kwr):
         #利用字典.file、sheet构造
           if len(kwr)==0:

               dic_init = {"workbook": "实时电路可靠性分析工具V039.xlsm", "sheet": "全路由","add":"add1"}

               super().__init__(**dic_init)
           else:
               super().__init__(**kwr)

           self.dic_celltrans = {"8": self.simplepath}
           self.dic_addcell = {"adddidiao": self.paththrughdidiao}
           self.dic_top = {}
           self.dic_top["cha"] = self.dic_celltrans
           self.dic_top["add"] = self.dic_addcell

    def iter_n1alysis(self,list_src,pattern):
        #基于list_src产生一系列字段描述该条条记录
        outputdic={}
        for curline in list_src:
            #电路中断
            outputdic["content"] = curline
            match=re.findall(pattern,curline[8])

            if len(match)>0 and list_src[9]=="-":
                outputdic["type"]="off"
                outputdic["stype"]="single path"
                yield outputdic



            elif len(match)>0 :
                match2=re.findall(pattern,curline[9])
                if len(match2)>0:
                    outputdic["type"] = "off"

                    outputdic["stype"] = "both stop"
                    yield outputdic
                else:
                    outputdic["type"] = "low"

                    outputdic["stype"] = "main stop"
                    yield outputdic
            else:

                match2 = re.findall(pattern,curline[9])
                if len(match2)>0:
                    outputdic["type"] = "low"

                    outputdic["stype"] = "spare stop"
                    yield outputdic

















            yield outputdic









dic_init={"workbook": "实时电路可靠性分析工具V039.xlsm", "sheet": "全路由","add":"add1"}
hw = HwAnalysis(**dic_init)
fillterkwr={"工作路由":"省调.*-14.*->"}
re_list=hw.filter(**fillterkwr)
pattern="省调.*-14.*->"


sum=0
for i in hw.iter_n1alysis(re_list,pattern):
    if "type" in i.keys():
        if i["type"]=="off" or i["type"]=="low":
            print(i["content"])
            sum+=1

print(sum)

# for i in hw.sheetlistconvert(re_list,**hw.dic_top):
#     print(i)


