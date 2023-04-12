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
    #买电话
    phone=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    #打电话
    phone.connect(("127.0.0.1",80))
    while True:
        #1.发命令
        cmd=input("请输入命令:").strip()
        if not cmd:continue
        phone.send(cmd.encode("utf-8"))
        #2.以写的方式打开文件，接受服务端发来的文件内容写入客户端新文件
        #先接收报头长度
        header_size_bytes=phone.recv(4)
        header_size=struct.unpack("i",header_size_bytes)[0]
        #再收报头
        header_bytes=phone.recv(header_size)
        #从报头中解析出文件的描述信息
        header_json=header_bytes.decode("utf-8")
        header_dic=json.loads(header_json)
        file_path=header_dic["file_path"]
        file_size=header_dic["file_size"]
        #接收真实数据,并写入文件
        with open(file=file_path,mode="wb+") as fp:
            recv_size=0
            print("文件接收中……")
            while recv_size < file_size:
                line=phone.recv(1024)
                recv_size += len(line)
                fp.write(line)
                fp.flush()
            print("文件接收完成")
    phone.close()
