import tkinter as tk

import Pdebug
import tkinter.ttk


# 增加功能描述，检测同目录下csv文件，若有的都加入df，并且增加一列字段跟表名一样。光口筛选的时候可以筛选三张网光口，N-1分析的时候，需要选择是属于哪一张网


class newUI:
    def __init__(self, oneCsvaylisys):
        self.list_maintapname = ["功能1", "功能2", "功能3"]
        self.oneCsvaylisys = oneCsvaylisys
        self.wd = tk.Tk()
        self.wd.geometry("300x300")
        self.wd.title = "数据分析软件"
        self.CreatemainFrame()
        self.wd.mainloop()
        pass

    # def makelblist(self,lblist):
    def tab_click(self, event=None):
        print(type(event))
        click_w = event.widget['text']
        for i in self.list_maintapname:
            if self.namelb_list[i][0]["text"] == click_w:
                self.namelb_list[i][1].pack(side='top')

            else:
                self.namelb_list[i][1].pack_forget()

        pass

    def CreatemainFrame(self):

        self.tabframe = tk.Frame(self.wd, width=200)
        self.mframe = tk.Frame(self.wd, width=200)
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
        self.f2_creat()
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
            text1.delete(1.0, "end")

            # c=Pdebug.Csvaylisys("39.csv")
            c = Pdebug.Csvaylisys.allcsv()
            r_list = c.showallopaht(entry1.get())

            for i in r_list:
                text1.insert("insert", str(i) + "\n")

        def on_output():
            file = open("output.txt", mode="w")
            list_output = text1.get("0.0", "end")
            print("output is :"+list_output)
            for i in list_output:
                file.writelines(i)



        top = self.namelb_list["功能1"][1]
        f1 = tk.Frame(top)
        f2 = tk.Frame(top)
        f3 = tk.Frame(top)

        labe1 = tk.Label(f1, text='光口查询功能:输入待查询站点名字后，即可获得与该站发生联系的光口以及对侧站点槽位，连接速率信息', font="15", bg="yellow")
        labe2 = tk.Label(f2, text='请输入站点名字', font="20", bg="gray")
        entry1 = tk.Entry(f2)
        bt1 = tk.Button(f2, text="确定", command=sure_click)
        text1 = tk.Text(f3, width=100)
        bt2 = tk.Button(f3, text="导出至本地目录", command=on_output)

        labe1.pack()
        labe2.pack(side="left")
        entry1.pack(side="left")
        bt1.pack(side="left")
        text1.pack(side="top")
        bt2.pack(side="top")

        f1.pack(side="top")
        f2.pack(side="top")
        f3.pack(side="top")

        pass

    def f2_creat(self):

        # def sure_click():
        #     text1.delete(1.0, "end")
        #
        #     # c=Pdebug.Csvaylisys("39.csv")
        #     c = Pdebug.Csvaylisys.allcsv()
        #     r_list = c.showallopaht(entry1.get())
        #
        #     for i in r_list:
        #         text1.insert("insert", str(i) + "\n")
        #
        # def on_output():
        #     file = open("output.txt", mode="w")
        #     list_output = text1.get("0.0", "end")
        #     print("output is :"+list_output)
        #     for i in list_output:
        #         file.writelines(i)



        top = self.namelb_list["功能2"][1]
        f1 = tk.Frame(top)#显示那些需要显示的checkbutton
        f2 = tk.Frame(top)#显示查询N-1分析的光路
        f3 = tk.Frame(top)#树形目录显示要得东西

        labe1 = tk.Label(f1, text='光口查询功能:输入待查询站点名字后，即可获得与该站发生联系的光口以及对侧站点槽位，连接速率信息', font="15", bg="yellow")

        labe_node1_name = tk.Label(f2, text='A站名字:', font="20", bg="gray")
        entry_node1_name = tk.Entry(f2)
        labe_node1_slot= tk.Label(f2, text='A站槽位:', font="20", bg="gray")
        entry_node1_slot = tk.Entry(f2)
        labe_node1_inter = tk.Label(f2, text='A站光口:', font="20", bg="gray")
        entry_node1_inter = tk.Entry(f2)
        labe_node2_name = tk.Label(f2, text='B站名字:', font="20", bg="gray")
        entry_node2_name = tk.Entry(f2)
        labe_node2_slot = tk.Label(f2, text='B站槽位:', font="20", bg="gray")
        entry_node2_slot = tk.Entry(f2)
        labe_node2_inter = tk.Label(f2, text='B站光口:', font="20", bg="gray")
        entry_node2_inter = tk.Entry(f2)

        cb_ob=tk.Checkbutton(f2,text="老B网")
        cb_na = tk.Checkbutton(f2, text="新A网")
        cb_nb=tk.Checkbutton(f2, text="新B网")

        list_tname = ["name", "type"]
        tree_output = tk.ttk.Treeview(f3, columns=list_tname)

        for i in list_tname:
            tree_output.heading(i, text=i)
            tree_output.column(i)

        labe_node1_name.pack(side="left")
        entry_node1_name.pack(side="left")
        labe_node1_slot.pack(side="left")
        entry_node1_slot.pack(side="left")
        labe_node1_inter.pack(side="left")
        entry_node1_inter.pack(side="left")
        labe_node2_name.pack(side="left")
        entry_node2_name.pack(side="left")
        labe_node2_slot.pack(side="left")
        entry_node2_slot.pack(side="left")
        labe_node2_inter.pack(side="left")
        entry_node2_inter.pack(side="left")

        cb_ob.pack(side="left")
        cb_na.pack(side="left")
        cb_nb.pack(side="left")

        tree_output.pack()


        # bt1 = tk.Button(f2, text="确定", command=sure_click)
        #
        #
        # text1 = tk.Text(f3, width=100)
        # bt2 = tk.Button(f3, text="导出至本地目录", command=on_output)


        # for i in range(0, self.int_sheettitle):
        #     tree_output.heading(list_tname[i], text=list_tname[i])
        #
        #     tree_output.column(list_tname[i], width=round(2568 / (self.int_sheettitle + 2)))
        #
        #     list_temn = []
        #
        #     lb_tname = tk.Label(self.wd, text=list_tname[i], width="25")
        #     tb_tname = tk.Entry(self.wd, width=25)
        #     ckbt_output = tk.Checkbutton(frame_selectoutpu, text=list_tname[i], variable=list_var[i], onvalue=1,
        #                                  offvalue=0)
        #
        #     # tb_tname=tk.Text(self.wd,width="25",height="2")
        #     # tb_tname.insert("insert",list_tname[i])
        #     #
        #
        #     ckbt_output.grid(row=i // 4, column=i % 4)
        #     lb_tname.grid(row=0, column=i)
        #     tb_tname.grid(row=1, column=i)
        #     #
        #     list_temn.append(lb_tname)
        #     list_temn.append(tb_tname)
        #     list_tcontainer.append(list_temn)
        #
        # # 放置radiobutton 框架
        # frame_selectoutpu.grid(row=2, column=3, columnspan=3, rowspan=3)
        #
        # tree_output.grid(row=10, column=0, columnspan=self.int_sheettitle + 1)



        f1.pack(side="top")
        f2.pack(side="top")
        f3.pack(side="top")

        pass

fname = "48.csv"
cc = Pdebug.Csvaylisys(fname)

c = newUI(cc)
