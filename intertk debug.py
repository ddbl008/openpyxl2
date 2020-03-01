#coding:utf-8
import tkinter
# 导入TK的符号常亮
from tkinter.constants import *

def sendStr():
    print('Data Send Ok!')


#  实例化TK类，主窗口必须为.TK(),而其他子窗口为.Toplevel()
top = tkinter.Tk()

# 设置窗口的尺寸大小

#top.wm_geometry('900x480+1000+100')
top.wm_geometry()

# 不允许 改变 窗口的宽和高
top.wm_resizable(False,False)

# 设置窗口标题
top.title('TCP Server')

# 设置label标签
L1 = tkinter.Label(top, text='TCP Sever;\n20108/09/15',
                   width=15, justify=LEFT, relief=RIDGE, background='#6699ff', )\
    .pack_configure(anchor=S, side=LEFT, ipady=2, pady=2, fill=NONE)

# 设置容器
frame1 = tkinter.Frame(top,height=80,width=60,relief=RIDGE, bg='#ff3399',bd=5,borderwidth=4)
# 设置填充和布局
frame1.pack(fill=NONE,ipady=2,expand=False)

# 添加接收区文字标签
L2 = tkinter.Label(frame1,text='接\n收\n区',width=2, justify=LEFT, font=("宋体", 12, "bold"),)\
    .pack(padx=2,pady=40,side=LEFT,anchor=N)

# 添加接收区的文本框
txt1 = tkinter.Text(frame1,width = 40, height = 10).pack(padx=2,pady=10,side=RIGHT,anchor=N)


frame2 = tkinter.Frame(top, relief=RIDGE,bg='#3366ff')
frame2.pack(fill=X, padx=2,pady=10,side=LEFT)

# 加一个复选框，一个按键
chk_text = 'Hex Display'
int_if_choise = tkinter.IntVar()
chk1 = tkinter.Checkbutton(frame2,text=chk_text,font=('黑体',12),variable=int_if_choise,onvalue='OK',offvalue='NO')
chk1.pack(fill=NONE,side=LEFT,padx=2,pady=10)
print('shuchu:',int_if_choise)


# 设置容器
frame3 = tkinter.Frame(top,height=120,width=60,relief=RIDGE, bg='#ff3399',bd=5,borderwidth=4)
# 设置填充和布局
frame3.pack(fill=X,ipady=2,expand=False)

# 设置字符串变量
ServerReceiveVar = tkinter.StringVar(top,'')

L3 = tkinter.Label(frame3, text='Cache&Input:',font=('黑体',12))
L3.pack(fill=NONE, expand=NO, side=TOP, anchor=W, padx=2,pady=10)



txt2 = tkinter.Text(frame3, height = 2, width = 30).pack(padx=2, pady=2, ipady=4, side=LEFT, anchor=N)


button1 = tkinter.Button(frame3,text='Send Str', command=sendStr).pack(side=TOP, anchor=W, padx=2, pady=4)

# IP 列表
button2 = tkinter.Button(frame3,text="Exit",command=top.destroy).pack(side=TOP, anchor=N, padx=2, pady=10)

top.mainloop()