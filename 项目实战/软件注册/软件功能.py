import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy, tkinter, chardet, windnd, socket
from tkinter import messagebox

import window
class Application(window.window):
    def __init__(self):
        #创建一个缓冲区
        self.buffer=None
        #创建一个容器存放用户名
        self.user_name = tkinter.StringVar(value=None)
        #创建一个容器存放密码
        self.pwd = tkinter.StringVar(value=None)
        #创建一个容器存放自动登录按钮值
        self.auto_login_value=tkinter.StringVar(value="None")
        #生成配置文件路径
        self.config_path=os.path.join(os.getcwd(),"config.ini")
        #读取配置文件
        self.read_config()
        #显示窗口
        self.window()

    def get_mysql(self):
        conf=configparser.ConfigParser()
        conf.read(filenames=self.config_path,encoding="utf-8")
        #获取所有用户信息
        self.user_list=conf.has_option()
        print(self.user_list)
        time.sleep(1000)

    def log_in_user_name_validate(self):
        user_name=self.entry_user_name.get()
        if user_name in self.user_list:
            label=tkinter.Label(master=self.frame1,text="用户名输入正确",fg="red",bg="blue")
            label.grid(row=0,column=2,sticky="W")
        else:
            label = tkinter.Label(master=self.frame1, text="用户名输入错误", fg="red",bg="blue")
            label.grid(row=0, column=2,sticky="W")

    def log_in_pwd_validate(self):
        pwd=self.entry_pwd.get()
        if not pwd.isdecimal():
            label1 = tkinter.Label(master=self.frame1, text="密码输入错误", fg="red", bg="blue")
            label1.grid(row=1, column=2, sticky="W")
        elif pwd>1000000 and pwd<999999:
            label2=tkinter.Label(master=self.frame1,text="密码输入正确",fg="red",bg="blue")
            label2.grid(row=1,column=2,sticky="W")

    def log_in_validate(self):
        #读取用户数据库进行登录验证
        self.get_mysql()
        self.log_in_user_name_validate()
        self.log_in_pwd_validate()

    def log_in(self):
        self.log_in_validate()


    def register(self):
        pass

    def read_config(self):
        try:
            conf=configparser.ConfigParser()
            conf.read(filenames=self.config_path,encoding="utf-8")
            self.auto_login_value.set(conf.get(section="软件设置",option="自动登录"))
            if self.auto_login_value.get()=="yes":
                self.user_name.set(conf.get(section="用户信息", option="用户名"))
                self.pwd.set(conf.get(section="用户信息", option="密码"))
        except:
            self.save_config()

    def save_config(self):
        conf=configparser.ConfigParser()
        #保存用户软件设置
        conf.add_section("软件设置")
        conf.set(section="软件设置",option="自动登录",value=self.auto_login_value.get())
        #保存用户信息
        conf.add_section("用户信息")
        conf.set(section="用户信息", option="用户名", value=self.user_name.get())
        conf.set(section="用户信息", option="密码", value=self.pwd.get())
        with open(file=self.config_path,mode="w+",encoding="utf-8") as fp:
            conf.write(fp=fp)

if __name__ == "__main__":
    root=tkinter.Tk()
    root.geometry("500x500")
    root.title("软件界面")
    app=Application()
    root.mainloop()