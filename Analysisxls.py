import openpyxl
import re


class Analysisxls:
    def __init__(self, **kwr):

        self.workbookname = "实时电路可靠性分析工具V039.xlsm"
        self.sheetname = "全路由"
        self.myinit(**kwr)
        self.wb = openpyxl.load_workbook(self.workbookname)
        self.st = self.wb.get_sheet_by_name(self.sheetname)

    def filter(self, **kwr):
        cur = self.st.iter_rows()
        currow = next(cur)
        list_re = []
        # 获取**kwr中的组成一个按顺序排列的字符串

        while currow != self.mainrowtocelltup2():
            currow = next(cur)

        list_tname = []

        for i in currow:
            list_tname.append(i.value)

        list_pd = self.listpd(list_tname, **kwr)

        while currow:

            list_cur = []
            for i in currow:
                list_cur.append(i.value)

            if self.panjue(list_pd, list_cur):

                list_re.append(list_cur)
            try:
                currow = next(cur)
            except:
                return list_re
                # currow = next(cur)

    def panjue(self, p1, s1):

        for p in p1:
            if p == 1:
                continue
            else:
                if re.match(p, s1[p1.index(p)]) is None:
                    return 0

        return 1

    def listpd(self, list_tname, **kwr):
        list_p = len(list_tname) * [1]
        for key in kwr:
            iter_li = iter(list_tname)
            plist = next(iter_li)  # type:str
            while plist:
                if plist.find(key) > -1:
                    list_p[list_tname.index(plist)] = kwr[key]
                    break
                plist = next(iter_li)

        return list_p

    def myinit(self, **kwr):
        for a in kwr:
            if a == "workbook":
                self.workbookname = kwr[a]
            elif a == "sheet":
                self.sheetname = kwr[a]

    def __str__(self):
        self.filter()
        return str(self.mainrowtocelltup2())

    def mainrowtocelltup2(self):
        # 根据表格中第一行等于整体表格宽度来判断是否是表头别，利用生成器实现

        ll = self.st.max_column

        # print (type(st._cells))
        num = 1
        perrow = self.st.iter_rows()
        while True:
            exit_flag = False

            currow = next(perrow)
            for i in currow:

                if i.value == None:
                    exit_flag = True
                    break

            if exit_flag:
                continue

            return currow


# dicc = {"级别": "VC[3,4]$", "方向": "双向"}
# c = Analysisxls(**dicc)
# # tlist = c.mainrowtocelltup2()
# # list = []
# # for i in tlist:
# #     list.append(i.value)
# # print(list)
# a=c.filter(**dicc)
# for i in a:
#     print(i)
#
# print(len(a))
