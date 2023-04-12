import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy

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
from tkinter import messagebox, Button

def get_url_dic_list():
    url_dic_list=[]
    with open(page_url_path,"rt+",encoding="utf-8") as fp1:
        with open(detail_url_path, "rt+", encoding="utf-8") as fp2:
            page_url_list=fp1.readlines()
            detail_url_list = fp2.readlines()
            for index in range(max(len(page_url_list),len(detail_url_list))):
                try:
                    page_url=page_url_list[index].strip()
                except:
                    page_url=None
                try:
                    detail_url = detail_url_list[index].strip()
                except:
                    detail_url=None
                url_dic = {
                    "page_url": page_url,
                    "detail_url": detail_url
                }
                url_dic_list.append(url_dic)
    return url_dic_list


async def fetch(session,page_url=None,detail_url=None):
    if page_url:
        page_tree=await spider(session,page_url)
        await page_url_xpath(session,tree=page_tree,page_url=page_url)     #此函数会自动保存信息，无需save
    if detail_url:
        detail_tree=await spider(session,detail_url)
        info=await detail_url_xpath(tree=detail_tree,detail_url=detail_url)
        await save_file(info)


async def spider(session,url):
    if session and url:
        async with session.get(url=url, headers=headers,verify_ssl=False) as response:
            html=await response.text()
            tree=etree.HTML(html)
            response.close()
            return tree


async def page_url_xpath(session,tree,page_url):
    try:
        detail_urls=tree.xpath("//li[@class='layui-clear']/a/@href")
        for detail_url in detail_urls:
            #用于堵塞，避免爬取速度过快
            block()
            info=await detail_url_xpath(session,detail_url)
            # 将爬取到的文件写入excel
            await save_file(info)
        print(f"爬取完成:{page_url}")
    except:
        print(f"爬取失败:{page_url}")
        # await fail_url_save(page_url=page_url)

async def detail_url_xpath(session,detail_url):
    tree=spider(session=session,url=detail_url)
    port = re.findall("http://www.anbu0.com/(.*?).html", detail_url)[0]
    # 避免索引空列表报错问题
    # TODO 这部分xpath解析标签有问题，需要重做
    '''
    try:
        name = tree.xpath("//*div[@class='right']/h3/text()")[0]
    except:
        name = "无"
    try:
        t_pan = tree.xpath(f"//*[@id='post-{port}']/div[2]/p[5]/a/@href")[0]
    except:
        t_pan = "无"
    try:
        t_pwd = tree.xpath(f"//*[@id='post-{port}']/div[2]/p[5]/text()")[1].strip("(" and ")").split(":")[1]
    except:
        t_pwd = "无"
    try:
        b_pan = tree.xpath(f"//*[@id='post-{port}']/div[2]/p[6]/a/@href")[0]
    except:
        b_pan = "无"
    try:
        b_pwd = tree.xpath(f"//*[@id='post-{port}']/div[2]/p[6]/text()")[1].split("：")[1]
    except:
        b_pwd = "无"

    info = {
        "name": name,
        "t_pan": t_pan,
        "t_pwd": t_pwd,
        "b_pan": b_pan,
        "b_pwd": b_pwd,
    }
    return info
    '''

async def save_file(info):
    #将info管道内容拆分出来
    name=info["name"]
    #将解析出错的跳过保存
    if name=="无":
        return None
    t_pan=info["t_pan"]
    t_pwd=info["t_pwd"]
    b_pan=info["b_pan"]
    b_pwd=info["b_pwd"]
    text = f"\"游戏名:{name}\",\"百度网盘链接:{b_pan}\",\"百度网盘访问码:{b_pwd}\",\"天翼云链接:{t_pan}\",\"天翼云访问码:{t_pwd}\"\n"
    #将写入任务封装为save_file方法
    await write_to_txt(text,name)

async def write_to_txt(text,name):
    # 将info写入文件
    with open(CSV_PATH, "at+", encoding="GBK") as fp:
        fp.write(text)
        fp.flush()
        print(f"信息保存成功：{name}")

async def fail_url_save(page_url=None,detail_url=None):
    if page_url:
        page_url_text=f"{page_url}\n"
        with open(page_url_path,"at+",encoding="utf-8") as fp:
            fp.write(page_url_text)
            fp.flush()
    elif detail_url:
        detail_url_text=f"{detail_url}\n"
        with open(detail_url_path, "at+", encoding="utf-8") as fp:
            fp.write(detail_url_text)
            fp.flush()

#此处用于堵塞爬虫，以免被封ip
def block():
    time.sleep(0.75)

async def main():
    tasks=[]
    global ua
    global headers
    global CSV_PATH
    global EXCEL_PATH
    global page_url_path
    global detail_url_path
    ua = UserAgent()
    CSV_PATH="H:\项目\数据\save1.csv"
    EXCEL_PATH="H:\项目\数据\save1.xlsx"
    page_url_path = "H:\项目\数据\\fail_page_url.txt"
    detail_url_path = "H:\项目\数据\\fail_detail_url.txt"
    headers={
        "User_Agent":ua.firefox
    }
    url_dic_list=get_url_dic_list()
    async with aiohttp.ClientSession() as session:
        for url_dic in url_dic_list:
            page_url=url_dic["page_url"]
            detail_url=url_dic["detail_url"]
            tasks.append(asyncio.ensure_future(fetch(session,page_url,detail_url)))
        await asyncio.wait(tasks)

if __name__=="__main__":
    asyncio.run(main())

