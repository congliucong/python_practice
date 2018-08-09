# coding=UTF-8
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import time


class Jay_Zhou():

    def __init__(self):
        # 请求地址
        self.request_url = "https://music.163.com/#/artist/album?id=6452&limit=120&offset=0"
        # 保存地址
        self.floder_path = "D:\python\Jay"

    def get_pictures(self):
        print("开始表演")
        driver = webdriver.PhantomJS()
        driver.get(self.request_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source
        # 创建文件夹
        self.mkdir(self.floder_path)
        # 切换文件夹
        os.chdir(self.floder_path)
        file_names = self.get_files(self.floder_path)

        all_li = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        for li in all_li:
            album_img = li.find('img')['src']
            album_name = li.find('p')['title']
            album_date = li.find('span', class_='s-fc3').get_text()
            end_pos = album_img.index('?')
            album_img_url = album_img[:end_pos]
            photo_name = album_name.replace('/', '').replace(':', '') + '-' + str(album_date) + '.jpg'
            print(album_img_url, photo_name)
            if photo_name in file_names:
                print("图片已经存在，不再重新下载")
            else:
                self.save_img(album_img_url, photo_name)

    def save_img(self, url, file_name):
        print("开始请求图片地址·························")
        img = self.request(url)
        print("开始保存图片")
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, "图片保存成功！")
        f.close()

    def request(self, url):
        r = requests.get(url)
        return r

    # 创建文件夹
    def mkdir(self, path):
        path = path.strip()
        isexists = os.path.exists(path)
        if not isexists:
            print("创建名为", path, "的文件夹")
            os.mkdir(path)
            print("创建成功")
            return True
        else:
            print(path, "文件夹已经存在，不需要再创建")
            return False

    def get_files(self, path):
        pic_names = os.listdir(path)
        return pic_names

album_cover = Jay_Zhou()
album_cover.get_pictures()