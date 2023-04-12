import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, numpy, \
    ez_setup, ffmpeg, json, datetime, re, configparser
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

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""
def spider(url):
    res = requests.get(
        url=url,
        headers={
            "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }
    )
    return res


def wb_exists_judge(url,num):
    res=spider(url)
    if res.status_code!=200 :
        print("{}--404 not found".format(num))
    else:
        print("{}--{}".format(num,url))
        file1.write("{}\n".format(url))
        file2.write("{}\n".format(url))
        file1.flush()
        file2.flush()
        config_write_file(str(num+1))


def config_read_file():
    config_path="H:/测试/pic_config.ini"
    conf=configparser.ConfigParser()
    conf.read(config_path)
    file_num=conf.getint('config','start_pic_num')
    return file_num

def config_write_file(start_pic_num):
    config_path="H:/测试/pic_config.ini"
    conf=configparser.ConfigParser()
    conf.read(config_path)
    conf.set('config','start_pic_num',start_pic_num)
    with open(config_path,"r+") as fp:
        conf.write(fp)


if __name__=="__main__":
    wb_head="http://1.weihuasdgs.com.cn/1/"
    num=config_read_file()
    Pool = ThreadPoolExecutor(1000)
    with open(r"H:/测试/待测试_副本.txt", mode="at+", encoding="utf-8") as  file1:
        with open(r"H:/测试/待测试.txt", mode="at+", encoding="utf-8") as  file2:
            for i in range(10000):
                url="{}{}.php".format(wb_head,num)
                Pool.submit(wb_exists_judge(url,num))
                num+=1