import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, numpy, \
    ez_setup, ffmpeg, json, datetime, re
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
def Get_UA():
    ua=UserAgent()
    brower_list=["ie","firefox"]
    browser=random.choice(brower_list)
    if browser=="ie":
        return ua.ie
    else:
        return ua.firefox

if __name__=="__main__":
    ua=Get_UA()
