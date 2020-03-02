import tkinter as tk

import Pdebug
import tkinter.ttk


class newUI:
    def __init__(self, oneCsvaylisys):
        self.list_maintapname=["功能1","功能2","功能3"]
        self.oneCsvaylisys = oneCsvaylisys
        self.wd = tk.Tk()
        self.wd.geometry("300x300")
        self.wd.title = "数据分析软件"
        self.CreatemainFrame()
        self.wd.mainloop()
        pass

    # def makelblist(self,lblist):
    def tab_click(self,event=None):
        print(type(event))
        click_w=event.widget['text']
        for i in self.list_maintapname:
            if self.namelb_list[i][0]["text"]==click_w:
                self.namelb_list[i][1].pack(side='top')

            else:
                self.namelb_list[i][1].pack_forget()







        pass

    def CreatemainFrame(self):

        self.tabframe = tk.Frame(self.wd,width=200)
        self.mframe = tk.Frame(self.wd,width=200)
        self.lf = tk.LabelFrame(self.tabframe)

        lblist = self.list_maintapname
        length = len(lblist)
        print(length)
        self.namelb_list = {}
        for i in range(0, length):
            one_list = []
            one_bt = tk.Button(self.lf, text=lblist[i])
            one_bt.bind("<Button-1>", self.tab_click)
            one_frame = tk.Frame(self.mframe)
            one_list.append(one_bt)
            one_list.append(one_frame)
            self.namelb_list[lblist[i]] = one_list
            one_bt.pack(side="left")
            one_frame.pack()

        # self.btton1=tk.Button(self.lf,text='12221')
        # self.btton2 = tk.Button(self.lf, text='12222')
        # self.btton3 = tk.Button(self.lf, text='12223')
        #
        self.lf.pack()

        self.tabframe.pack(side="top")
        self.mframe.pack(side="top")

        self.f1_creat()
        # btton1 = tk.Label(self.namelb_list["功能1"][1], text='第一功能框dddd')
        # btton2 = tk.Label(self.namelb_list["功能2"][1], text='第二功能框')
        # btton3 = tk.Label(self.namelb_list["功能3"][1], text='第三功能框')
        # self.namelb_list["功能2"][1].pack_forget()
        # self.namelb_list["功能3"][1].pack_forget()
        # btton1.pack(side="left")
        # btton2.pack(side="left")
        # btton3.pack(side="left")



        pass

    def f1_creat(self):

        def sure_click():
            text1.delete(1.0,"end")

            c=Pdebug.Csvaylisys("39.csv")
            r_list=c.showallopaht(entry1.get())

            for i in r_list:


                text1.insert("insert", str(i)+"\n")




            pass


        top=self.namelb_list["功能1"][1]
        f1=tk.Frame(top)
        f2 = tk.Frame(top)
        f3 = tk.Frame(top)

        labe1 = tk.Label(f1, text='光口查询功能:输入待查询站点名字后，即可获得与该站发生联系的光口以及对侧站点槽位，连接速率信息',font="15",bg="yellow")
        labe2 = tk.Label(f2, text='请输入站点名字',font="20",bg="gray")
        entry1=tk.Entry(f2)
        bt1=tk.Button(f2,text="确定",command=sure_click)
        text1=tk.Text(f3,width=100)


        labe1.pack()
        labe2.pack(side="left")
        entry1.pack(side="left")
        bt1.pack(side="left")
        text1.pack()

        f1.pack(side="top")
        f2.pack(side="top")
        f3.pack(side="top")



        pass


fname = "39.csv"
cc = Pdebug.Csvaylisys(fname)

c = newUI(cc)
