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
from concurrent.futures.thread import ThreadPoolExecutor
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
excutable_path="H:\测试\浏览器驱动\chromedriver.exe"

#无头浏览器
def options(excutable_path):
    chorme_options=Options()
    chorme_options.add_argument('--headless')
    chorme_options.add_argument('--disable-gpu')
    browser=webdriver.Chrome(executable_path=excutable_path,chrome_options=chorme_options)
    return browser
"""
def read_episode_name():
    episode_file="H:\视频\episode_name.txt"
    with open(episode_file,"rt+",encoding="utf-8") as fp:
        epidsode_name_list=fp.readlines()
    return epidsode_name_list

if __name__ == "__main__":
    file_path=r"H:\视频\我的动漫\星游记"
    for root,dirs,files in os.walk(file_path):
        if files:
            episode_name_list = read_episode_name()
            for file in files:
                #改名
                episode_num = int(re.findall("\[QIYI]\[Rainbow Sea]\[(.*?)]\[GB]\[AVC_AAC]", file)[0])
                episode_name = episode_name_list[episode_num-1].strip()
                old_file_path = fr'{file_path}\{file}'
                new_file_path=fr'{file_path}\{episode_name}.flv'
                if old_file_path.endswith('.flv'):
                    os.renames(old_file_path,new_file_path)
                #忘加MP4后缀
                # if not file.endswith('.mp4'):
                #     new_file=f"{file}.mp4"
                #     new_file_path=fr'{file_path}\{new_file}'
                #     old_file_path=fr'{file_path}\{file}'
                #     os.renames(old_file_path,new_file_path)