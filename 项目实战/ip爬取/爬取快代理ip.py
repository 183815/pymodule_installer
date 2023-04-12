import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, docx, xlwt, \
    configparser, tqdm

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
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from lxml import etree
from docx import document
from docx.document import Document as Doc
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

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
def spider(url):
    ua=UserAgent()
    headers={
        "User_Agent": ua.ie
    }
    res=requests.get(url=url,headers=headers)
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
async def create_task(url):
    #只能创建一个端口
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.gather(fetch(session,url))]
        await asyncio.wait(tasks)

async def spider(session,url):
    ua=UserAgent()
    headers={
        "User_Agent":ua.firefox
    }
    async with session.get(url=url,headers=headers,verify_ssl=False) as response:
        html=await response.text()
        tree = etree.HTML(html)
        return tree

async def fetch(session,url):
    tree=await spider(session,url)
    tr_list=tree.xpath("//*[@id='list']/table//tr")
    del (tr_list[0])
    for tr in tr_list:
        ip=tr.xpath("./td[1]/text()")[0]
        port=tr.xpath("./td[2]/text()")[0]
        type=tr.xpath("./td[4]/text()")[0]
        response_time=float(tr.xpath("./td[6]/text()")[0].strip("秒"))
        if response_time<3:
            if type=="HTTP":
                proxy=f"HTTP://{ip}:{port}"
                # proxy= {
                #     "http":f"http://{ip}:{port}"
                # }
            elif type=="HTTPS":
                proxy=f"HTTPs://{ip}:{port}"
                # proxy= {
                #     "https":f"https://{ip}:{port}"
                # }
            PROXIES.append(proxy)
    await save_file(PROXIES)


async def save_file(PROXIES):
    with open(FILEPATH,"wt+",encoding="utf-8") as fp:
        for proxy in PROXIES:
            text=f"{proxy}\n"
            fp.write(text)
            fp.flush()

if __name__ == "__main__":
    global url
    global test_url
    global FILEPATH
    global PROXIES
    url="https://free.kuaidaili.com/free/inha/"
    test_url="https://pan.baidu.com"
    FILEPATH="H:\项目\数据\ProxyAgent.txt"
    PROXIES=[]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(create_task(url))