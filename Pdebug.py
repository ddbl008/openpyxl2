import pandas as pd
import numpy as np
import openpyxl
import traceback
import re
import os
import types


class Csvaylisys:
    def __init__(self, fname):
        if type(fname) is str:
            self.df = self.initdf(fname)
        if isinstance(fname, pd.DataFrame):

            self.df=fname
        import os
        import configparser

        # 当前文件路径
        proDir = os.path.split(os.path.realpath(__file__))[0]
        # 在当前文件路径下查找.ini文件
        configPath = os.path.join(proDir, "Pddebug.ini")

        conf = configparser.ConfigParser()

        # 读取.ini文件
        conf.read(configPath, encoding='utf-8')

        self.dic_classify = {}
        for i in conf.options("type"):
            self.dic_classify[i] = str.split(conf.get("type", i), "/")

    @classmethod
    def allcsv(cls):
        mydir = os.getcwd()
        # for root,dir,file in os.walk(mydir):
        #     print(type(root))
        #     print(type(dir))
        #     print(file)
        root, dir, file = next(os.walk(mydir))
        print(file)
        csv = []
        for i in file:
            if i.split(".")[-1] == "csv":
                csv.append(i)
        df=pd.DataFrame()

        for acsv in csv:
            df2=cls.initdf(type(Csvaylisys),acsv)
            df = pd.concat([df, df2], axis=0, ignore_index=True)

        return cls(df)

    def initdf(self, fname):
        ftape=str(fname)[-3:]
        if ftape=="csv":

            df = pd.read_csv(fname)
        if ftape=="lsx" or ftape=="xls":
            df=pd.read_excel("省干新A网.xlsx",encoding="cp936")



        formwidth = df.shape[1]
        # df2=df[(df.iloc[:,formwidth-1])=='备注']
        df2 = df[~(pd.isnull((df.iloc[:, formwidth - 1])))]
        list1 = df2.index.to_list()

        # print(df.columns.get_loc(list1))
        df3 = pd.read_csv(fname, header=list1[0] + 1)

        df3["来源"]=fname

        return df3

    def addsimplepathcol(self):
        self.df["工作简化"] = ""
        narry = self.df['工作路由'].values
        nn = self.df["工作简化"].values
        nlen = 3807

        for i in range(0, nlen):
            # print(type(nn[i,]),type(narry[i,]))
            nn[i,] = self.simplepath(narry[i,])

        self.df["备用简化"] = ""
        narry = self.df['保护路由'].values
        nn = self.df["备用简化"].values
        nlen = 3807

        for i in range(0, nlen):
            # print(type(nn[i,]),type(narry[i,]))
            nn[i,] = self.simplepath(narry[i,])

        return self.df

    def outhead(self):

        return list(self.df.keys())

    def simplepath(self, str_path):

        # 获得如下类型输出('423-太安开关站-6', '422-黄坪变-12'), ('422-黄坪变-14', '305-仁和开关站-7')
        if str_path == "-":
            return "无保护路径"

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

    def querykey(self, idic, odic):

        cond = True
        for i in idic:

            try:

                cond = cond & self.df[i].str.contains(idic[i])
            except Exception as e:
                print(e.args)
                print(traceback.format_exc())
        for i in odic:

            try:

                cond = cond & ~(self.df[i].str.contains(odic[i]))
            except Exception as e:
                print(e.args)
                print(traceback.format_exc())
        # cond=cond & ~(self.df["级别"].str.contains("服务"))

        return self.df[cond]

    #实现N-1分析按照指定的字符串排序输出
    def sort(self,df):
        def bianhua(a,li_key):
            lista = li_key
            aa = a  # type:str
            for i in lista:
                if re.search(i, aa,re.IGNORECASE):
                    return lista.index(i)
            return 10

        l_keylevel=[]

        l_lv1=["保护","安稳","稳控","自动化"]
        l_lv2=["500kV","220kV","110kV","35kV"]
        l_keylevel.append(l_lv1)
        l_keylevel.append(l_lv2)
        li_sname=[]
        for i in range(0,len(l_keylevel)):
            #df["序号"+i]=df["名称"].apply(bianhua,args=(df["名称"],l_keylevel[i]))
            df["序号" + str(i)] = df["名称"].apply(bianhua,args=(l_keylevel[i],))

            li_sname.append("序号"+str(i))


        li_sname.append("名称")
        fdf=df.sort_values(by=li_sname)

        df1=fdf[fdf["n-1影响"]=="业务中断"]
        df2 = fdf[fdf["n-1影响"] == "可靠性降低"]
        #df.sort_values()
        #df["序号"]=df["名称"].apply(bianhua)
        df = pd.concat([df1, df2], axis=0, ignore_index=True)


        del li_sname[-1]


        return df.drop(columns=li_sname,axis=1)

    def n1(self, susbednpattern):
        # 影响主用路由
        idic = {}
        idic["工作路由"] = susbednpattern

        odic = {}
        odic["保护路由"] = "-"
        df1 = self.querykey(idic, odic)
        df1['n-1影响'] = '可靠性降低'
        # 影响备用路由
        idic = {}
        idic["保护路由"] = susbednpattern

        odic = {}
        odic["工作路由"] = susbednpattern
        odic["级别"]="服务层"
        df2 = self.querykey(idic, odic)
        df2['n-1影响'] = '可靠性降低'

        # 影响单路径
        idic = {}
        idic["工作路由"] = susbednpattern
        idic["保护路由"] = "^-$"

        odic = {}
        odic["级别"] = "服务层"

        df3 = self.querykey(idic, odic)
        df3['n-1影响'] = '业务中断'

        # 影响主备路径
        idic = {}
        idic["工作路由"] = susbednpattern
        idic["保护路由"] = susbednpattern

        odic = {}
        odic["级别"] = "服务层"

        df4 = self.querykey(idic, odic)
        df4['n-1影响'] = '业务中断'

        # print(df2["名称"])

        dfr = df4.append(df3).append(df2).append(df1)

        dfr=self.sort(dfr)


        return dfr







    def showallopaht(self, nodename):
        #通过输入节点名字nodename，关联出其对应的光口以及对侧光口，并以列表形式输出
        Pnodename=r".{,5}"+nodename+r".?"
        pat1 = r"服务层: SDH\[101 - 省调 - (.*?) - SL16A - 1(SDH - 1) - VC4:16->103 - (.*?) - (.*?) - SL16A - 1(SDH - 1) - VC4: 16\];"
        pat1 = r"\[\d{1,4}-.*?" + Pnodename + r"-(.*?)-.*?S\D{,3}(\d{1,2}).*?->\d{1,4}-(.*?)-(.*?)-.*$"
        list_Oaptical=[]
        print(self.df.shape[0])
        for i in range(0, self.df.shape[0]):
            t = str(self.df.iloc[i, 8])
            souce_t=str(self.df.iloc[i, 14])

            match = re.search(pat1, t, re.MULTILINE)
            if match:
                print("patrern:")
                print(match.groups())
                print(pat1)
                print(t)
                list_temp = []
                list_temp.append(nodename)
                for i in match.groups(()):
                    list_temp.append(i)
                #加入来源标识：
                list_temp.append(souce_t)
                list_Oaptical.append(list_temp)


        list2=[]
        for i in list_Oaptical:
            if i not in list2:
                list2.append(i)


        for i in list2:
            print(i)
        return list2


    def typeclassis(self,df,index_name,newcol_name,dic_class=None):
        if dic_class==None:
            dic_class=self.dic_classify

        def bianhua(a,dic_class):
            for onet in dic_class:
                for j in dic_class[onet]:
                    if a.find(j)>-1:
                        return onet



            return "其他"




        df[newcol_name]=df[index_name].apply(bianhua,args=(dic_class,))



        return df




fname="39.csv"
pat = "厂口.*-5.*-1.*?->.*?龙海.*?-11-.*?-1.*"
c = Csvaylisys(fname)
df=c.n1(pat)
print(df)
list_t=["序号","名称","级别","n-1影响","工作路由","保护路由","来源"]
df[list_t].to_csv("dfout.csv",encoding='utf_8_sig')






dic_class={}
dic_class["自动化"]=["OCS","EMS"]
dic_class["稳控"]=["安稳","稳控"]
dic_class["网管"]=["网管"]




c.typeclassis(df[list_t],"名称","业务分类").to_csv("typeclassis.csv",encoding='utf_8_sig')
