# coding=UTF-8
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
        self.sroll_down(driver=driver, times=1)
        print(driver.page_source)
        print("开始获取所有div标签")
        all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('img', class_='_2zEKz')

        print('开始创建文件夹')
        is_new_folder = self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        print("div标签的数量是：", len(all_a))
        # 获取文件夹中所有文件名，类型为list
        file_names = self.get_files(self.folder_path)
        for a in all_a:
            img_str = a['src']
            print("a标签的src内容是", img_str)
            first_pos = 0
            second_pos = img_str.index('?ixlib')

            # 使用python切片功能截取双引号之间的内容
            img_url = img_str[first_pos: second_pos]
            # 截取url中参数前面、网址后面的字符串为图片名
            name_start_pos = img_url.index('.com/') + 5
            name_end_pos = len(img_url)
            img_name = img_url[name_start_pos: name_end_pos] + '.jpg'
            print(img_name)
            img_name = img_name.replace('/', '')

            if is_new_folder:
                self.save_img(img_url, img_name)
            else:
                if img_name not in file_names:
                    self.save_img(img_url, img_name)
                else:
                    print("该图片已经存在：", img_name, "不再重新下载")

    def get_files(self, path):
        pic_names = os.listdir(path)
        return pic_names

    def save_img(self, url, file_name):
        print("开始请求图片地址·························")
        img = self.request(url)
        print("开始保存图片")
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def request(self, url):
        r = requests.get(url)
        return r

    def sroll_down(self, driver, times):
        for i in range(times):
            print("开始执行第", str(i+1), "次下拉操作")
            # 执行js下拉操作
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("第", str(i+1), "次下拉操作执行完毕")
            print("第", str(i+1), "次等待网页加载")
            # 等待30秒，页面加载出来再执行下拉操作
            time.sleep(30)

    def mkdir(self, path):
        path = path.strip()
        isexists = os.path.exists(path)
        if not isexists:
            print("创建名字叫做：", path, "的文件夹")
            os.makedirs(path)
            print("创建成功")
            return True
        else:
            print("文件夹已经存在，不再创建")
            return False

beauty = BeautifulPicture()
beauty.get_pic()