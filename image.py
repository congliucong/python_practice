# coding=UTF-8
import requests
import re
def img(url):
    imgcontent = requests.get(url).content
    url = 'https://cn.how-old.net/Home/Analyze?isTest=False&source=&version=cn.how-old.net'
    data = {'file': imgcontent}
    r =requests.post(url, files=data).content.decode('utf-8').replace('\\', '')
    print(r)
    gender = re.search(r'"gender": "(.*?)"', r)
    age = re.search(r'"age": (.*?),', r)
    if gender.group(1) == 'Female':
        gender = '女'
    else:
        gender = '男'

    result = [gender, age.group(1)]
    return result
