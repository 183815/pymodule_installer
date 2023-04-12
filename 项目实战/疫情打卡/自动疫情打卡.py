import os, shutil, zipfile, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, docx, xlwt

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

class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

if __name__ == "__main__":
    excutable_path = "H:/测试/浏览器驱动/chromedriver.exe"
    url="https://yqfk.sicau.edu.cn/Web/Account/ChooseType"
    file_path="H:/截图"
    img_path="{}/截图.png".format(file_path)
    code_img_path="{}/验证码.png".format(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    browser=webdriver.Chrome(executable_path=excutable_path)
    #进入登录界面
    browser.get(url)
    stu_log=browser.find_element(by=By.XPATH,value='//*[@id="teacher"]/a/img')
    stu_log.click()
    #调整浏览器页面布局
    # browser.execute_script('document.body.style.zoom="0.8"')

    #自动识别验证码（需要消耗积分）
    # #截图
    # browser.save_screenshot(img_path)
    # #对验证码进行定位
    # code_img_ele=browser.find_element(by=By.XPATH,value='//*[@id="code-box"]')
    # location=code_img_ele.location
    # size=code_img_ele.size
    # rangle=(int(location['x']),int(location['y']),int(location['x'])+int(size['width']),int(location['y']+int(size['height'])))
    # #对验证码区域进行确定并截图
    # i=Image.open(img_path)
    # frame=i.crop(rangle)
    # frame.save(code_img_path)
    # #使用超级鹰对验证码进行识别
    # chaojiying = Chaojiying_Client('17366965107','syz183815','929853')	#用户中心>>软件ID 生成一个替换 96001
    # im = open(code_img_path, 'rb').read()									#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # check_code=chaojiying.PostPic(im, 3004)
    # code=check_code['pic_str']
    # print(check_code)

    #手动识别验证码（免费不过麻烦）
    code=input("请输入验证码：")
    #登录操作
    stu_id=browser.find_element(by=By.XPATH,value='//*[@id="StudentId"]')
    stu_id.send_keys('201803029')
    name=browser.find_element(by=By.XPATH,value='//*[@id="Name"]')
    name.send_keys('183815')
    code_btn=browser.find_element(by=By.XPATH,value='//*[@id="codeInput"]')
    code_btn.send_keys(code)
    login_btn=browser.find_element(by=By.XPATH,value='//*[@id="Submit"]')
    login_btn.send_keys(Keys.ENTER)
    #填报操作
    start=browser.find_element(by=By.XPATH,value='//*[@id="platfrom2"]/a/div')
    start.click()
    location_btn=browser.find_element(by=By.XPATH,value='//*[@id="form1"]/div[1]/div[3]/div[2]/div[2]/input')
    location_btn.send_keys('青竹街道')
    browser.execute_script("window.scrollTo(0,100);")
    in_schoole=browser.find_element(by=By.XPATH,value='//*[@id="b073c8ee-499a-4698-aab3-0bb7a1b6d40a"]')
    in_schoole.click()
    reason=browser.find_element(by=By.XPATH,value="//*[@id="form1"]/div[1]/div[4]/div[1]/div[2]/div[3]/div[2]/div/input")
    reason.send_keys("实习")
    inoculate=browser.find_element(by=By.XPATH,value="//*[@id="01dd94b0-c1e5-45f3-b173-69c3d0417d20"]")
    inoculate.click()
    # browser.quit()