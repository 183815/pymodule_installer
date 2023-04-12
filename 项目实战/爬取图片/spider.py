import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle
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

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""


#从本地文件获取php地址
def get_php():
    php_lines=[]
    with open(r"H:/测试/已测试.txt",mode="rt",encoding="utf-8") as file:
        lines=file.readlines()
    for line in lines:
        line=line.strip()
        php_lines.append(line)
    return php_lines


# 获取respons响应
def spider(url):
    ua=UserAgent()
    headers={
        "User_Agent": ua.ie
    }
    res=requests.get(url=url,headers=headers)
    return res


#xpath解析出图片url
def get_pic_url(url):
    res=spider(url)
    img_url_list=[]
    html_text = res.text
    tree = etree.HTML(html_text)
    img_list = tree.xpath('/html/body/div[1]/div/div[1]/p[1]/img')
    img_num = 0
    for img_wb in img_list:
        img_url = img_wb.xpath('./@src')[0]
        print(img_url)
        img_url_list.append(img_url)
    return img_url_list


#下载图片
def down_load(pic_file_num,pic_num,url):
    pic_file_path="H:/图片/{}".format(pic_file_num)
    pic_path="H:/图片/{}/{}.jpg".format(pic_file_num,pic_num)
    if not os.path.exists(pic_file_path):
        os.makedirs(pic_file_path)
    res=spider(url)
    html = res.content
    with open(pic_path,"wb") as fp:
        fp.write(html)



