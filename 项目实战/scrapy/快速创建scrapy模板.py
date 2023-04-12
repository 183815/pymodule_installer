import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, docx, xlwt, \
    configparser, tqdm, cmd

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
def config(scrapy_path,project_name):
    judge=input("是否自动修改配置?是：yes|y   否：no|n\n请选择:")
    if judge=='yes'or judge=='y'or judge== '是':
        setting_path=f'{scrapy_path}/{project_name}/{project_name}/settings.py'
        pipelines_path=f'{scrapy_path}/{project_name}/{project_name}/pipelines.py'
        pic_judge=input("是否需要保存图片文件?是：yes|y   否：no|n\n请选择:")
        #修改items配置
        with open(setting_path,"rt+",encoding="utf-8") as fp:
            lines=fp.readlines()
            for i in range(len(lines)):
                lines[i]=lines[i].replace('ROBOTSTXT_OBEY = True','ROBOTSTXT_OBEY = False')
                if "ITEM_PIPELINES" in lines[i] or "DOWNLOADER_MIDDLEWARES" in lines[i]:
                    lines[i]=lines[i].strip('# ')
                    if pic_judge == 'yes' or pic_judge == 'y' or pic_judge == '是':
                        lines[i+1] = lines[i+1].replace(lines[i+1],f'\'{project_name}.pipelines.image_pipelines\': 300,\n')
                    lines[i+2] = lines[i+2].strip('# ')
        #修改settings.py文件
        with open(setting_path,"wt+",encoding="utf-8") as fp:
            text1="from fake_useragent import UserAgent\nua=UserAgent()\nUSER_AGENT = ua.ie\nLOG_LEVEL='ERROR'\n"
            fp.write(text1)
            for line in lines:
                fp.write(line)
            if pic_judge == 'yes' or pic_judge == 'y' or pic_judge == '是':
                pic_path = input("请输入文件保存路径:")
                text2=f"IMAGES_STORE={pic_path}\n"
                fp.write(text2)
        #修改pipelines.py文件
        with open(pipelines_path,"wt",encoding="utf-8") as fp:
            text3="from scrapy.pipelines.images import ImagesPipeline\nimport scrapy\nclass image_pipelines(ImagesPipeline):\n    def get_media_requests(self, item, info):\n        yield scrapy.Request(item[''])"
            fp.write(text3)
        print("配置成功")
    else:
        print("默认配置")



def INPUT():
    project_name=input("请输入scrapy项目名:").split()[0]
    spider_name = input("请输入爬虫名称:").split()[0]
    if project_name==spider_name:
        print('项目名和爬虫名不能相同，请重新输入!')
        os.system('cls')
        return INPUT()
    else:
        main_url = input("请输入网址:").split()[0]
        name = {
            'project_name': project_name,
            'spider_name': spider_name,
            'main_url':main_url,
        }
        return name

#创建主体项目文件
def start_project(scrapy_path,project_name,spider_name,main_url):
    # 创建scrapy工程
    man1 = f'scrapy startproject {project_name}'
    os.system(man1)
    # 创建爬虫文件
    man2 = f'scrapy genspider {spider_name} {main_url}'
    os.system(man2)
    # 移动爬虫文件
    shutil.move(f'{scrapy_path}/{spider_name}.py',
                f'{scrapy_path}/{project_name}/{project_name}/spiders/{spider_name}.py')
    # 创建主文件
    with open(f'{scrapy_path}/{project_name}/main.py', "w+", encoding="utf-8") as fp:
        text = f"from scrapy import cmdline\ncmdline.execute('scrapy crawl {spider_name}'.split())"
        fp.write(text)
    print("scrapy框架创建成功！".strip())


if __name__ == "__main__":
    scrapy_path = os.getcwd()
    name=INPUT()
    project_name =name['project_name']
    spider_name =name['spider_name']
    main_url=name['main_url']
    start_project(scrapy_path,project_name,spider_name,main_url)
    config(scrapy_path, project_name)