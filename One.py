import requests
from bs4 import BeautifulSoup

class One():
    def __init__(self):
        self.headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        self.web_url = 'http://wufazhuce.com/'  # 要访问的网页地址
        self.folder_path = 'D:\wx'

    def get_pic(self):
        r = requests.get(self.web_url)
        img_div = BeautifulSoup(r.text, 'lxml').find_all('a', class_='fp-one-imagen')
        first_page = img_div[0]
        for a in img_div:
            img_url = a['src']
            print(img_url)

one = One()
one.get_pic()