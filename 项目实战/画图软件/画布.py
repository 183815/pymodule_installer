import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy, tkinter, chardet

from tkinter import *

class Application():
    def __init__(self):
        #设置画布属性
        self.width=300
        self.hight=300
        self.bg="black"
        #创建画布
        self.create_canvas()

    def create_canvas(self):
        canvas=Canvas(master=root,width=self.width,height=self.hight,bg=self.bg)
        canvas.pack(side="top")
        #创建按钮
        btn_start=Button(root,text="开始",name="start")
        btn_start.pack(side="left",padx="10")
        btn_pen=Button(root,text="画笔",name="start")
        btn_pen.pack(side="left",padx="10")
        btn_rectangle=Button(root,text="矩形",name="start")
        btn_rectangle.pack(side="left",padx=10)
        btn_cls=Button(root,text="清屏",name="start")
        btn_cls.pack(side="left",padx=10)
        btn_eraser=Button(root,text="橡皮擦",name="start")
        btn_eraser.pack(side="left",padx=10)
        btn_Line=Button(root,text="直线",name="start")
        btn_Line.pack(side="left",padx=10)
        btn_arrow=Button(root,text="箭头直线",name="start")
        btn_arrow.pack(side="left",padx=10)
        btn_color=Button(root,text="颜色",name="start")
        btn_color.pack(side="left",padx=10)

if __name__ == "__main__":
    root=Tk()
    root.geometry("500x500+200+200")
    root.title("CANVAS(画布)")
    root.iconbitmap("F:\图片\图标\月亮.ico")
    app=Application()
    root.mainloop()