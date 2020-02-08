import tkinter as tk
import Analysisxls
import tkinter.ttk

c = Analysisxls.Analysisxls()
tlist = c.mainrowtocelltup2()
list_tname=[]
for i in tlist:
    list_tname.append(i.value)
print(list_tname)


class myUI:
    def __init__(self,*list_tname):
        self.wd=tk.Tk()
        self.wd.geometry("2568x1080")
        self.wd.title="数据分析软件"
        self.int_sheettitle=len(list_tname)
        list_tcontainer=[]
        for i in range(0,self.int_sheettitle):
            list_temn=[]

            lb_tname=tk.Label(self.wd,text=list_tname[i],width="25")
            lb_tname.grid(row=0,column=i)
            tb_tname=tk.Text(self.wd,width="25",height="2")
            tb_tname.insert("insert",list_tname[i])

            tb_tname.grid(row=1,column=i)
            list_temn.append(lb_tname)
            list_temn.append(tb_tname)
            list_tcontainer.append(list_temn)


            print("the {} time".format(i))



        for j in self.wd.winfo_children():
            print (j)

        # for i in list_tcontainer:
        #     print (i[0]["text"])

        self.wd.mainloop()


a=myUI(*list_tname)

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


