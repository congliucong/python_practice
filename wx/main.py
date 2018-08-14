import os
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
import json
import requests
import traceback
import tornado.escape
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, EventMessage

settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'view'),
            'cookie_secret': 'e440769943b4e8442f09de341f3fea28462d2341f483a0ed9a3d5d3859f==78d',
            'login_url': '/',
            'session_secret': "3cdcb1f07693b6e75ab50b466a40b9977db123440c28307f428b25e2231f1bcc",
            'session_timeout': 3600,
            'port': 80,
            'wx_token': 'weixin',
            }

conf = WechatConf(
    token='weixintoken',
    appid='wx1ed711720d6937a9',
    appsecret='Angel84562',
    encrypt_mode='normal',
    encoding_aes_key='z1TVUN3oA5MMEWd2h49aQAwBQEwimrPMTl1oKwcAaxf'
)


class TulingAutoReply:
    def __init__(self, tuling_key, tuling_url):
        self.key = tuling_key
        self.url = tuling_url

    def reply(self, unicode_str):
        body = {'key': self.key, 'info': unicode_str.encode('utf-8')}
        r = requests.post(self.url, data=body)
        r.encoding = 'utf-8'
        respon = r.text
        if respon is None or len(respon) == 0:
            return None
        else:
            try:
                js = json.loads(respon)
                if js['code'] == 100000:
                    return js['text'].replace('<br>', '\n')
                elif js['code'] == 200000:
                    return js['url']
                else:
                    return None
            except Exception:
                traceback.print_exc()
                return None


wechat = WechatBasic(conf=conf)


auto_reply = TulingAutoReply('691514c677c141d9b779c5f29be17b13', 'http://www.tuling123.com/openapi/api')


class WX(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

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

    def wx_proc_msg(self, body):
        try:
            wechat.parse_data(body)
        except ParseError:
            print
            'Invalid Body Text'
            return
        # 消息是文本消息
        if isinstance(wechat.message, TextMessage):
            content = wechat.message.content
            reply = auto_reply.reply(content)
            if reply is not None:
                return wechat.response_text(content=reply)
            else:
                return wechat.response_text(content=u"我不是很懂你在说什么~")
            return  wechat.response_text(content=u"知道了")
        elif isinstance(wechat.message, EventMessage):
            if wechat.message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
                return wechat.response_text(content=u"欢迎关注Lcccc的公众号~")
        else:
            return wechat.response_text(content=u"啦啦啦啦~")

    def post(self):
        signature = self.get_argument('signature', 'default')
        timestamp = self.get_argument('timestamp', 'default')
        nonce = self.get_argument('nonce', 'default')
        if signature != 'default' and timestamp != 'default' and nonce != 'default' \
                and wechat.check_signature(signature, timestamp, nonce):
            body = self.request.body.decode('utf-8')
            try:
                result = self.wx_proc_msg(body)
                if result is not None:
                    self.write(result)
            except IOError as e:
                return


web_handlers = [
        (r'/wx80', WX),
        ]

define("port", default=settings['port'], help="run on the given port", type=int)

if __name__ == '__main__':
    app = tornado.web.Application(web_handlers, **settings)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()