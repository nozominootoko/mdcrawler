import os

import requests
from lxml import etree
import comic
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()  # 声明一个谷歌配置对象
opts.headless = True
browser = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chromedriver.exe", options=opts)  # 选项注入

url = "http://manhua.dmzj.com/jiroushaonvyalingnengjuduoshaogongjin/"
co = comic.comic()
req = requests.get(url)
html = req.text
parser = etree.HTMLParser()
p = etree.fromstring(html, parser)

name = p.xpath("//*[@class=\"anim_title_text\"]//h1")[0].text
co.name = name
author = p.xpath("//*[@class=\"anim-main_list\"]//tr[3]//a")[0].text
co.author = author
area = p.xpath("//*[@class=\"anim-main_list\"]//tr[4]//a")[0].text
co.area = area
status = p.xpath("//*[@class=\"anim-main_list\"]//tr[5]//a")[0].text
co.status = status
date = p.xpath("//*[@class=\"anim-main_list\"]//tr[9]//span")[0].text
co.date = date
tags = p.xpath("//*[@class=\"anim-main_list\"]//tr[7]//a")[0].text.split(" ")
co.tags = tags
latest = p.xpath("//*[@class=\"anim-main_list\"]//tr[9]//a")[0].text
co.latest = latest
fmurl = p.xpath("//*[@class=\"anim_intro_ptext\"]//img")[0].attrib['src']
hualist = []  # 每话的网址
tps = p.xpath("//*[@class=\"cartoon_online_border\"]//a")

for tp in tps:
    hualist.append(tp.attrib['href'])
if not os.path.exists("./" + name):
    os.mkdir("./" + name)
with open("./" + name + "/fm.jpg", "wb") as f:
    headers = {
        'DNT': '1',
        'Referer': 'http',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    r = requests.get(fmurl, headers=headers)
    if not r.status_code == 403:
        f.write(r.content)
downlog = open("./" + name + "/downlog", "a+")
downlines = downlog.readlines()
for hua in hualist:
    prefix = "http://manhua.dmzj.com"
    url = prefix + hua
    browser.get(url)
    # 获取本话名称
    lparser = etree.HTMLParser()
    lp = etree.fromstring(browser.page_source, lparser)
    huaname = lp.xpath("//*[@class=\"display_middle\"]//span")[0].text
    # 创建每话的文件夹
    huapath = "./" + name + "/" + huaname + "/"
    if not os.path.exists(huapath):
        os.mkdir(huapath)
    picurls = lp.xpath(".//*[@id=\"page_select\"]//option")
    if huapath in downlines:
        continue
    downlog.write(huapath + "\n")
    downlog.flush()
    i = 1
    for pu in picurls:
        pic_url = pu.attrib['value']
        pic_name = "0" + str(i) + ".jpg"
        # 下载每页
        pic_path = huapath + pic_name
        if not os.path.exists(pic_path):
            with open(pic_path, "wb+") as f:
                down = requests.get("https:" + pic_url)
                f.write(down.content)
                print("已下载" + pic_path)
                time.sleep(1)
                i += 1
browser.close()
co.save_to_file()
downlog.close()
# 下载漫画
# 1、创建漫画文件夹
