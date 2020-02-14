import tkinter as tk
import Analysisxls
import tkinter.ttk

c = Analysisxls.Analysisxls()
tlist = c.mainrowtocelltup2()
list_tname = []
for i in tlist:
    list_tname.append(i.value)
print(list_tname)


class myUI:
    def __init__(self, *list_tname):
        self.wd = tk.Tk()
        self.wd.geometry("2568x1080")
        self.wd.title = "数据分析软件"
        self.int_sheettitle = len(list_tname)
        list_tcontainer = []
        list_var = []
        for i in range(0, self.int_sheettitle):
            list_var.append(tk.IntVar())

        frame_selectoutpu = tk.Frame(self.wd)
        tree_output = tk.ttk.Treeview(self.wd, columns=list_tname)

        for i in range(0, self.int_sheettitle):
            tree_output.heading(list_tname[i], text=list_tname[i])

            tree_output.column(list_tname[i], width=round(2568 / (self.int_sheettitle + 2)))

            list_temn = []

            lb_tname = tk.Label(self.wd, text=list_tname[i], width="25")
            tb_tname = tk.Entry(self.wd, width=25)
            ckbt_output = tk.Checkbutton(frame_selectoutpu, text=list_tname[i], variable=list_var[i], onvalue=1,
                                         offvalue=0)

            # tb_tname=tk.Text(self.wd,width="25",height="2")
            # tb_tname.insert("insert",list_tname[i])
            #

            ckbt_output.grid(row=i // 4, column=i % 4)
            lb_tname.grid(row=0, column=i)
            tb_tname.grid(row=1, column=i)
            #
            list_temn.append(lb_tname)
            list_temn.append(tb_tname)
            list_tcontainer.append(list_temn)

        # 放置radiobutton 框架
        frame_selectoutpu.grid(row=2, column=3, columnspan=3, rowspan=3)

        tree_output.grid(row=10, column=0, columnspan=self.int_sheettitle + 1)

        # tree_output.grid()

        # for i in range(0,self.int_sheettitle):

        def bt_radio_sure():
            lb_output.delete(1.0, 'end')
            for i in list_var:
                lb_output.insert("insert", i.get())

        bt_radiosure = tk.Button(frame_selectoutpu, text="确定", command=bt_radio_sure)
        bt_radiosure.grid()

        lb_output = tk.Text(self.wd, width=220)
        lb_output.grid(column=1, columnspan=self.int_sheettitle - 2)
        cc = Analysisxls.Analysisxls()
        list_src = cc.filter()
        for j in cc.alsomecol(list_src, **c.dic_top):
            tree_output.insert('', 'end', values=j)

        self.wd.mainloop()

        dicc = {"方向": "双向", "工作路由": "版纳地调.*-6.*->"}

        # list_text = c.list_getsheetcontent("19:20")
        # print("test:", list_text[1][8])
        #
        # pattern = "dfdfdf"
        # match = re.findall(pattern, list_text[1][8])
        # print(len(match))

        # for i in list_tcontainer:
        #     print (i[0]["text"])


a = myUI(*list_tname)

# dicc = {"级别": "VC[3,4]$", "方向": "双向"}
# c = Analysisxls.Analysisxls()
# # tlist = c.mainrowtocelltup2()
# # list = []
# # for i in tlist:
# #     list.append(i.value)
# # print(list)
#
# a=c.filter(**dicc)
# def hitme():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#
#
#     else:
#         on_hit = False
#         var.set(e.get())
#
# window = tk.Tk()
# window.title('my window')
#
# window.geometry('500x220')
#
# bt=[None,None,None]
# cbox=tkinter.ttk.Combobox(window)
# cbox["value"]=a
# combox=tk.Listbox(window,width=100)
# combox.insert(0,*a)
# var = tk.StringVar()
#
# for i in range(0,2):
#     print(i)
#     tname="This is NO.{} label".format(i)
#
#     #var.set("This is NO.{} label".format(i))
#     la= tk.Label(window, text=tname, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
#     la["text"]="hellog"
#     la.pack()
#
#
# cbox.pack()
#
# on_hit=False
# window.mainloop()
# window.winfo_children()
