import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver  #导入Selenium

class One():
    def __init__(self):
        self.headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        self.web_url = 'http://wufazhuce.com/'  # 要访问的网页地址
        self.folder_path = "D:\wx"
        r = requests.get(self.web_url)
        self.soup = BeautifulSoup(r.text, features="html5lib")

    def get_pic(self):
        img_url = self.soup.find_all('img', class_='fp-one-imagen')[0]['src']
        title = self.soup.find_all('div', class_='fp-one-cita')[0].text.strip()
        start_pos = img_url.index('com/')
        img_name = img_url[start_pos+4:len(img_url)] + '.jpg'
        # 创建文件夹
        self.mkdir(self.folder_path)
        # 切换文件夹
        os.chdir(self.folder_path)
        self.save_img(img_url, img_name)


    def get_page(self):
        page = self.soup.find_all('p', class_='one-articulo-titulo')[0].contents[1]
        page_url = page['href']
        print(page_url)
        driver = webdriver.PhantomJS()
        driver.get(page_url)
        driver.save_screenshot('D:/wx/foq.png')



    def save_img(self, url, file_name):
        print("开始请求图片地址·························")
        img = requests.get(url)
        print("开始保存图片")
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, "图片保存成功！")
        f.close()

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

one = One()
one.get_pic()