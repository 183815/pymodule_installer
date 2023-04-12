import os, shutil, requests, decimal, random, time, smtplib, hashlib, copy, csv, imageio, moviepy, ez_setup, \
    ffmpeg, json, datetime, re, bs4, lxml, cv2, turtle, parsel, pprint, subprocess, asyncio, aiohttp, xlwt, \
    configparser, tqdm, math, xlrd, pymysql, wxpy


class get_proxy:
    def __init__(self):
        self.proxy_Path="H:\项目\数据\ProxyAgent.txt"
        self.proxy_list = []
        self.proxies={}

    def get_proxy_list(self):
        with open(self.proxy_Path,"rt",encoding="utf-8") as fp:
            old_proxy_list=fp.readlines()
            for old_proxy in old_proxy_list:
                self.proxy_list.append(old_proxy.replace("\n",""))
        return self.proxy_list

    def get_random_proxy(self):
        #直接调用，节省代码量
        self.proxy_list=self.get_proxy_list()
        return random.choice(self.proxy_list)

    def get_newest_proxy(self):
        self.proxy_list=self.get_proxy_list()
        return self.proxy_list[0]