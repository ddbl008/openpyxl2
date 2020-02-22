import pandas as pd
import numpy as np
import openpyxl
import traceback


class Csvaylisys:
    def __init__(self,fname):
        self.df=self.initdf(fname)
        #print(self.df.head(3))
    def initdf(self,fname):
        df=pd.read_csv(fname)

        formwidth=df.shape[1]
        #df2=df[(df.iloc[:,formwidth-1])=='备注']
        df2 = df[~(pd.isnull((df.iloc[:, formwidth - 1])))]
        list1=df2.index.to_list()
        print(type(list1))
        print(list1[0])
        #print(df.columns.get_loc(list1))
        df3=pd.read_csv(fname,header=list1[0]+1)
        print(df3)



        return df3




    def outhead(self):

        return list(self.df.keys())

    def query(self,idic,odir):
        idic={"名称":"保护","保护路由":"-"}
        odic={"级别":"3","名":"辅"}
        cond=True
        for i in idic:

            try:

                cond=cond & self.df[i].str.contains(idic[i])
            except Exception as e:
                print(e.args)
                print(traceback.format_exc())
        for i in odic:

            try:

                cond = cond & ~(self.df[i].str.contains(odic[i]))
            except Exception as e:
                print(e.args)
                print(traceback.format_exc())
        #cond=cond & ~(self.df["级别"].str.contains("服务"))

        return self.df[cond]







fname="39.csv"
a={}
b={}
c = Csvaylisys(fname)
print(c.outhead())
rlist=list(c.query(a,b)["名称"])
for i in rlist:
    print(i)
