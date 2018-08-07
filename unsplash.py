from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import time


class BeautifulPicture():

    def __init__(self):
        # ������ָ��һ������ͷ��ģ��chrome�����
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 '
                                      '(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
        # Ҫ���ʵĵ�ַ
        self.web_url = 'https://unsplash.com'
        self.folder_path = 'D:\python\BeautifulPicture'

    def get_pic(self):
        print("��ʼ��ҳ����")
        # ʹ��selenium ͨ��phantomjs��������������
        driver = webdriver.PhantomJS()
        driver.get(self.web_url)
        # ִ����ҳ�������ײ������� ִ������
        self.sroll_down(driver=driver, times=3)
        print("��ʼ��ȡ����div��ǩ")
        all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('div', class_='cV68d')
        print('��ʼ�����ļ���')
        is_new_folder = self.mkdir(self.folder_path)
        print('��ʼ�л��ļ���')
        os.chdir(self.folder_path)
        print("div��ǩ�������ǣ�", len(all_a))
        for a in all_a:
            img_str = a['srcset']
            print("a��ǩ��style������", img_str)


    def save_img(self, url, file_name):
        print("��ʼ����ͼƬ��ַ��������������������������������������������������")
        img = self.get_pic(url)

    def sroll_down(self, driver, times):
        for i in range(times):
            print("��ʼִ�е�", str(i+1), "����������")
            # ִ��js��������
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("��", str(i+1), "����������ִ�����")
            print("��", str(i + 2), "�εȴ���ҳ����")
            # �ȴ�30�룬ҳ����س�����ִ����������
            time.sleep(30)