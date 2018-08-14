import json
import requests
import traceback

class TulingAutoReply:
    def __init__(self, tuling_key, tuling_url):
        self.key = tuling_key
        self.url = tuling_url

    def reply(self, unicode_str):
        body = {'key': self.key, 'info': unicode_str.encode('utf-8'), 'userid': self.key[0:16]}
        r = requests.post(self.url, data=body)
        r.encoding = 'utf-8'
        respon = r.text
        if respon is None or len(respon) == 0:
            return None
        else:
            try:
                js = json.loads(respon)
                if js['code'] == 100000:  # 文本
                    return js['text'].replace('<br>', '\n')
                elif js['code'] == 200000:  # 链接
                    return js['url']
                elif js['code'] == 302000:  # 新闻
                    return js['text']+'\n'+js['list'][0]['article']+'\n'+js['list'][0]['detailurl']
                elif js['code'] == 308000:  # 菜谱
                    return js['text']+'\n'+js['list'][0]['info']+'\n'+js['list'][0]['detailurl']
                else:
                    return None
            except Exception:
                traceback.print_exc()
                return None