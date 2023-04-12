import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
 json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, ffmpeg

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

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
def spider(url):
    headers={
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res=requests.get(url=url,headers=headers)
    return res
"""
# def write_html(html):
#     html_path="H://测试/html.txt"
#     with open(html_path,"wt",encoding="utf-8") as fp:
#         fp.write(html)

#TODO：还有防盗链参数问题待解决
def spider(url):
    headers={
        "referer": "https://space.bilibili.com/38407276/channel/collectiondetail?sid=1636",
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res=requests.get(url=url,headers=headers)
    return res


def save_file(url,file_path):
    res=spider(url)
    data=res.content
    with open(file_path,"wb") as fp:
        fp.write(data)
    print("{}————下载成功！".format(file_path))

#TODO:还有视频和音频合并部分待解决
# def composite_file(video_path,audio_path,composite_path):
#     cmd=f"ffmpeg.exe -i {video_path} -i {audio_path} -acodec copy -vcodec copy {composite_path} "
#     subprocess.run(cmd,shell=True)


def download_url(json_data,title):
    print("视频下载中……")
    #获取视频url
    video_url=json_data['data']['dash']['video'][0]['base_url']
    video_name=title+".mp4"
    #获取音频url
    audio_url=json_data['data']['dash']['audio'][0]['base_url']
    audio_name=title+".mp3"
    #保存视频
    video_path="{}/{}".format(file_path,video_name)
    save_file(video_url,video_path)
    #保存音频
    audio_path = "{}/{}".format(file_path, audio_name)
    save_file(audio_url,audio_path)
    composite_path ="{}/composited_{}".format(file_path,video_name)
    # composite_file(video_path,audio_path,composite_path)
    print("视频下载完成！")


if __name__ == "__main__":
    url="https://space.bilibili.com/38407276/channel/collectiondetail?sid=1636"
    file_path="H:/视频/哔哩哔哩"
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    res=spider(url)
    html=res.text
    title=re.findall('<span class="tit">(.*?)</span>',html)[0]
    info=re.findall('<script>window.__playinfo__=(.*?)</script>',html)[0]
    json_data=json.loads(info)
    download_url(json_data,title)