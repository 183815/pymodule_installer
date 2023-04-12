import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle,aiohttp,asyncio

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
from aiohttp import ClientSession

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""


def spider(url):
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    return res


# 对图片url进行get请求下载
def get_img(img_url, img_path):
    res = spider(img_url)
    if res.status_code==200:
        html = res.content
        with open(img_path, "wb") as fp:
            fp.write(html)
    else:
        print("{}下载失败！".format(img_url))


def x_path(file_num, page_url):
    # 对每页的url进行xpath解析
    file_path = r"H:\图片\4k\{}".format(file_num)
    res = requests.get(url=page_url, headers=headers)
    html = res.text
    tree = etree.HTML(html)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    # 对每页的图片都新建一个文件夹
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    # 对每张图片都标个序号
    img_num = 0
    # 对li列表进行xpath解析
    for li in li_list:
        img_detail_url = "https://pic.netbian.com/{}".format(li.xpath('./a/@href')[0])
        html = spider(img_detail_url).text
        tree = etree.HTML(html)
        img_src = tree.xpath('//*[@id="img"]/img/@src')[0]  # 获取图片src
        img_name = tree.xpath('//*[@id="img"]/img/@alt')[0]  # 获取图片名称
        img_name = img_name.encode('iso-8859-1').decode('GBK').replace(" ", "_")  # 对图片名称进行重新编码
        img_path = r"H:\图片\4k\{}\{}.{}.jpg".format(file_num, img_num, img_name)  # 对图片路径进行拼接
        img_url = "https://pic.netbian.com{}".format(img_src)  # 对图片url进行拼接
        get_img(img_url,img_path) #下载图片
        print("{}--下载成功".format(img_path,img_url))
        img_num += 1  # 图片序列号+1


def input_judge(object, decimal, str):
    ip = int(input(object))
    if decimal and isinstance(ip, int):
        return int(ip)
    elif str and isinstance(ip, str):
        return ip
    else:
        print("输入错误")
        return None


if __name__ == "__main__":
    file_num = 0  # 文件夹号
    page_num = 1  # 页号
    url = "https://pic.netbian.com/4kmeinv/"
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    index = int(input("请输入一共爬取页数："))
    page_num = int(input("请输入爬取起始页："))
    # 不断提取每页的url
    for i in range(index):
        #拼接每页url
        if page_num > 1:
            page_url = "{}index_{}.html".format(url, page_num)
        else:
            page_num = 1
            page_url = "{}index.html".format(url)
        # 对每页的url进行xpath解析
        file_num = page_num - 1
        page_num += 1
        x_path(file_num, page_url)
    print("请求下载完成!")