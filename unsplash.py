from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import time


class BeautifulPicture():

    def __init__(self):
        # 给请求指定一个请求头来模拟chrome浏览器
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 '
                                      '(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
        # 要访问的地址
        self.web_url = 'https://unsplash.com'
        self.folder_path = 'D:\python\BeautifulPicture'

    def get_pic(self):
        print("开始网页请求")
        # 使用selenium 通过phantomjs来进行网络请求
        driver = webdriver.PhantomJS()
        driver.get(self.web_url)
        # 执行网页下拉到底部操作， 执行三次
        self.sroll_down(driver=driver, times=3)
        print("开始获取所有div标签")
        all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('div', class_='cV68d')
        print('开始创建文件夹')
        is_new_folder = self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        print("div标签的数量是：", len(all_a))
        for a in all_a:
            img_str = a['srcset']
            print("a标签的style内容是", img_str)


    def save_img(self, url, file_name):
        print("开始请求图片地址·························")
        img = self.get_pic(url)

    def sroll_down(self, driver, times):
        for i in range(times):
            print("开始执行第", str(i+1), "次下拉操作")
            # 执行js下拉操作
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("第", str(i+1), "次下拉操作执行完毕")
            print("第", str(i + 2), "次等待网页加载")
            # 等待30秒，页面加载出来再执行下拉操作
            time.sleep(30)