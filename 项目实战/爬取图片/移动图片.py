import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, docx, xlwt, \
    configparser, tqdm

import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageFont
from urllib import request
from email.mime.text import MIMEText
from email.utils import formataddr
from openpyxl import load_workbook
from fake_useragent import UserAgent
from datetime import datetime, timezone, timedelta
from concurrent.futures.thread import ThreadPoolExecutor
from lxml import etree
from docx import document
from docx.document import Document as Doc
from multiprocessing.dummy import Pool
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from PIL import Image
from hashlib import md5
from selenium.webdriver.common.keys import Keys

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
def spider(url):
    ua=UserAgent()
    headers={
        "User_Agent": ua.ie
    }
    res=requests.get(url=url,headers=headers)
    return res
   
#浏览器驱动路径
excutable_path="H:/测试/浏览器驱动/chromedriver.exe"

#无头浏览器
def options(excutable_path):
    chorme_options=Options()
    chorme_options.add_argument('--headless')
    chorme_options.add_argument('--disable-gpu')
    browser=webdriver.Chrome(executable_path=excutable_path,chrome_options=chorme_options)
    return browser
"""
def config_read(config_path):
    conf=configparser.ConfigParser()
    conf.read(config_path)
    root=conf.get("config","root")
    old_pic_path=conf.get("config", "old_pic_path")
    new_pic_path=conf.get("config","new_pic_path")
    config_dic={
        "root": root,
        "old_pic_path":old_pic_path,
        "new_pic_path":new_pic_path,
    }
    return config_dic


def config_write(config_path,root,old_pic_path,new_pic_path):
    conf=configparser.ConfigParser()
    conf.read(config_path)
    conf.set("config", "root", root)
    conf.set("config","old_pic_path",old_pic_path)
    conf.set("config", "new_pic_path", new_pic_path)
    with open(config_path,"r+") as fp:
        conf.write(fp,conf)
        fp.flush()


def move_pic_path(file_path,file_path_1,config_path):
    # 读取配置文件
    config_root=config_read(config_path)['root']    #待移动文件所处根目录
    old_pic_path = config_read(config_path)['old_pic_path']     #待移动文件路径
    new_pic_path=config_read(config_path)['new_pic_path']   #待移动文件将要移动的去移往的路径
    #判断是否默认路径
    if config_root=="0":
        config_root=f"{file_path}\\10012"
    if old_pic_path=="0":
        old_pic_path=f"{file_path}\\10012\\0.jpg"
    if new_pic_path=="0":
        new_pic_path=f"{file_path_1}\\10012_0.jpg"
    #判断文件夹是否存在
    if not os.path.exists(file_path_1):
        os.makedirs(file_path_1)
    #遍历目标文件列表
    pic_list=os.walk(file_path)
    #启动开关，刚开始遍历时状态为off,如果遍历到了目标文件就on
    start="off"
    for root,dirs,files in pic_list:
        #遍历到将要移动前往的目录
        if root==config_root or start=="on":
            dir=re.findall("H:\\\图片\\\mv\\\(.*)",root)[0]
            #将图片序号归零
            new_pic_num=0
            # 找到当前文件
            for file in files:
                old_pic_path=f"{root}\{file}"
                if os.path.isfile(old_pic_path) and os.path.exists(old_pic_path):
                    new_pic_path = f"{file_path_1}\{dir}_{new_pic_num}.jpg"
                    #对图片进行移动
                    shutil.copyfile(old_pic_path,new_pic_path)
                    #将图片序号加一
                    new_pic_num+=1
                    #将配置文件进行更新
                    config_write(config_path,root,old_pic_path,new_pic_path)
                    #下一步骤开关
                    start="on"
            print(f"{root}复制完成!")
    print("\n复制完成")




if __name__ == "__main__":
    file_path="H:\图片\mv图片"
    file_path_1="H:\图片\mv图片1"
    config_path="H:\图片\config.ini"
    file_num=0
    move_pic_path(file_path, file_path_1,config_path)

