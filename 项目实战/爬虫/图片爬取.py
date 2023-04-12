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
from multiprocessing.dummy import Pool
from lxml import etree

"""
网易邮箱授权码163:HCSADAHITHADZOJQ
QQ授权码:phmvmsxsdgtpdfia
网易邮箱授权码126:XETKLGOBZOYIZBAL
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
"""
#对图片url进行get请求下载
def get_img(url,img_path):
    headers={
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    res=requests.get(url=url,headers=headers)
    html=res.content
    with open(img_path,"wb") as fp:
        fp.write(html)



#从本地文件读取php链接
def get_url_list():
    file_path="H:/测试/待测试.txt"
    new_url_lists=[]
    with open(file_path,"r") as fp:
        old_url_lists=fp.readlines()
    for old_url_list in old_url_lists:
        new_url_lists.append(old_url_list.strip())
    return new_url_lists


def update_php(new_list,old_list):  #更新文件
    new_file="H:/测试/待测试.txt"
    old_file = "H:/测试/已测试.txt"
    with open(new_file, "wt") as fp1:   #刷新待测试文件
        for php in new_list:
            fp1.write("{}\n".format(php))
        fp1.flush()
    with open(old_file, "at") as fp2:   #刷新已测试文件
        for php in old_list:
            fp2.write("{}\n".format(php))
        fp2.flush()


def deduplication_already():#对已测试列表进行去重和排序
    already_test_file= "H:/测试/已测试.txt"
    with open(already_test_file,"rt") as fp:
        lines=list(set(fp.readlines()))
        lines.sort(reverse=True)
    with open(already_test_file, "wt") as fp:
        for line in lines:
            fp.write(line)


# def thread_pool(func,page_url_list):
#     pool=Pool(10)
#     pool.map(func,page_url_list)
#     pool.close()
#     pool.join()


def img_url_xpath(file_name,page_url,schedule_table):
    # 对每页的url进行xpath解析
    headers={
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    file_path="H:\图片\美女图片\{}".format(file_name)
    res=requests.get(url=page_url,headers=headers)
    html=res.text
    tree=etree.HTML(html)
    p_list=tree.xpath('/html/body/div[1]/div/div[1]/p')
    #对每页的图片都新建一个文件夹
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    #对每张图片都标个序号
    img_num = 0
    #对li列表进行xpath解析
    for p in p_list:
        if p.xpath('./img/@src'):   #检测该返回的src列表是否为空
            img_url=p.xpath('./img/@src')[0] #获取图片url
            img_path="H:/图片/美女图片/{}/{}.jpg".format(file_name,img_num)  #对图片路径进行拼接
            get_img(img_url,img_path)
            std_out(schedule_table,img_path)
            img_num += 1    #图片序列号+1


def page_url_xpath(page_url,schedule_table):
    # 对每行的php进行xpath解析
    if page_url:
        file_name = re.findall("http://1.weihuasdgs.com.cn/1/(.*?).php", page_url)[0]
        img_url_xpath(file_name,page_url,schedule_table)


def std_out(schedule_table,img_path):
    print("当前进度为:{}————{}--下载成功".format(schedule_table,img_path),end="")


if __name__ == "__main__":
    page_url_list=get_url_list()    #获取的每页url
    page_url_list_lenth=len(page_url_list)  #总的页面数量
    new_list=[]
    old_list=[]
    for page_url in page_url_list:    #将php复制到new_list列表中
        new_list.append(page_url)
    schedule=0
    #不断提取每页的url
    for page_url in page_url_list:
        schedule_table="\r下载完成：{}/{}".format(schedule,page_url_list_lenth)
        page_url_xpath(page_url,schedule_table)
        # thread_pool(page_url_xpath,page_url_list)  #多线程下载
        new_list.remove(page_url)   #更新待测试列表
        old_list.append(page_url)   #更新已测试列表
        update_php(new_list,old_list)   #更新已测试和待测试文件
        deduplication_already()  # 对已测试列表进行去重
        schedule += 1
    print("下载完成100%")