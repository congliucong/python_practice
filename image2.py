# coding=UTF-8
import requests
import re
import base64
import  json
import  time
def image2(url):
    imgcontent = requests.get(url).content
    img = base64.b64encode(imgcontent)
    url = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'
    r = requests.post(url, data=img)
    j = json.loads(r.content.decode('utf-8'))
    img_url = j['Host'] + j['Url']
    url2 ='http://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi&tid=87fb67a170ff4912b3afbf4cf0cd6c1c'
    t = time.time()
    data1 = {
        'MsgId': int(round(t * 1000)),
        'CreateTime': int(t),
        'Content[imageUrl]': img_url
    }
    r2 = requests.post(url2, data=data1)
    j2 = json.loads(r2.content.decode('utf-8'))
    return j2

print(image2('http://mmbiz.qpic.cn/mmbiz_jpg/yLBTWsibAkU0aicE1VNKPyZaU4RCGp1VStQ6iaGibj1ciakX4crGBTkFDooSEvVNWyTlMPbGGUxNgPr3IcgaAKLmcbA/0'))

