import turtle

import os

import turtle as t
import time

# file=open("output.txt",mode="r")
# list_srt=file.readlines()
#
# for i in list_srt:
#     print(i)
#
# rad=360/len(list_srt)
# dis=400
# radius=50
#
# n=len(list_srt)
# turtle.color('orange')
# turtle.pensize(3)
# turtle.circle(radius*2)
#
#
# t.penup()
# t.left(90)
# t.forward(100)
# t.pendown()
# t.write(list_srt[0].split(',')[0], font=('Arial', 15, 'normal'))
# for i in range(0,n-1):
#     t.left(rad)
#     t.penup()
#     t.forward(4*rad)
#     t.write(list_srt[i].split(',')[1], font=('Arial', 15, 'normal'))
#     t.pendown()
#
#
#     if list_srt[i].split(',')[2].split("'")[1]=="16":
#         print("get 15")
#         t.pensize(10)
#     if list_srt[i].split(',')[2].split("'")[1] == "4":
#         t.pensize(5)
#     if list_srt[i].split(',')[2].split("'")[1]=="1":
#         t.pensize(2.5)
#
#
#     t.forward(dis-4*rad)
#     t.pensize(3)
#
#     t.forward(radius)
#     t.write(list_srt[i].split(',')[3],font=('Arial', 20, 'normal'))
#     t.backward(radius)
#
#
#     t.right(90)
#
#     t.write(list_srt[i].split(',')[4], font=('Arial', 15, 'normal'))
#     t.circle(radius)
#     t.left(90)
#     t.penup()
#     t.backward(dis)
#     t.pendown()
#     t.position()
#
#
#
#
# print(type(t.position()))
# t.done()
#
#
#
# # turtle.circle(150)
# # turtle.penup()
# # turtle.goto(0, -100)
# # turtle.pendown()
# # turtle.circle(100)
# # t.penup()
# # t.goto(100, 500)
# # t.pendown()
# # t.goto(-100, 300)
# t.done()


# turtle.circle(150)



#
# for i in list_srt:
#     print(i)

class mt:
    @classmethod
    def line(cls,long,des,b_long=0,**kwr):
        cls.move(b_long)
        t.forward(long/2)
        t.write(des)
        t.forward(long / 2)
        cls.move(b_long)

    @classmethod
    def dbouleline(cls,long,des1,des2,b_xlong=0,b_ylong=0,**kwr):
        t.right(90)
        cls.move(b_ylong)
        t.left(20)
        cls.move(b_xlong)
        t.forward(long/2)
        t.write(des1)
        t.forward(long/2)
        cls.move(b_xlong)
        t.left(90)
        cls.move(2*b_ylong)
        t.left(90)
        cls.move(b_xlong)
        t.forward(long / 2)
        t.write(des2)
        t.forward(long / 2)
        t.left(90)
        cls.move(b_ylong)
        t.left(90)
        cls.move(long+b_xlong)

    @classmethod
    def end(cls):
        t.done()

    @classmethod
    def left(cls,rad):
        t.left(rad)

    @classmethod
    def right(cls, rad):
        t.left(rad)

    @classmethod
    def move(cls,dis):
        t.penup()
        t.forward(dis)
        t.pendown()

    @classmethod
    def cir(cls,rad,des="circle"):

        t.write(des)
        t.right(90)
        cls.move(rad)
        t.left(90)
        t.circle(rad)
        t.left(90)
        cls.move(rad)
        t.right(90)
        # t.left(180)
        # cls.move(rad)
        # t.left(90)

    @classmethod
    def fallout_line(cls, rad,dis, des="fallout line",**kwr):
        t.left(rad)
        if "bk_len" in kwr.keys():
            cls.move(kwr["bk_len"])
            t.forward(dis)
            t.write(des)
            t.forward(dis)
            cls.move(kwr["bk_len"])
        else:
            t.forward(dis)
            t.write(des)
            t.forward(dis)

        t.penup()
        t.setpos(0,0)
        t.pendown()
        t.right(rad)

    @classmethod
    def fallout_cirle(cls, rad, r,dis, des="fallout circle", **kwr):
        t.left(rad)
        cls.move(dis)
        t.write(des)
        t.left(180)
        cls.move(r)
        t.left(90)
        t.circle(r)
        t.left(90)
        t.penup()
        t.setpos(0, 0)
        t.pendown()
        t.right(rad)



        pass

# turtle.speed()
# “fastest”: 0
#
# “fast”: 10
#
# “normal”: 6
#
# “slow”: 3
#
# “slowest”: 1
#
# turtle.Turtle().screen.delay(0)
#最快速度显示
#测试用例
#t.speed("fastest")
turtle.Turtle().screen.delay(2)
mt.fallout_line(90,100)
mt.fallout_cirle(0,100,250)
mt.fallout_cirle(90,100,250)
mt.fallout_cirle(180,100,250)

#mt.move(100)
mt.fallout_line(135,250)
# mt.cir(50)
# t.right(30)
# for i in range (0,8):
#
#
#     t.left(30)
#     #mt.line(100,"hello",50)
#     mt.dbouleline(100, "line1", "line2", 50, 7)
#     mt.cir(50)
#     t.penup()
#     t.setx(0)
#     t.sety(0)
#     t.pendown()
#
#
#
# mt.dbouleline(100,"line1","line2",10,10)

mt.end()