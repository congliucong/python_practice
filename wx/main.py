import os
import tornado.web
import tornado.httpserver
from tornado.options import define, options
import tornado
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'view'),
            'cookie_secret': 'e440769943b4e8442f09de341f3fea28462d2341f483a0ed9a3d5d3859f==78d',
            'login_url': '/',
            'session_secret': "3cdcb1f07693b6e75ab50b466a40b9977db123440c28307f428b25e2231f1bcc",
            'session_timeout': 3600,
            'port': 8800,
            'wx_token': 'weixin',
            }

conf = WechatConf(
    token='weixintoken',
    appid='wx1ed711720d6937a9',
    appsecret='Angel84562',
    encrypt_mode='normal',
    encoding_aes_key='z1TVUN3oA5MMEWd2h49aQAwBQEwimrPMTl1oKwcAaxf'
)
wechat = WechatBasic(conf=conf)


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


web_handlers = [
        (r'/wx', WX),
        ]

define("port", default=settings['port'], help="run on the given port", type=int)

if __name__ == '__main__':
    app = tornado.web.Application(web_handlers, **settings)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()