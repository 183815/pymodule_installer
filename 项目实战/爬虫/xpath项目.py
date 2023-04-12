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
def xpath_analy(file_name,xpath_analy):
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse(file_name, parser=parser)
    result_list = tree.xpath(xpath_analy)
    return result_list


def save_file(file_name,html):
    with open(file_name,"wb") as fp:
        fp.write(html)


def get_html(page_num):
    url = f"https://www.shicimingju.com/book/sanguoyanyi/{page_num}.html"
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    html = res.content
    return html

def write_book(book_path,titles,result_list):
    with open(book_path,"at",encoding="utf-8") as fp:
        for result in result_list:
            for title in titles:
                fp.write(f"{title.strip}\n{result.strip}")


if __name__ == "__main__":
    book_path = "H://测试/三国演义.txt"
    file_name="H://测试/html.txt"
    page_nums=10
    for page_num in range(1,page_nums):
        html=get_html(page_num)
        save_file(file_name,html)
        result_list=xpath_analy(file_name,'//div[@class="chapter_content"]/text()')
        titles=xpath_analy(file_name,'//div[@class="card bookmark-list"]/h1/text()')
        write_book(book_path,titles,result_list)