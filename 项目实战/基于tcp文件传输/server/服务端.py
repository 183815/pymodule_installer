import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy, tkinter, chardet, windnd, socket, struct

import numpy as np
import pandas as pd
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
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from lxml import etree
from multiprocessing.dummy import Pool
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from PIL import Image
from hashlib import md5
from selenium.webdriver.common.keys import Keys
from scrapy import cmdline
from flask import Flask

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL

#同步爬虫
def spider(url):
    ua=UserAgent()
    headers={
        "User_Agent": ua.ie
    }
    res=requests.get(url=url,headers=headers)
    return res
   
#异步爬虫
async def spider(url):
ua=UserAgent()
headers={
    "User_Agent": ua.ie
}
with aiohttp.ClientSession as session:
    async with await session.get(url,headers) as res:
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
if __name__ == "__main__":
    #买手机
    phone=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    #绑定电话卡
    phone.bind(("127.0.0.1",80))
    #等待连接
    phone.listen(5)
    print("\r服务已开启，等待连接……",end="")
    #建立通讯循环
    while True:
        #获取连接客户端地址
        conn,client_addr=phone.accept()
        print(f"\r({client_addr})已建立连接，等待命令输入……")
        #1.收命令
        cmd=conn.recv(1024).decode('utf-8')
        if not cmd:break
        #2.解析命令,提取相应命令参数
        command=cmd.split(" ")[0]
        file_path=cmd.split(" ")[1]
        #3.将文件信息进行封装
        header_dic={
            "file_path":file_path,
            "file_size":os.path.getsize(file_path),
        }
        #4.将文件转为json格式并编码
        header_json=json.dumps(header_dic)
        header_bytes=header_json.encode("utf-8")
        # 5.发送报头长度
        conn.send(struct.pack("i",len(header_bytes)))
        # 6.发送报头
        conn.send(header_bytes)
        #7.发送文件
        if command=="get" and os.path.exists(file_path):
            print("文件发送中……")
            with open(file=file_path,mode="rb+") as fp:
                #如果文件相当大，不能一下全读出来！否则内存开销较大
                for line in fp:
                    conn.send(line)
            print("文件发送完成")
    conn.close()
    phone.close()


