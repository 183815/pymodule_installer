import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, numpy, \
    ez_setup, ffmpeg, json, datetime, re, bs4, lxml

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

#基于bs4的数据解析
"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""
#写入文本数据
def save_file(file_name,file_object):
    with open(file_name,mode="w",encoding="UTF-8") as fp:
        fp.write(file_object)

if __name__ == "__main__":
    file_name="H:/测试/down_load.txt"
    ua = UserAgent()
    url = "https://www.shicimingju.com/1870.html"
    headers = {"User_Agent": ua.ie}
    page_text= requests.get(url=url,headers=headers).text
    #实例化BeautifulSoup对象
    soup=BeautifulSoup(page_text,"lxml")
    li_list=soup.select(".book-mulu > ul > li")
    # 写入文件
    fp = open(file_name,"w",encoding="utf-8")
    # 数据解析
    for li in li_list:
        title=li.a.string
        detail_url="{}{}".format("https://www.shicimingju.com",li.a["href"])
        #对详情页发请求，解析出章节内容
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关章节内容
        detail_soup=BeautifulSoup(detail_page_text,"lxml")
        detail_soup.find("div",class_="chapter_content")
        div_tag=detail_soup.find("div",class_="chapter_content")
        #解析到章节内容
        content=div_tag.text
        file_name_object="{}:{}\n".format(title,content)
        fp.write(title)
        print(title+"爬取成功!")
    fp.close()