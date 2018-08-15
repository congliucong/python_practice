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
    data = {
        'MsgId': int(round(t * 1000)),
        'CreateTime': int(t),
        'Content[imageUrl]': img_url
    }
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/68.0.3440.84 Safari/537.36',
        'Cookie': 'cpid=GDYkSSc2PjUiNS9OfzFWSs1MFjcfsVkxXU_DtFhM0DROAA; salt=6CFF0CF1C9C28722E1D01AEB1F27FB1C; ARRAffinity=8b8a8be852985dae037d393620848ea4328b01c42b3600412006908712f513ce; ai_user=GB5XH|2018-08-15T02:27:21.980Z; ai_session=fDqhR|1534300043087.5|1534300043087.5',
        'Referer': 'http://kan.msxiaobing.com/V3/Portal?task=yanzhi&ftid=f6aca7ed5a784ad0be60d8ec94bf19a1'
    }
    r2 = requests.post(url2, data=data, headers=head)
    j2 = json.loads(r2.content.decode('utf-8'))
    return j2

print(image2('https://mediaplatform.msxiaobing.com/image/fetchimage?key=EjJdtJA119BQNNF3GjYDcxIxGzE1dlECBGdPVwgDMFMWIyozFycACy4A'))

