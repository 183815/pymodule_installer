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
from lxml import etree

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""


def html_file(file_path, html):
    with open(file_path, "wb") as fp:
        fp.write(html)


def get_elem(elem_list, elem_path):
    fp = open(elem_path, "w", encoding="utf-8")
    for elem in elem_list:
        fp.write(f"{elem}\n")
    fp.close()


if __name__ == "__main__":
    file_path = "H://测试/章节.txt"
    book_path = "H://测试/三国演义.txt"
    elem_path = "H://测试/获取元素.txt"
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    html = res.content
    html_file(file_path, html)

    # xpath解析
    # parser=etree.HTMLParser(encoding="utf-8")
    # tree=etree.parse(file_path,parser=parser)
    # result=tree.xpath('//div[@class="book-mulu"]//li/a/text()')
    # get_elem(result,elem_path)
    # print(result)

    # bs4解析
    # with open(file_path, "rb") as fp:
    #     soup = BeautifulSoup(fp, 'lxml')
    #     # Tag=soup.find('li',id="top_bar")
    #     # Tag=soup.find_all("li")
    #     Tag = soup.select(".top_bar")
    #     print(Tag)
