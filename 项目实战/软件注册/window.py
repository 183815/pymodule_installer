import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy, tkinter, chardet, windnd, socket


class window:
    def window(self):
        self.frame1=tkinter.Frame(root,bg="blue",width=500,height=400,padx=120,pady=200)
        self.frame1.grid(row=0,column=0,sticky="NSEW")
        #获取用户名
        label_user=tkinter.Label(self.frame1,text="用户名")
        label_user.grid(row=0,column=0,padx=2,pady=2,sticky="NSEW")
        self.entry_user_name=tkinter.Entry(self.frame1,width=20,bg="yellow",highlightcolor="blue",textvariable=self.user_name,validate="all",validatecommand=self.log_in_user_name_validate)
        self.entry_user_name.grid(row=0,column=1,padx=2,pady=2)
        #获取密码
        label_pwd=tkinter.Label(self.frame1,text="密码")
        label_pwd.grid(row=1,column=0,padx=2,pady=2,sticky="NSEW")
        self.entry_pwd=tkinter.Entry(self.frame1,width=20,bg="yellow",highlightcolor="blue",textvariable=self.pwd,validate="all",validatecommand=self.log_in_pwd_validate,show="*")
        self.entry_pwd.grid(row=1,column=1,padx=2,pady=2)
        #登录按钮
        buttom_log=tkinter.Button(self.frame1,text="登录",width=5,height=2,bg="white",fg="blue",cursor="heart",command=self.log_in)
        buttom_log.grid(row=2,column=1,sticky="W")
        #注册按钮
        buttom_regist=tkinter.Button(self.frame1,text="注册",width=5,height=2,bg="white",fg="blue",cursor="heart",command=self.register)
        buttom_regist.grid(row=2,column=1,sticky="E")
        #自动登录按钮
        self.auto_login=tkinter.Checkbutton(self.frame1,text="自动登录",fg="red",bg="white",onvalue="yes",offvalue="no",variable=self.auto_login_value,width=8,height=2,command=self.save_config)
        self.auto_login.grid(row=2,column=2,sticky="W")