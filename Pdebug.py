import pandas as pd
import numpy as np
import openpyxl
import traceback
import re


class Csvaylisys:
    def __init__(self, fname):
        self.df = self.initdf(fname)
        # print(self.df.head(3))

    def initdf(self, fname):
        df = pd.read_csv(fname)

        formwidth = df.shape[1]
        # df2=df[(df.iloc[:,formwidth-1])=='备注']
        df2 = df[~(pd.isnull((df.iloc[:, formwidth - 1])))]
        list1 = df2.index.to_list()

        # print(df.columns.get_loc(list1))
        df3 = pd.read_csv(fname, header=list1[0] + 1)

        # def tt(x):
        #     naay = (x["方向"].values)
        #     for ii in range(0,3806):
        #         naay[ii,]= naay[ii,]+"nie"
        #     for i in naay:
        #         i=2
        #     print(naay.shape)
        #     return x["方向"]
        #
        # df3["方向"]= tt(df3)

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
        df2 = self.querykey(idic, odic)
        df2['n-1影响'] = '可靠性降低'

        # 影响单路径
        idic = {}
        idic["工作路由"] = susbednpattern
        idic["保护路由"] = "-"

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
                list_Oaptical.append(list_temp)

        list2=[]
        for i in list_Oaptical:
            if i not in list2:
                list2.append(i)


        for i in list2:
            print(i)
        return list2

#
# fname = "39.csv"
# idic = {"名称": "保护", "保护路由": "-"}
# odic = {"级别": "3", "名": "辅"}
# pat = "省调.*-14.*->"
# c = Csvaylisys(fname)
#
#
# pat = "曲靖地调"
# c.showallopaht(pat)
