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


if __name__ == "__main__":
    ua=UserAgent()
    referer = "https://www.douyin.com/discover"
    data={
        "mix_mode":"1",
        "account":"2e3d332534323633333c3330343532",
        "password":"767c7f343d363d3430",
        "account_type":"0",
        "service":"https://www.douyin.com",
        "fixed_mix_mode":"1"
    }
    headers={
        "User_Agent":ua.firefox,
        "referer":referer
    }
    url="https://www.douyin.com/discover"
    session=requests.session()
    session.post(url=url,data=data,headers=headers)
    res=session.get(url=url,headers=headers)
    html=res.text
    pprint.pprint(html)