import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql

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

from proxy_interface import get_proxy

def detail_url_xpath(detail_url):
    tree=spider(detail_url)
    port=re.findall("http://www.anbu0.com/(.*?).html",detail_url)[0]
    name=tree.xpath("//*[@class='right']//h3/text()")[0]
    t_pan=tree.xpath(f"//*[@id='post-{port}']/div[2]/p[5]/a/@href")[0]
    t_pwd=tree.xpath(f"//*[@id='post-{port}']/div[2]/p[5]/text()")[1].strip("(" and ")").split(":")[1]
    b_pan=tree.xpath(f"//*[@id='post-{port}']/div[2]/p[6]/a/@href")[0]
    b_pwd = tree.xpath(f"//*[@id='post-{port}']/div[2]/p[6]/text()")[1].split("：")[1]
    info={
        "name":name,
        "t_pan":t_pan,
        "t_pwd":t_pwd,
        "b_pan":b_pan,
        "b_pwd":b_pwd,
    }
    return info


def url_xpath(tree):
    detail_urls=tree.xpath("//li[@class='layui-clear']/a/@href")
    for detail_url in detail_urls:
        info=detail_url_xpath(detail_url)
        pprint.pprint(info)



def spider(url):
    ua=UserAgent()
    headers={
        "User_Agent":ua.firefox
    }
    proxies={
        "http":Proxy.get_newest_proxy()
    }
    response=requests.get(url=url,headers=headers,proxies=proxies)
    html=response.text
    tree=etree.HTML(html)
    return tree


if __name__ == "__main__":
    global Proxy
    Proxy=get_proxy()
    url = "http://www.anbu0.com/pc/pcgame"
    tree=spider(url)
    url_xpath(tree)