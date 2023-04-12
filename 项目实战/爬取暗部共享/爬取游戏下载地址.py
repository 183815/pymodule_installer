import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, docx, xlwt

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
from multiprocessing.dummy import Pool
from selenium import webdriver
from openpyxl import Workbook

# async def time_count(fetch):
#     t1=time.time()
#     fetch()
#     t2=time.time()
#     print(f"程序总共耗时:{int(t2-t1)}秒")


async def fetch():
    page_url = "http://www.anbu0.com/pc/pcgame"
    urls = [f"{page_url}/page/{index}" for index in range(2, PAGE_NUM)]
    urls.append(page_url)
    #创建一个端口session
    async with aiohttp.ClientSession() as session:
        #将这个session端口和url传递给create_task
        tasks = [asyncio.ensure_future(create_task(session,url=url)) for url in urls]
        #将需要io的任务挂起
        await asyncio.wait(tasks)

async def create_task(session,url):
    tree=await spider(session,url)
    await url_xpath(session,tree,url)

async def spider(session, url):
    headers = {
        "User_Agent": Ua.firefox
    }
    #IP代理
    # proxy={
    #     "http":"http://58.20.232.245:9091",
    #     "http":"http://218.75.102.19:8000"
    # }
    #此处可设置超时时长timeout
    async with session.get(url=url, headers=headers,timeout=10, verify_ssl=False) as response:
        html = await response.text()
        tree = etree.HTML(html)
        response.close()
        return tree

async def url_xpath(session,tree,url):
    try:
        detail_urls=tree.xpath("//li[@class='layui-clear']/a/@href")
        for detail_url in detail_urls:
            #用于堵塞，避免爬取速度过快
            block()
            info=await detail_url_xpath(session,detail_url)
            # 将爬取到的文件写入excel
            await save_file(info)
        print(f"爬取完成:{url}")
    except:
        print(f"爬取失败:{url}")
        await fail_url_save(page_url=url)

async def detail_url_xpath(session,detail_url):
    try:
        tree=await spider(session,detail_url)
    except:
        print(f"获取失败:{detail_url}")
        await fail_url_save(detail_url=detail_url)
        return None
    port = re.findall("http://www.anbu0.com/(.*?).html", detail_url)[0]
    #避免索引空列表报错问题
    try:
        name= tree.xpath("//*[@class='right']//h3/text()")[0]
    except:
        name ="无"
    try:
        t_pan= tree.xpath(f"//*[@id='post-{port}']/div[2]/p[5]/a/@href")[0]
    except:
        t_pan = "无"
    try:
        t_pwd= tree.xpath(f"//*[@id='post-{port}']/div[2]/p[5]/text()")[1].strip("(" and ")").split(":")[1]
    except:
        t_pwd = "无"
    try:
        b_pan= tree.xpath(f"//*[@id='post-{port}']/div[2]/p[6]/a/@href")[0]
    except:
        b_pan = "无"
    try:
        b_pwd= tree.xpath(f"//*[@id='post-{port}']/div[2]/p[6]/text()")[1].split("：")[1]
    except:
        b_pwd = "无"
    try:
        active_code= tree.xpath(f"//*[@id='post-{port}']/div[2]/p[4]/span/text()")[0].lstrip("激活码：")
    except:
        active_code = "无"

    info = {
        "name": name,
        "detail_url":detail_url,
        "t_pan": t_pan,
        "t_pwd": t_pwd,
        "b_pan": b_pan,
        "b_pwd": b_pwd,
        "active_code":active_code,
    }
    return info


async def fail_url_save(page_url=None,detail_url=None):
    if page_url:
        page_url_text=f"{page_url}\n"
        page_url_path="H:\项目\数据\\fail_page_url.txt"
        with open(page_url_path,"at+",encoding="utf-8") as fp:
            fp.write(page_url_text)
            fp.flush()
    elif detail_url:
        detail_url_text=f"{detail_url}\n"
        detail_url_path = "H:\项目\数据\\fail_detail_url.txt"
        with open(detail_url_path, "at+", encoding="utf-8") as fp:
            fp.write(detail_url_text)
            fp.flush()

#此处用于堵塞爬虫，以免被封ip
def block():
    time.sleep(0.6)


async def save_file(info):
    #将info管道内容拆分出来
    name=info["name"]
    #将解析出错的跳过保存
    if name=="无":
        return None
    detail_url=info["detail_url"]
    t_pan=info["t_pan"]
    t_pwd=info["t_pwd"]
    b_pan=info["b_pan"]
    b_pwd=info["b_pwd"]
    active_code=info["active_code"]
    text = f"\"游戏名:{name}\",\"详情请见:{detail_url}\",\"百度网盘链接:{b_pan}\",\"百度网盘访问码:{b_pwd}\",\"天翼云链接:{t_pan}\",\"天翼云访问码:{t_pwd}\",\"激活码:{active_code}\"\n"
    #将写入任务封装为save_file方法
    await write_to_txt(text,name)

async def write_to_txt(text,name):
    # 将info写入文件
    with open(CSV_PATH, "at+", encoding="GBK") as fp:
        fp.write(text)
        fp.flush()
        print(f"信息保存成功：{name}")

def form_turn():
    csv=pd.read_csv(CSV_PATH,encoding="GBK")
    csv.to_excel(EXCEL_PATH)
    os.remove(CSV_PATH)
    print("程序运行结束！")

if __name__=="__main__":
    global CSV_PATH
    global EXCEL_PATH
    global PAGE_NUM
    global Ua
    CSV_PATH="H:\项目\数据\save.csv"
    EXCEL_PATH="H:\项目\数据\save.xlsx"
    Ua = UserAgent()
    try:
        PAGE_NUM=int(input("获取页数："))+1
        asyncio.run(fetch())
        form_turn()
    except:
        print("输入异常")
