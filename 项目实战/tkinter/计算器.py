import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql

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
from tkinter import *
from tkinter.filedialog import *
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

def menu(root):
    sign_text=("+","-","×","÷")
    num_text=((1,2,3,4,5),
              (6,7,8,9,0))
    lable01=Label(text="计算器",bg="blue",fg="white").pack(side="top")
    Entry(root).pack(side="top")
    for index in range(len(sign_text)):
        sign_btn=Button(root,text=sign_text[index],width=2,height=2,bg="black",fg="white",anchor="ne",overrelief="flat").pack(side="left")
    for index in range(len(num_text)):
        num_btn=Button(root,text=num_text[index],width=2,height=2,bg="black",fg="white",anchor="ne",overrelief="flat").pack(side="left")




if __name__=="__main__":
    root=Tk()
    root.geometry("500x500")
    menu(root)
    root.mainloop()

