# -*- coding: utf-8 -*-
import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy, tkinter, chardet, windnd, socket, struct

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from threading import Thread

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
def func1(a):
    print(f"1:{a}")

def func2(a):
    print(f"2:{a}")

def get_char():
    return input()

if __name__ == "__main__":
    a=get_char()
    t1=Thread(target=func1(a))
    t1.start()
    t1.join(timeout=1)
    t2=Thread(target=func2(a))
    t2.start()
    t2.join(timeout=1)
