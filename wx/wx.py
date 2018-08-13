import tornado
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

conf = WechatConf(
    token='weixintoken',
    appid='wx1ed711720d6937a9',
    appsecret='Angel84562',
    encrypt_mode='normal',
    encoding_aes_key='z1TVUN3oA5MMEWd2h49aQAwBQEwimrPMTl1oKwcAaxf'
)
wechat = WechatBasic(conf=conf)


class WX(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument('signature', 'default')
        timestamp = self.get_argument('timestamp', 'default')
        nonce = self.get_argument('nonce', 'default')
        echostr = self.get_argument('echostr', 'default')
        if signature != 'default' and timestamp != 'default' and nonce != 'default' and echostr != 'default' \
                and wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write('Not Open')
