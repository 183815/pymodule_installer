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

def get_session(url):
    data = {
        "action": "user_login",
        "username": "q175219",
        "password": "568568"
    }
    # 实例化一个session对象
    session = requests.session()
    # 获取目标session会话（其中包含cookies）
    # 注意：该会话不能获取网页数据，无需赋值，只能重新进行get请求
    session.post(url=url, headers=headers, data=data)
    return session

def get_detail_url(session,url):
    res=session.get(url)
    html=res.text
    port_list = re.findall("<article id=\"post-(.*?)\"", html)
    tree=etree.HTML(html)
    game_list=tree.xpath("/html/body/div[1]/div[2]/div/main/div[2]/div/div/div/div/main/div[1]")
    for game in game_list:
        for port in port_list:
            try:
                detail_url=game.xpath(f"//*[@id='post-{port}']/div[1]/div[1]/a/@href")[0]
                xpath_detail_url(detail_url,port)
            except:
                pass


def xpath_detail_url(url,port):
    # session=get_session(url)
    # res=session.get(url=url,headers=headers)
    # html=res.text
    # tree=etree.HTML(html)
    post_pan_url=f"https://86000k.com/go?post_id={port}"
    session=get_session(post_pan_url)
    res=session.get(post_pan_url,headers=headers)
    print(res.text)

if __name__ == "__main__":
    global headers
    ua = UserAgent()
    headers = {
        "User_Agent": ua.firefox
    }
    url = "https://86000k.com/"
    for page in range(1,10):
        if page<2:
            new_url=url
        else:
            new_url=f"{url}page/{page}/"
        session = get_session(new_url)
        get_detail_url(session,new_url)
    # 对目标网页进行请求

