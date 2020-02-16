#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk
import Analysisxls

g_font = ("Monaco", 12)


class mianframe(object):
    def __init__(self, master=None):
        self.root = master

        self.initframe2()

    def initframe2(self):
        self.mainfrm = tk.Frame(self.root)
        self.mainfrm.grid()

        self.frm_choose = tk.LabelFrame(self.mainfrm)
        self.frm_choose.grid(padx=1, pady=2)
        self.creat_chooseFrame()

        self.frm_func1 = tk.LabelFrame(self.mainfrm)
        self.frm_func1.grid(padx=1, pady=2)
        self.creat_func1frame()

        self.frm_func2 = tk.LabelFrame(self.mainfrm)
        self.frm_func2.grid(padx=1, pady=2)
        self.creat_func2frame()

    def creat_func1frame(self):
        # 此功能实现的路径的N-1分析
        list_name = ["A点名称", "A点槽位", "A点光口", "B点名称", "B点槽位", "B点光口"]
        self.dic_entry = {}

        for i in range(0, len(list_name)):
            la_temp = tk.Label(self.frm_func1, text=list_name[i])
            en_temp = tk.Entry(self.frm_func1)
            la_temp.grid()
            en_temp.grid()
            self.dic_entry[list_name[i]] = en_temp

        # 查询按钮,定义鼠标N-1分析
        def click_sure1(event=None):
            for i in self.dic_entry:
                print(i, self.dic_entry[i].get())
            print("once")
            # SDH[101-省调-14-SL16A-1(SDH-1)-VC4:4->105-厂口变-9-SL16A-1(SDH-1)-VC4:4]
            str_pattern = self.dic_entry[list_name[0]].get() + ".*?-" + self.dic_entry[list_name[1]].get() + "-.*?-" + \
                          self.dic_entry[
                              list_name[2]].get() + ".*?->.*?" + self.dic_entry[list_name[3]].get() + ".*?-" + \
                          self.dic_entry[list_name[4]].get() + "-.*?-" + \
                          self.dic_entry[list_name[5]].get()

            dic_mutienry = {}
            print(str_pattern)
            dic_mutienry["工作路由"] = str_pattern

            cc = Analysisxls.Analysisxls()
            list_src = cc.filter(**dic_mutienry)
            list_re = []
            for j in cc.alsomecol(list_src, **cc.dic_top):
                list_re.append(j)


            for i in list_re:
                print(i)
            # tree_output.insert('', 'end', values=list_re)

        bt_sure = tk.Button(self.frm_func1, text="确定查询", command=lambda: click_sure1())
        bt_sure.grid()

    def creat_func2frame(self):
        bt = tk.Button(self.frm_func2, text="func2 button")
        bt.grid()

    def btn_click(self, event=None):
        btn_text = event.widget['text']

        if btn_text == 1:
            # self.show_label_0.pack(fill="both", expand=1, padx=2, pady=2)
            # self.show_label_1.pack_forget()
            # self.show_label_2.pack_forget()
            # self.show_label_3.pack_forget()
            # self.frm_funcshow.pack_forget()
            self.frm_func1.grid()
            self.frm_func2.grid_forget()
        elif btn_text == 2:
            self.frm_func2.grid()
            self.frm_func1.grid_forget()

            # elif btn_text == "3":
            #     self.show_label_0.pack_forget()
            #     self.show_label_1.pack_forget()
            #     self.show_label_2.pack(fill="both", expand=1, padx=2, pady=2)
            #     self.show_label_3.pack_forget()
            # elif btn_text == "Button3":
            #     self.show_label_0.pack_forget()
            #     self.show_label_1.pack_forget()
            #     self.show_label_2.pack_forget()

    def creat_chooseFrame(self):
        list_btn = [i for i in range(1, 5)]
        list_bt = []
        for i in list_btn:
            self.bt = tk.Button(self.frm_choose, text=i)
            list_bt.append(self.bt)
            self.bt.grid(row=0, column=i)
            self.bt.bind('<Button-1>', self.btn_click)


#
#         self.root = master
#         self.create_frame()


# class ShowFrame(object):
#     '''
#     show frame
#     '''
#
#     def __init__(self, master=None):
#
#         self.root = master
#         self.create_frame()
#
#     def create_frame(self):
#         '''
#         create main frame
#         '''
#         self.frm = tk.Frame(self.root)
#         self.frm.pack(fill="both", expand=1)
#
#         self.frm_choose = tk.LabelFrame(self.frm)
#         self.frm_choose.pack(fill="both", expand=1, padx=2, side=tk.TOP)
#         self.frm_funcshow = tk.Frame(self.frm, width=100)
#         self.frm_show = tk.LabelFrame(self.frm)
#         self.frm_show.pack(fill="both", expand=1, padx=2, side=tk.LEFT)
#         self.frm_funcshow.pack(fill="both", expand=1, padx=2, side=tk.RIGHT)
#
#         self.treeview=tk.Entry(self.frm_funcshow)
#         self.treeview.pack()
#
#         self.create_frm_choose()
#         self.create_frm_show()
#
#     def create_frm_choose(self):
#         '''
#         create frame choose
#         '''
#         self.choose_info_lst = ["Button0", "Button1", "Button2", "Button3","BT4"]
#         self.choose_btn_lst = list()
#         for index, value in enumerate(self.choose_info_lst):
#             temp_btn = tk.Button(self.frm_choose,
#                                  anchor="w",
#                                  text=value,
#                                  font=g_font,
#                                  command=self.btn_click)
#             #temp_btn.bind('<Button-1>', self.btn_click)
#             temp_btn.pack(fill="both", expand=1, padx=2, pady=2, side=tk.LEFT)
#             self.choose_btn_lst.append(temp_btn)
#
#     def create_frm_show(self):
#         '''
#         create frame show
#         '''
#         self.show_label_0 = tk.Label(self.frm_show, text="Button0", font=g_font)
#         self.show_label_0.pack(fill="both", expand=1, padx=2, pady=2)
#
#         self.show_label_1 = tk.Label(self.frm_show, text="Button1", font=g_font)
#         self.show_label_1.pack_forget()
#
#         self.show_label_2 = tk.Label(self.frm_show, text="Button2", font=g_font)
#         self.show_label_2.pack_forget()
#
#         self.show_label_3 = tk.Label(self.frm_show, text="Button3", font=g_font)
#         self.show_label_3.pack_forget()
#
#     def btn_click(self, event=None):
#         '''
#         choose frm
#         '''
#         btn_text = event.widget['text']
#         if btn_text == "Button0":
#             self.show_label_0.pack(fill="both", expand=1, padx=2, pady=2)
#             self.show_label_1.pack_forget()
#             self.show_label_2.pack_forget()
#             self.show_label_3.pack_forget()
#             self.frm_funcshow.pack_forget()
#         elif btn_text == "Button1":
#             self.show_label_0.pack_forget()
#             self.show_label_1.pack(fill="both", expand=1, padx=2, pady=2)
#             self.show_label_2.pack_forget()
#             self.show_label_3.pack_forget()
#         elif btn_text == "Button2":
#             self.show_label_0.pack_forget()
#             self.show_label_1.pack_forget()
#             self.show_label_2.pack(fill="both", expand=1, padx=2, pady=2)
#             self.show_label_3.pack_forget()
#         elif btn_text == "Button3":
#             self.show_label_0.pack_forget()
#             self.show_label_1.pack_forget()
#             self.show_label_2.pack_forget()
#             self.show_label_3.pack(fill="both", expand=1, padx=2, pady=2)


if __name__ == "__main__":
    '''
    main loop
    '''
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry()

    app = mianframe(root)
    # app.mainfrm.grid()
    root.mainloop()
