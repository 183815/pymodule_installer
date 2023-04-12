import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel

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
def spider(url):
    headers={
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res=requests.get(url=url,headers=headers)
    return res

#对简历url进行get请求下载
def get_resume(url,resume_num):
    res=spider(url)
    html_text=res.text
    tree=etree.HTML(html_text)
    resume_url=tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
    resume_name=tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]  #获取简历名称
    resume_name = resume_name.encode('iso-8859-1').decode('utf-8').strip()  # 对简历名称进行重新编码
    resume_path = "H:\简历\{}\{}.{}.rar".format(file_num, resume_num, resume_name)  # 对简历路径进行拼接
    res=spider(resume_url)
    html=res.content
    with open(resume_path,"wb") as fp:
        fp.write(html)
    print("{}————————下载成功".format(resume_path))


def x_path(file_num,page_url):
    # 对每页的url进行xpath解析
    file_path="H:\简历\{}".format(file_num)
    res=spider(page_url)
    html=res.text
    tree=etree.HTML(html)
    #对每页的简历都新建一个文件夹
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    #对每张简历都标个序号
    resume_num = 0
    # #对li列表进行xpath解析
    li=tree.xpath('//*[@id="container"]')[0]
    resume_hrefs=li.xpath('.//div/a/@href')
    for resume_href in resume_hrefs:
        resume_url="https:{}".format(resume_href)     #对简历url进行拼接
        get_resume(resume_url,resume_num) #下载简历
        resume_num += 1    #简历序列号+1


if __name__ == "__main__":
    file_num=0  #文件夹号
    page_num=1 #页号
    total_page=20   #爬取的总页数
    url="https://sc.chinaz.com/jianli/free.html"
    file_num=int(input("请问您想从哪页开始爬取？"))
    total_page=int(input("请问您想爬取多少页数据?"))+1
    for page_num in range(1,total_page):
        if page_num>1:
            url="https://sc.chinaz.com/jianli/free_{}.html".format(page_num)
        x_path(file_num,url)
        file_num+=1