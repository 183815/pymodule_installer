import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel

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

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""
def write_wb(wb):
    path="H:/测试/已测试1.txt"
    with open(path,"at") as fp:
        fp.write(wb)

def flush_wb(wb):
    path="H:/测试/待测试1.txt"
    with open(path,"at") as fp:
        fp.write(wb)

if __name__ == "__main__":
    wb_path="H:/测试/待测试.txt"
    new_wb_list=[]
    index=51
    with open(wb_path,"r") as fp:
        old_wb_list =fp.readlines()
    old_wb_list_lenth=len(old_wb_list)
    print("总网址个数为:{}".format(old_wb_list_lenth))
    for i in range(0,index):
        write_wb(old_wb_list[i])
    for i in range(index,old_wb_list_lenth):
        flush_wb(old_wb_list[i])
